import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy"

while True:
    orig = input("Начальное местоположение: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Место назначения: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
        print("=============================================")
        print("Маршрут из " + (orig) + " в " + (dest))
        print("Продолжительность поездки: " + (json_data["route"]["formattedTime"]))
        # Британская имперская система мер:
        # print("Мили: (Гал.)" + str(json_data["route"]["distance"]))
        # print("Использованное топливо: " + str(json_data["route"]["fuelUsed"]))
        
        # Международная система единиц, то что вы используете на физике/химии СИ
        # print("Километры:      " + str((json_data["route"]["distance"])*1.61))
        # print("Использованное топливо (Литр.): " + str((json_data["route"]["fuelUsed"])*3.78))
        
        # Форматирование
        print("Километры:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Использованное топливо (Литр.): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        