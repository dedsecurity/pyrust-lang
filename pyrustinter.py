import math
import os

print("Pyrust 1.0.0 (April 1 2021, 15:36:02)")

pi = ""
cls = ""
hello = ""

while True:
    def printf(msg):
        print(msg);
        
    i = input("\033[32mpyrust> \033[m")
    y = eval(i)

    if i == "pi":
        print(math.pi)
    elif i == "exit":
        break
    elif i == "cls":
        os.system("cls")
    elif i == "hello":
        print("Hello World!")
    elif i == "print":
        print("<built-in function printf>")



