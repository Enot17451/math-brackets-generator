from random import *

def getNumber():
    return str(randint(1,20))

def getNumberSign():
    s = choice(["+","-","+","-","+","-","+","-","+","-","+","-"])
    if s == "+":
        return ""
    else:
        return "-"

def getSign():
    return choice(["+","-","+","-","+","-","+","-","+","-","+","-"])

def getLetter():
    if randint(1,100) > 50:
        return choice(["x","y","a","b","k","m","n","z","c","x","y","a","b","k","m","n","z","c"])
    else:
        return ""

n = 20
for x in range(n):
    q = f"{getNumberSign()}{getNumber()} {getSign()} ({getNumberSign()}{getNumber()}{getLetter()} {getSign()} {getNumber()}{getLetter()})"
    print(q)
