import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime
from pytz import timezone

# Load the Random Forest model from pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

openweatherapikey = 'YOUR API KEY'

# Flask App Initialization
app = Flask(__name__)
CORS(app)

# Convert square feet to square meters
def convert_area_to_sqm(area_in_fts):
    return area_in_fts * 0.092903

# Fetch real-time weather data from OpenWeather API
def get_weather_data(lat, lon, api_key):
    # URL to fetch weather data using latitude and longitude
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_dir = data['wind']['deg']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']

        # Get current time and convert to day of year
        now = datetime.now()
        day_of_year = now.timetuple().tm_yday
        time_of_day_s = 10 * 60 * 60  # Fixed time for 10:00 AM

        return {
            'Temperature': temp,
            'Humidity': humidity,
            'WindDirection': wind_dir,
            'WindSpeed': wind_speed,
            'Pressure': pressure,
            'DayOfYear': day_of_year,
            'TimeOfDay(s)': time_of_day_s
        }
    else:
        return None

# Prediction function
def predict_solar_energy(temp, humidity, wind_dir, wind_speed, day_of_year, time_of_day_s, pressure, area, panel_power_rating, avg_daily_sun_hours, derate_factor, cost_per_kWh, panel_cost, installation_cost):
    input_data = pd.DataFrame({
        'Temp in Celcius': [temp],
        'Humidity': [humidity],
        'WindDirection(Degrees)': [wind_dir],
        'Speed': [wind_speed],
        'Pressure': [pressure],
        'DayOfYear': [day_of_year],
        'TimeOfDay(s)': [time_of_day_s]
    })

    # Predict solar radiation (kWh/m²/day)
    solar_radiation = model.predict(input_data)[0]
    solar_density = solar_radiation / 24
    total_power_gen_capacity = solar_density * area
    num_solar_panels = total_power_gen_capacity / panel_power_rating
    daily_energy_production = total_power_gen_capacity * avg_daily_sun_hours * derate_factor
    annual_energy_production = daily_energy_production * 365
    annual_cost_savings = annual_energy_production * cost_per_kWh
    total_investment = (num_solar_panels * panel_cost) + installation_cost
    payback_period = total_investment / annual_cost_savings if annual_cost_savings > 0 else float('inf')

    return {
        'solar_radiation (kWh/m²/day)': solar_radiation,
        'solar_density (kWh/m²/hour)': solar_density,
        'total_power_gen_capacity (kW)': total_power_gen_capacity,
        'num_solar_panels': num_solar_panels,
        'daily_energy_production (kWh)': daily_energy_production,
        'annual_energy_production (kWh)': annual_energy_production,
        'annual_cost_savings': annual_cost_savings,
        'total_investment': total_investment,
        'payback_period (years)': payback_period
    }

def get_values(purpose):
    if purpose == "Industry" or purpose == "Agriculture":
        panel_power_rating = 0.3  # kW
        derate_factor = 0.8
        panel_cost = 18000  # ₹ per panel (approximate cost of a polysrystalline solar panel in India)
        installation_cost = 50000  # ₹ (approximate installation cost in India)
    elif purpose == "IT" or purpose == "Domestic":
        panel_power_rating = 0.35  # kW
        derate_factor = 0.85
        panel_cost = 25000  # ₹ per panel (approximate cost of a monocrystalline solar panel in India)
        installation_cost = 60000  # ₹ (approximate installation cost in India)
    else:
        raise ValueError("Invalid purpose")
    
    return panel_power_rating, derate_factor, panel_cost, installation_cost

# Flask App Initialization
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Fetch data from request payload
    area_in_fts = data.get('areaSize')  # Area size in square meters from frontend
    marker_coords = data.get('marker')  # Lat/lon marker coordinates
    purpose = data.get('category')  # Purpose (Industry, Agriculture, IT, etc.)

    # Ensure all inputs are available
    if not area_in_fts or not marker_coords or not purpose:
        return jsonify({'error': 'Missing input data'}), 400

    # Fetch lat and lon from marker_coords
    lat = marker_coords.get('lat')
    lon = marker_coords.get('lng')

    if lat is None or lon is None:
        return jsonify({'error': 'Invalid marker coordinates'}), 400

    # Fetch weather data
    weather_data = get_weather_data(lat, lon, openweatherapikey)

    if not weather_data:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    # Convert area to square meters (area is already in square meters)
    area = area_in_fts
  
    # Get purpose-specific values (adjust this logic based on your requirement)
    panel_power_rating, derate_factor, panel_cost, installation_cost = get_values(purpose)
    print("x")
    # Use the fetched weather data for prediction
    result = predict_solar_energy(
        weather_data['Temperature'], weather_data['Humidity'],
        weather_data['WindDirection'], weather_data['WindSpeed'],
        weather_data['DayOfYear'], weather_data['TimeOfDay(s)'],
        weather_data['Pressure'], area, panel_power_rating,
        5, derate_factor, 8, panel_cost, installation_cost
    )
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
