import random as r
import math as m
import time as t
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i" , "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetDict = []

r.seed(t.time())
def genUniqueNumber(usedNumbers):
    nonuniqueNumbers = usedNumbers
    uniqueNumber = 0 
    while True{
        uniqueNumber = r.randInt(1,26)
        if uniqueNumber !in nonuniqueNumbers
            return uniqueNumber
    }
def generateRandomStartPosition():
    numbersUsed = []
    for i in alphabetList{

        numberKey = genUniqueNumber(numbersUsed)
        numbersUsed.append(numberKey)
        alphabetDict.append(alphabetList[i],) 

    }
