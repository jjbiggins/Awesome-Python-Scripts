import requests


def get_temperature(json_data):
    return json_data['main']['temp']

def get_weather_type(json_data):
    return json_data['weather'][0]['description']

def get_wind_speed(json_data):
    return json_data['wind']['speed']



def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return (
        weather_details
        + f"The weather in {city} is currently {weather_type} with a temperature of {temperature} degrees and wind speeds reaching {wind_speed} km/ph"
    )


def main():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    city = input("City Name : ")
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    weather_details = get_weather_data(json_data, city)
    # print formatted data
    print(weather_details)



main()