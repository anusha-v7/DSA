'''class Car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
    def drive(self):
        print(f"{self.brand},{self.colour} is driving")
my_car=Car("BMW","RED")
my_car.drive()    '''


#Encapsulation keeps the data safe by hiding using private variables

''' class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
acc=Bankaccount(1000)
acc.deposit(500)
print(acc.get_balance()) '''


#Abstraction means hiding complex details and showing only what's neccasary

''' from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*3.14*self.r
class Rectangle(Shape):
    def __init__(self,h,b):
        self.h=h
        self.b=b
    def area(self):
        return self.h*self.h
cir=Circle(5)
rec=Rectangle(4,9)
print("area of the circle is ",cir.area())
print("area of the retangle is",rec.area())   '''



'''   from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def sound(self):
        pass
class Tesla(Car):
    def engine(self):
        print("tesla is starting")
    def sound(self):
        print("sound is rouring")
class BMW(Car):
    def engine(self):
        print ("BMW is starting")
    def sound(self):
        print ("sound is roming")
tea=Tesla()
bmv=BMW()
tea.engine()
tea.sound()
bmv.engine()
bmv.sound()

class Car():
    def __init__(self,sound):
        self.sound=sound
    def model(self):
        return("{self.sound},sounding")
t=Car("roaring")
t.model()   '''


#abstraction

'''class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
acc=Bank(511)
print(acc.deposite(500))
print(acc.get_balance()) '''


'''from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def colour(self):
        pass
class Tesla(Car):
    def sound(self):
        return " tesla if awesome"
    def colour(self):
        return "tesla is in red  colour"
t=Tesla()
print(t.sound())
print(t.colour())'''


#class abstract method 
"""from abc import ABC,abstractmethod 
class Bank():
    @abstractmethod 
    def Car(self):
        pass
    @abstractmethod
    def engine(self):
        pass
class Benz(Bank):
    def engine(self):
        print("benz is starting ")
    def Car(self):
        print("benz is luxury car ")
t=Benz()
t.Car()
t.engine()"""




# polymorphism means many forms it allows the same method or 
# operator to behave differently for different objects 

"""class Dog() :
    def sound (self):
        print("dog barks ")
class Animal():
    def sound (self):
        print("animal makes sound ")
ani=Animal()
ani.sound()
dog=Dog()
dog.sound()"""


