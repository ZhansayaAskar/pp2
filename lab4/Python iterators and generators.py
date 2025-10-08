#1 a
n= int (input(" enter number "))
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= n:
      x = self.a ** 2
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
  
# b 
def Squares(n):
    for i in range(1, n + 1):
        yield i ** 2  


N = int(input("enter number: "))


for num in Squares(N):
    print(num)

  
  
#2 a
s= int (input("enter number for  print the even num "))
class EvenNum:
    def __iter__(self):
        self.a=0
        return self
    
    def __next__(self):
        while self.a <=s:
            x= self.a
            self.a +=1
            if x % 2 ==0:
                return x
        raise StopIteration

myclass=EvenNum()
myiter = iter (myclass)

for x in myiter:
    print(x)      
    
 # b     
    
def Evennum(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i  


n = int(input("enter number for  print the even num: "))


print(",".join(str(x) for x in Evennum(n)))

#3 
def Divide(n):
    for i in range (0,n+1):
        if i%3==0 and i%4==0:
            yield i 

n = int(input("enter number : "))

for x in Divide(n):
    print(x)
    
    
#4
def squares(a,b):
    for i in range (a,b+1):
        yield i ** 2

a = int(input("enter a: "))
b= int(input("enter b: "))


for num in squares(a,b):
    print(num)


#5
def down (a):
    for i in range (a,-1,-1):
        yield i 
        
n = int(input("enter a num: "))



for num in down(n):
    print(num)
