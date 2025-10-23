import os

#task1
path =  '/Users/zansaa/Documents/pp2/lab6/testpath/'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#task2

path =  '/Users/zansaa/Documents/pp2/lab6/testpath/'

print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#task3

path =  '/Users/zansaa/Documents/pp2/lab6/testpath/ex.txt'

if os.path.exists(path):
    print("Path exists!")
    print("Directory part:", os.path.dirname(path))
    print("File name part:", os.path.basename(path))
else:
    print("Path does not exist")

#task4
path =  '/Users/zansaa/Documents/pp2/lab6/testpath/ex.txt'

if os.path.exists(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
else:
    print(" File does not exist.")
    
#task5


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


path = '/Users/zansaa/Documents/pp2/lab6/testpath/ex.txt'


with open(path, "w") as myfile:
    for c in color:
        myfile.write("%s\n" % c)

with open(path, "r") as content:
    print(content.read())

#task6
import string

folder = '/Users/zansaa/Documents/pp2/lab6/testpath/' 

for letter in string.ascii_uppercase:
    file_path = os.path.join(folder, letter + ".txt")
    with open(file_path, "w") as f:
        f.write(letter)
        
        
#task7

f = open("/Users/zansaa/Documents/pp2/lab6/testpath/ex.txt", "r")
txt = f.read()
f.close()


p = open("/Users/zansaa/Documents/pp2/lab6/testpath/copy.txt", "w")
p.write(txt)
p.close()

#task7

file_path = '/Users/zansaa/Documents/pp2/lab6/testpath/del.txt'


if os.path.exists(file_path):
   
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted successfully!")
    else:
        print("No permission to delete this file.")
else:
    print("File does not exist.")
