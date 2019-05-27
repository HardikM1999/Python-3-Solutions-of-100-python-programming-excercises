Question 2:
#Write a program which can compute the factorial of a given number
#The results should be seperated by commas on a single line
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

x = int(input())
print(fact(x))

Question 3:
#With a given integer n,write a program to generate a dictionary that contains (i,i*i) such that is an integer between 1 and n both included and then program should print the dictionary
n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)

Question 4:
#Write a program which accepts a sequence of comma seperated numbers from console and generate a list and a tuple which contains every number.
values = input()
l = values.split(",")
t = tuple(l)
print(l)
print(t)

Question 5:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case 
#Also please use simple test functions to test the class methods


class InputOutputString(object):
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutputString()
strObj.getString()
strObj.printString()

Question 6:
#Write a program that calculates and prints the values according to the given formula:
#Q = square root of [(2*C*D)/H]
#C is 50.H is 30
#D is variable whose values will be given to you in comma-seperated sequence
import math 
c = 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

Question 7:
#Input 2 digits X and Y and generate a 2d array.The element values should be i*j for row as i and column as j.
input_str = input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col

print(multilist)


Question 8:
