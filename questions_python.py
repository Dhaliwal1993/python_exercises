# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:24:15 2019

@author: acer
"""
#question 1
num = int(input("enter a number: "))
for i in range(2, num):
	if num % i  == 0:
		print(num,"is not prime number")
		break
else:
	print(num," is a prime number")

#question 2
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num,"is Even Number")
else:
   print(num,"is Odd Number")

#question 3
string=input("Enter any string:")
if(string==string[::-1]):
      print("The string "+string+" is a palindrome")
else:
      print("The string "+string+" is not a palindrome")

#question 4
gadgets = ["Python", "Java", 100, "Php", 310.28, "C#", 27.00,"Asp", 1000, "R", "Django"]
str_list=[]
num_list=[]
for i in gadgets:
    if type(i)==str:
        str_list.append(i)
    elif type(i)==int or type(i)==float:
        num_list.append(i)
print("List with String is: ",str_list)                                
print("List with Numbers is: ",num_list)                                 
print("List with Sorted String is: ",sorted(str_list))                                  
print("List with Reversed Sorted String is: ",sorted(str_list,reverse=True))            
print("List with Sorted Numbers is: ",sorted(num_list))                         
print("List with Reversed Sorted Numbers is: ",sorted(num_list,reverse=True))            
#question 5
n=int(input("Enter the size of list:"))
num_list=[]
for i in range(n):
    x=int(input())
    num_list.append(x)
a=(sorted(num_list,reverse=True)) 
print("Sorted list is:",a)
print("Highest Number is: ",a[0])
print("Second Highest Number is: ",a[1])
#question 6
products = {
                "SMART WATCH": 550,
                "PHONE" : 1000,
                "PLAYSTATION": 500,
                "LAPTOP" : 1550,
                "MUSIC PLAYER" : 600,
                "TABLET" : 400
            }
price=int(input("Enter the price:"))
dict1={}
for i in products:
    if products[i]<=price:
        dict1[i]=products[i]
print(dict1)
#question 7
num=int(input("Enter the number:"))
if num % 3 == 0 and num % 5 == 0:
    print("Fizzbuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)      
#question 8
speed=int(input("Enter the Speed:"))
demerit_point=0
if(speed<70):
    print("OK")
elif(speed>70):
    demerit_point=demerit_point+1
    print(demerit_point)
    for i in demerit_point:
        if(speed>70):
            i=i+1
        print(i)
if(i>12):
    print("Suspended")
#question 9
values = input("Input some comma separated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
#question 10
my_str = input("Enter Strings: ")
words = my_str.split()
words.sort()
print("Sorted Strings:")
for word in words:
   print(word)
#question 11
s = input("Enter any sentence")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("No of Letters are: ", l)
print("No of Digits are: ", d)
#question 13
import re
password=input("Enter the password")
#x=re.findall("[a-zA-Z0-9$#@]",password)
if(re.findall("[a-zA-Z0-9$#@]",password) and (len(password)<12 and len(password)>6)):
    print(password)
else:
    print("Invalid password")
    