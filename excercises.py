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
#Write a program that accepts a comma seperated sequence of words as input and prints the words in a comma-seperated sequence after sorting.

input_str = input()
items = [x for x in input_str.split(',')]
items.sort()
print(','.join(items))

Question 9:
#Write a program that accepts sequence of lines as input and prints the lines after making all the characters in the sentence capitalized.

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for each_line in lines:
    print(each_line)


Question 10:
#Write a program that accepts a sequence of whitespace seperated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

input_str = input()
words = [word for word in input_str.split(' ')]
print(' '.join(sorted(list(set(words)))))

Question 11:
#Write a program which accepts a comma seperated sequence of 4-digit binary numbers as its input and then check whether they are divisible by 5 or not printed in a comma-seperated sequence.

ans = []
input_str = input()
items = [x for x in input_str.split(',')]
for i in items:
    dec = int(i,2)
    if dec % 5 == 0:
        ans.append(i)

print(','.join(ans))

Question 12:
#Write a program which finds numbers between 1000 and 3000(both included) whose digits are an even number printed in a comma-seperated sequence.

ans = []
for i in range(1000,3001):
    string = str(i)
    check = True
    for j in range(4):
        if int(string[j]) % 2 != 0:
            check = False
            break
    if check == True:
        ans.append(string)
print(','.join(ans))

Question 13:
#Write a program that accepts a sentence and calculates the number of letters and digits.

input_str = input()
dig = 0
let = 0
for it in input_str:
    if it.isdigit():
        dig += 1
    elif it.isalpha():
        let += 1

print("LETTERS: ",let)
print("DIGITS: ",dig)

Question 14:
#Write a program that accepts a sentence nd calculates the number of uppercase and lowercase letters.

input_str = input()
lcase = 0
ucase = 0
for i in input_str:
    if i.isupper():
        ucase += 1
    elif i.islower():
        lcase += 1
print("Lower Case: ",lcase)
print("Upper Case: ",ucase)

Question 15:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as value of a.

a = input()
ans = int('%s' %a) + int('%s%s' %(a,a)) + int('%s%s%s' %(a,a,a)) + int('%s%s%s%s' %(a,a,a,a))
print(ans)

Question 16:
# Use a list comprehension to square each odd numbers in a list.

input_str = input()
values = [ str(int(x)*int(x)) for x in input_str.split(',') if int(x)%2!=0]
print(','.join(values))

Question 17:
# Write a program which computes the net amount of a bank account based on a transaction log from console input. The transaction log format is:
#D 100
#W 200

ans = 0
while True:
    input_str = input()
    if not input_str:
        break
    values = input_str.split(' ')
    operation = values[0]
    amount = int(values[1])
    if operation == 'D':
        ans += amount
    elif operation == 'W':
        ans -= amount
print(ans)

Question 18:
# A website requires a user t input username and password to register.
#Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
# Atleast 1 letter between [a-z] Atleast 1 number between [0-9] Atleast 1 letter between [A-Z] Atleast 1 character from [#$@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma seperated passwords and will check them.Correct passwords are to printed as comma-seperated values.
import re
ans = []
input_str = input()
items = [x for x in input_str.split(',')]
for i in items:
    if len(i) < 6 or len(i) > 12:
        continue
    elif not re.search('[a-z]',i):
        continue
    elif not re.search('[A-Z]',i):
        continue
    elif not re.search('[$#@]',i):
        continue
    else:
        ans.append(i)

print(','.join(ans)) 

Question 19:
#Write a program to sort the (name,age,height) tuples by ascending order where name is string, age and height are numbers.
# The sort criteria is:
# Sort based on name
# Sort based on age
# Sort based on score
#The priority is that name>age>score
from operator import itemgetter, attrgetter
values = []
input_str = input()
while True:
    if not input_str:
        break
    else :
        values.append(tuple(input_str.split(',')))

print(values.sort(key = lambda elem:(elem[0],elem[1],elem[2]))

