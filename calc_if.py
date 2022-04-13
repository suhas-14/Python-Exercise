#Calculator program using if conditons only.

print("Simple calculator program\n")

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter choice(1-4):  "))

if choice == 1:
    a = int(input("enter the firt num: "))
    b = int(input("enter the second num: "))
    print("Total: ",a+b)

elif choice == 2:
    a = int(input("enter the firt num: "))
    b = int(input("enter the second num: "))
    print("Difference: ",a-b)
    
elif choice == 3:
    a = int(input("enter the firt num: "))
    b = int(input("enter the second num: "))
    print("Product: ",a*b)
    
elif choice == 4:
    a = int(input("enter the firt num: "))
    b = int(input("enter the second num: "))
    print("Quotient: ",a/b)

else:
    print("invalid choice")
    
    