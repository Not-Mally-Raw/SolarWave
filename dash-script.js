// Line Chart Example (Chart.js)
const ctxLine = document.getElementById('lineChart').getContext('2d');
const lineChart = new Chart(ctxLine, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May'],
        datasets: [{
            label: 'Solar Radiation',
            data: [3.8, 4.0, 4.5, 5.1, 5.6],
            borderColor: '#007bff',
            fill: false,
        }, {
            label: 'Solar Density',
            data: [0.15, 0.16, 0.17, 0.18, 0.19],
            borderColor: '#28a745',
            fill: false,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top',
            }
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Donut Chart Example
const ctxDonut = document.getElementById('donutChart').getContext('2d');
const donutChart = new Chart(ctxDonut, {
    type: 'doughnut',
    data: {
        labels: ['Solar Panels', 'Other Sources'],
        datasets: [{
            data: [75, 25],
            backgroundColor: ['#007bff', '#28a745'],
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top',
            }
        }
    }
});