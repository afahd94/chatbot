from flask import Flask, render_template, request
import requests

# Flask app setup
app = Flask(__name__)

# External API URL
api_url = 'https://api.weatherapi.com/v1/current.json?key=0a84c32ffb40e99cf8e9908652c005a0&q=Sydney'

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get weather data from the API
@app.route('/weather', methods=['GET'])
def get_weather():
    # Make an API request
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the API response
        weather_data = response.json()
        # Process the data or pass it directly to the template
        return render_template('weather.html', weather=weather_data)
    else:
        return 'Failed to fetch weather data'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
