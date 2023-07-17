import requests

def get_weather_desc_and_temp():
    api_key = "14c67f8f81d863db391cc6e653ac226d"
    lat = str(32.94089)
    lon = str(-117.24099)
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = round(json.get("main").get("temp_min"))
    temp_max = round(json.get("main").get("temp_max"))

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
def main():        
    weather_dict = get_weather_desc_and_temp()
    #Print the results
    print("Today's forecast is", weather_dict.get('description'))
    print("with a high of", weather_dict.get('temp_max'), "and a low of", weather_dict.get('temp_min'))

main()