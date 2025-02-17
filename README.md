# Solar Wave: Rooftop Solar Energy Potential Mapping

## Overview
Solar Wave is a deep learning-based system for mapping rooftop solar energy potential. It integrates machine learning, geospatial tools like OpenStreetMap (OSM), and interactive mapping technologies (Leaflet.js) to provide accurate estimations of rooftop solar power generation. The platform is designed to assist policymakers, urban planners, and businesses in optimizing solar installations, particularly in the Indian subcontinent. This initiative addresses the growing need for renewable energy adoption while providing scalable and user-friendly insights for diverse stakeholders.

## Features
- **Automated Rooftop Detection**: Uses deep learning (U-Net, Mask R-CNN) for high-accuracy building footprint extraction from satellite imagery.
- **Interactive Mapping**: Integrates OpenStreetMap (OSM) and Leaflet.js for user-friendly visualization and data exploration.
- **Advanced Solar Irradiance Estimation**: Computes effective solar exposure using dynamic irradiance models, adjusting for seasonal variations.
- **Energy Production Forecasting**: Predicts rooftop solar generation potential considering shading, orientation, and environmental factors.
- **Scalability & Cloud Integration**: Designed for large-scale implementation with cloud-based architecture support, enabling real-time data processing.
- **Environmental Impact Assessment**: Estimates carbon emission reductions from solar energy adoption and potential cost savings.
- **Decision Support System**: Provides intelligent recommendations for solar panel placement and expected ROI analysis.

## Methodology
1. **Data Preprocessing**: 
   - Extract building footprints from OSM using the Overpass API.
   - Apply image processing techniques (cloud removal, noise reduction) to enhance data quality.
   - Standardize solar irradiance and temperature data for accurate energy modeling.
   - Implement GIS-based terrain analysis to refine rooftop suitability metrics.

2. **Deep Learning-Based Building Footprint Extraction**:
   - Train U-Net and Mask R-CNN models for automated rooftop segmentation.
   - Refine extracted footprints to ensure precision in solar potential estimation.
   - Perform post-processing techniques to reduce false positives and enhance segmentation accuracy.

3. **Solar Energy Potential Estimation**:
   - Calculate usable rooftop area, accounting for obstructions like HVAC units and other structural elements.
   - Compute solar irradiance impact using solar zenith angle, orientation, and advanced radiation models.
   - Estimate annual energy generation, efficiency metrics, and carbon footprint reduction.

4. **Interactive Visualization & Accessibility**:
   - Implement Leaflet.js for an intuitive, web-based solar mapping platform.
   - Provide real-time data exploration with geospatial overlays and dynamic filtering options.
   - Offer customizable reports and export functionalities for stakeholders.

## Applications
- **Urban Planning**: Identifying optimal areas for large-scale solar adoption.
- **Industrial and Commercial Use**: Customized solar investment assessments for maximizing cost efficiency.
- **Government & Policy**: Supporting renewable energy initiatives and subsidy programs.
- **Smart Cities**: Integrating solar data for sustainable urban development.
- **Research & Academia**: Enabling data-driven studies on renewable energy potential and climate impact.

## Future Enhancements
- **3D Building Modeling**: Improved shading analysis for precise energy forecasting.
- **IoT Integration**: Real-time monitoring of panel performance and environmental conditions for enhanced accuracy.
- **Financial & Market Integration**: Incentive-based solar planning, dynamic pricing models, and peer-to-peer energy trading mechanisms.
- **Global Expansion**: Adapting the model for diverse geographic regions with localized climate considerations.
- **AI-Driven Optimization**: Implement reinforcement learning models to suggest ideal solar deployment strategies.

## Contributors
- Rahul Dewani (VIIT, Pune, India)
- Spandan Kewte (VIIT, Pune, India)
- Piyush Deshmukh (VIIT, Pune, India)
