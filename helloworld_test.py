from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_weather():
    """Fetch current weather for Sydney, AU from OpenWeatherMap.

    Returns a dict with keys: temp, description, icon, humidity, wind
    or None if unavailable.
    """
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return None
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': 'Sydney,AU', 'units': 'metric', 'appid': api_key}
        resp = requests.get(url, params=params, timeout=5)
        if resp.status_code != 200:
            return None
        j = resp.json()
        weather = {
            'temp': j.get('main', {}).get('temp'),
            'description': j.get('weather', [{}])[0].get('description'),
            'icon': j.get('weather', [{}])[0].get('icon'),
            'humidity': j.get('main', {}).get('humidity'),
            'wind': j.get('wind', {}).get('speed')
        }
        return weather
    except Exception:
        return None


@app.route('/')
def hello():
    weather = get_weather()
    return render_template('index.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)


def test_root_status_code():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200


def test_root_contains_hello():
    client = app.test_client()
    resp = client.get('/')
    assert b'Hello, World!' in resp.data


def test_root_content_type_html():
    client = app.test_client()
    resp = client.get('/')
    assert 'text/html' in resp.content_type
