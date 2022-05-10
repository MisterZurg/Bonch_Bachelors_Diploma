file = open("devices.txt", "a")
while True:
    newItem = input("Введите имя устройства: ")
    if newItem == "exit":
        print("Всё готово!")
        break
    file.write(newItem + "\n")
file.close()
