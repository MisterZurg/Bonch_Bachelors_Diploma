# Учитывая значение радиуса, выведите длинну окружности.
# Длинна окружности вычисляется по формуле: c = pi * 2 * radius

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue


    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Длина окружности c hflbecjv" + str(self.radius) + " равна " + str(myCircumference))

# Первый экземпляр класса Circle.
circle1 = Circle(2)
# Вызовите функцию printCircumference для экземпляра circle1.
circle1.printCircumference()

# Ещё два экземпляра класса Circle.
circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()
