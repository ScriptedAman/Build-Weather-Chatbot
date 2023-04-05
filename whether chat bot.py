import os
import requests
import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

api_key = '7214d3fa1a5345760cf14e4232b81203'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    if data['cod'] == '404':
        return None
    else:
        weather_data = {}
        weather_data['temperature'] = data['main']['temp']
        weather_data['description'] = data['weather'][0]['description']
        return weather_data

def generate_response(user_input):
    tokens = word_tokenize(user_input)
    if 'weather' in tokens:
        for i, token in enumerate(tokens):
            if token == 'in':
                city = ' '.join(tokens[i+1:])
                weather_data = get_weather(city)
                if weather_data is not None:
                    response = f'The temperature in {city} is {weather_data["temperature"]} degrees Celsius with {weather_data["description"]}.'
                else:
                    response = f'Sorry, I could not find weather information for {city}.'
                return response
    return 'Sorry, I did not understand your question.'

while True:
    user_input = input('You: ')
    response = generate_response(user_input)
    print('Bot:', response)
