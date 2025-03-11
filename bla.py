class Rectangle:
    ''' Docstring text here '''

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

    def length_cubed(self):
        return self.length ** 3

rect = Rectangle(4, 5)






class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
point1 = Point(5,3)
point2 = Point(-2,7)
print(point1)
print(point2)



class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return self.firstname

    def set_name(self, text):
        self.firstname = text

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, text):
        self.lastname =text

st1 = Student("Giorgi","Abashidze")
print(st1.get_lastname())
st1.set_lastname("Tchilaia")
print(st1.get_lastname())


