import requests

# CONSTANTS
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct?"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = ""  # Enter your api-key


def get_coords(city_name) -> dict:
    """"GETTING COORDINATES FROM CITY NAME"""
    coords = dict()
    # getting of response
    resp = requests.get(url=GEO_URL,
                        params={"q": city_name,
                                "appid": API_KEY,
                                "limit": 1})
    # getting JSON
    res_dict = resp.json()
    # verifying that the city is entered correctly
    if bool(res_dict):
        coords["lat"] = res_dict[0]["lat"]
        coords["lon"] = res_dict[0]["lon"]
    else:
        return "The city is entered incorrectly"
    return coords


def get_weather_dict(coords: dict) -> dict:
    """"GETTING WEATHER FROM COORDS"""
    lat, lon = coords["lat"], coords["lon"]
    result_dict = dict()
    # getting response
    resp = requests.get(url=WEATHER_URL,
                        params={"lat": lat,
                                "lon": lon,
                                "appid": API_KEY,
                                "units": "metric"})
    # getting JSON
    got_dict = resp.json()
    temp = got_dict["main"]["temp"]
    weather = got_dict["weather"][0]["description"]
    wind_speed = got_dict["wind"]["speed"]
    humidity = got_dict["main"]["humidity"]
    pressure = got_dict["main"]["pressure"]
    result_dict["temperature"] = temp
    result_dict["weather"] = weather
    result_dict["wind speed"] = str(wind_speed) + " m/s"
    result_dict["humidity"] = str(humidity) + "%"
    result_dict["pressure"] = str(pressure) + " GPa"
    return result_dict


def main():
    city = input("Enter city name\n").capitalize()
    coords = get_coords(city)
    while type(coords) is str:
        print(coords)
        city = input("Enter city name again\n").capitalize()
        coords = get_coords(city)
    weather_dict = get_weather_dict(coords)
    for key in weather_dict.keys():
        print(f"The {key} in {city} is {weather_dict[key]}.", end=" ")
    print("")


if __name__ == "__main__":
    while True:
        main()