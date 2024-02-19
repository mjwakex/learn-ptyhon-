class Circle:
    #initialise the class
    def __init__ (self, x, y ,rad):
        self.x, self.y, self.rad = x, y, rad
    
    def area(self):
        return 3.1415 * self.rad * self.rad

def getArea():
    c = Circle(1,3,69)
    return c.area()

#inheritance
class Human:

    def __init__ (self, name, age):
        self.name, self.age = name, age

    def human_name(self):
        return self.name
    
    def human_age(self):
        return self.age

    def __str__ (self):
        return f"{self.name} is {self.age}"
    
bob = Human("Bob", 69)
print(bob)

class Student(Human):
    #students are also humans
    def __init__ (self, name, age, smart):
        Human.__init__ (self, name, age)
        self.smart = smart
    
    def smart(self):
        return self.smart
    
    def __str__ (self):
        return f"{self.name} is a student who is {self.smart} smart"

bobby = Student("Bobby", 17, True)
print(bobby)

