import os
newfile=open("Edureka_Py.txt","w+")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python:")


for i in range(1,10):
    print(newfile.read())

newfile.seek(5)
print(newfile.tell())
os.rename("Edureka_Py.txt","Python1.txt")
os.remove("Python1.txt")

newfile.close()

