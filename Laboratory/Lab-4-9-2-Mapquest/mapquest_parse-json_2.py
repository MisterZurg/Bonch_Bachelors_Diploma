import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
