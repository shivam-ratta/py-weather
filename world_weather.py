import httpx
import os

params = {
    'format': 'json',
    'key': os.getenv("WORLD_WEATHER_KEY")
}

def get_timezone(query):
    params['q'] = query
    data = httpx.get('https://api.worldweatheronline.com/premium/v1/tz.ashx', params=params)
    return data.json()['data']

def get_weather(query):
    params['q'] = query
    data = httpx.get('https://api.worldweatheronline.com/premium/v1/weather.ashx', params=params)
    return data.json()['data']
