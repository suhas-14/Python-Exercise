# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:33:23 2022

@author: nanis
"""

def add():
    print("total: ",a+b)
    
def substract():
    print("difference: ",a-b)

def multiplication():
    print("product: ",a*b)

def division():
    print("quotient: ",a/b)

def remainder():
    print("modulous: ",a%b)

print("1. Addition")
print("2. Substration")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

choice = int(input("select an option: "))

if choice == 1:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    add()
    
elif choice == 2:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    substract()

elif choice == 3:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    multiplication()

elif choice == 4:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    division()

elif choice == 5:
    a = int(input("enter first num: "))
    b = int(input("enter second num: "))
    remainder()
    
    


    