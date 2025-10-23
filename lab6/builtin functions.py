#task1 

print("task 1")

from math import prod
list1  = [2, 3, 4, 5]
print(prod(list1))

#task2

print("task 2")
def count_uppercase(text):
    count=0
    
    
    for char in text:
      if (char.isupper()):
       count+=1
     
    return count

def count_lowercase(text):
    sum=0
    
    
    for char in text:
      if (char.islower()):
       sum+=1
     
    return sum


text = input("text: ")

count = count_uppercase(text)
sum = count_lowercase(text)

print("Upper num: ",count)
print("lower num: ",sum)

#task3 
print("task 3")
def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

sentence = input("Enter a sentence: ")
result = is_palindrome(sentence)

if result:
    print(f"'{sentence}' is polidrom")
else:
    print(f"'{sentence}' - not  polidrom")

#task4

print("task 4")
import time
import math

def timee(number, milliseconds):
    print(f"Wait {milliseconds} ...")
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result


number = int(input("Enter number: "))
delay = int(input("Enter delay in milliseconds: "))
result = timee(number, delay)
print(f"Square root of {number} after {delay} miliseconds is {result}")
    
    
#task5

print("task 5")

k=tuple(map(int,input().split()))
tuple1=k
print(all(tuple1)) 