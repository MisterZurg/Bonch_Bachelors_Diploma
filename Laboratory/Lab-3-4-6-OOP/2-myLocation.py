class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country


    def myLocation(self):
        print("Привет, меня зовут " + self.name + ", и я живу в стране " + self.country + ".")


# Первый экземпляр класса Location 
loc1 = Location("Денис", "Россия")
# Вызов метода
loc1.myLocation()

# Ещё три экземпляра и вызова методов для класса Location
loc2 = Location("김현아", "한국")
loc3 = Location("Шерхан", "Казахстан")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Ваше_Имя", "Ваша_Страна")
your_loc.myLocation()
