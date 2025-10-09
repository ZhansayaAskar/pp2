#1
print ("1 ex")
import math
s=float(input("enter degree:"))
print(math.radians(s))
#2
print ("2 ex")
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) / 2) * height
print(area)

#3
print ("3 ex")


n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area:.0f}")

#4
print ("4 ex")
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print(f"Area: {area:.1f}")


