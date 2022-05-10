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
        
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
        print("=============================================")
        print("Маршрут из " + (orig) + " в " + (dest))
        print("Продолжительность поездки: " + (json_data["route"]["formattedTime"]))
        print("Километры:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Использованное топливо (Литр.): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " км)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Статус: " + str(json_status) + "; Неверные данные пользователя для одной или обеих локаций.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Статус: " + str(json_status) + "; Отсутствие записи для одного или обоих мест.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Для статуса: " + str(json_status) + "; Обратитесь:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
