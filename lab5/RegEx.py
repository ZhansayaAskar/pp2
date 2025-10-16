
#1

import re

txt = input("")
x = re.search("ab*", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
#2

txt = input("")
x = re.search("ab{2,3}", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
#3
txt = input("")
x = re.findall("[a-z]+_[a-z]+", txt)

print(x)

#4
txt = input("")
x = re.findall("[A-Z][a-z]+", txt)

print(x)

#5
txt = input("")
x = re.findall("^a.*b$", txt)

print(x)

#6
txt = input("Enter text: ")
x = re.sub(r"[ ,.]", ":", txt)
print(x)

#7
txt = input("Enter text: ")
x = re.split("_", txt)
camel = x[0] + ''.join(word.title() for word in x[1:])
print(camel)

#8
txt = input("Enter text: ")
x = re.findall(r'[A-Z][a-z]*', txt)
print(x)

#9

txt = input("Enter text: ")
x = re.sub(r'([A-Z])', r' \1', txt).strip()
print(x)

#10

txt = input("Enter camelCase text: ")
x = re.sub(r'([A-Z])', r'_\1', txt).lower()
print(x)
