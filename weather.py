import requests, json
city = input("Enter City: ")
Api_Key = "4976409c5fc4acb53273d2a04b8b63a6"
URL = "https://api.openweathermap.org/data/2.5/weather?"
Complete_Url = URL + "q=" + city + "&appid=" + Api_Key + "&units=metric"
response = requests.get(Complete_Url)
if response.status_code == 200: # checking the status code of the request
   complete_weather_info = response.json()  #Getting data in json format
   weatherInfo = complete_weather_info['main']

   current_temperature = str(weatherInfo['temp'])
   current_humidity = str(weatherInfo['humidity'])
   current_pressure = str(weatherInfo['pressure'])
   print("Weather in " + city + " is:")
   print("Temperature: " + current_temperature + chr(176) + "C")
   print("Humidity: " + current_humidity + "%")
   print("Pressure: " + current_pressure + "hPa")  
else:
	print("Error in the HTTP request")