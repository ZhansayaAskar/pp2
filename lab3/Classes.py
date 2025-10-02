#1
class Do:
    def __init__(self):
        self.s = ""
        
    def getString(self):
        self.s = input("Enter: ")
    
    def printString(self):
        print(self.s.upper())
        
obj = Do()
obj.getString()
obj.printString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
shape1 = Shape()
print("Shape area:", shape1.area())   

square1 = Square(3)
print("Square area:", square1.area())  
    
    
#3 
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
shape1 = Shape()
print("Shape area:", shape1.area())   

square1 = Square(8)
print("Square area:", square1.area()) 

rect1 = Rectangle(5, 9)
print("Rectangle area:", rect1.area()) 

#4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
p1 = Point(7, 4)
p2 = Point(0, 0)

p1.show()   
p2.show()   

print("Distance:", p1.dist(p2)) 

p1.move(6, 8)
p1.show()   

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Balance = {self.balance}")
        else:
            print(f"Insufficient funds! {self.owner} has only {self.balance}")



acc = Account("Zhansaya", 1000)

acc.deposit(300)    
acc.withdraw(500)   
acc.withdraw(2000)  

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 11, 15, 17, 20]
primes = list(filter(lambda x: is_prime(x), nums))
print("Primes:", primes)  