import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy"

while True:
   orig = input("Начальное местоположение: ")
   dest = input("Место назначения: ")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
