#String Methods

#capitalize() - Converts the first character to upper case
"""
txt = "hello, I am Suhas!"

x = txt.capitalize()
print(x)
"""

#casefold() - Converts string into lower case
"""
txt = "THIS IS SUHAS!"
x = txt.casefold()
print(x)
"""

#center() - Returns a centered string
"""
txt  = "I am Suhas!"

x = txt.center(50)
print(x)
"""

#count() - Returns the number of times a specified value occurs in a string
"""
txt = "I love mangoes!, mangoes are my favorite fruit!"

x = txt.count("mangoes")
print(x)
"""

#encode() - Returns an encoded version of the string
"""
txt = "my name is suhas"

x = txt.encode()
print(x)
"""

#endswith() - Returns true if the string ends with the specified value
"""
txt = "hello, welcome all. I am Suhas!"

x = txt.endswith("!")
print(x)
"""

#expandtabs() - Sets the tab size of the string
"""
txt = "s\tu\th\ta\ts"

c = txt.expandtabs(9)
print(c)
"""

#find() - Searches the string for a specified value and returns the position of where it was found
"""
txt = "Yo, this is suhas here today!"

z = txt.find("t")
    #string.find(value, start, end)
x = txt.find("s", 0, -1)
print(x)
print(z)
"""

#format() - Formats specified values in a string
"""
txt = "For only {price:.2f} pounds!"

print(txt.format(price = 50))
"""

#index() - Searches the string for a specified value and returns the position of where it was found
"""
txt = "Yo, this is suhas here today!"

s = txt.index("suhas")
print(s)
"""

#isalnum() - Returns True if all characters in the string are alphanumeric
"""
txt = "Suhas1998"

t = txt.isalnum()
print(t)
"""

#isalpha() - Returns True if all characters in the string are in the alphabet
"""
txt = "CompanyZ"

z = txt.isalpha()
print(z)
"""

#isascii - Returns True if all characters in the string are ascii characters
"""
t = "suhas1998"

x = t.isascii()
print(x)
"""

#isdecimal() - Returns True if all characters in the string are decimals
"""
t = "\u0030"

print(t.isdecimal())
"""

#isdigit() - Returns True if all characters in the string are digits
"""
txt = "50019998"

print(txt.isdigit())
"""

#isidentifier - Returns True if the string is an identifier
"""
t = "demo"
y = "4suhas"

x = t.isidentifier()
print(x)
print(y.isidentifier()) #it cannot start with a number or underscore to be considered as identifier
"""
#islower() - Returns True if all characters in the string are lower case
"""
t = "THIS is suhas"

x = t.islower()
print(x)
"""

#isnumeric() - Returns True if all characters in the string are numeric
"""
x = '8933984115'

t = x.isnumeric()
print(t)
"""

#isprintable = Returns True if all characters in the string are printable
"""
t = "what's up? This is suhas #1998"

x = t.isprintable()
print(x)
"""

#isspace - Returns True if all characters in the string are whitespaces
"""
txt = "hey, i am just checking out all of the methods in strings!"
t = "  "

t = t.isspace()
z = txt.isspace()
print(z)
print(t)
"""

#istitle - Returns True if the string follows the rules of a title
"""
txt = "SUHAS, you are going to rule This WORLD!"

x = txt.istitle()
print(x)
"""

#isupper() - Returns True if all characters in the string are upper case
"""
txt = "SUHAS BE STRONG, YOU'VE GOT THIS."

print(txt.isupper())
"""

#join() - Converts the elements of an iterable into a string
"""
myTuple=('suhas','rash','nichi')

x = '#'.join(myTuple)
print(x)
"""

#ljust() - Returns a left justified version of the string
"""
txt = 'banana'
t = 'mango'

x = txt.ljust(30, 'a')
y = t.ljust(15)
print(x)
print(y)
"""

#lower() - Converts a string into lower case
"""
t = "Just TrYiNg To GeT iNto LoWer"

print(t.lower())
"""

#lstrip() - Returns a left trim version of the string
"""
txt = "        mango        "

x = txt.lstrip()

print("THis is my", x , "love")
"""

#maketrans() - Returns a translation table to be used in translations
"""
txt = "suhas"
mytable = txt.maketrans("s","c")
print(txt.translate(mytable))
"""

#partition - Returns a tuple where the string is parted into three parts
"""
txt = "Today is the longest day i have been awake to complete my work."

t = txt.partition("have")

print(t)
"""

#replace - Returns a string where a specified value is replaced with a specified value
"""
txt = "I love banana"

x = txt.replace("banana", "mango")
print(x)
"""

#rfind() - Searches the string for a specified value and returns the last position of where it was found
"""
txt = ("Mi casa, su casa")

x = txt.rfind("c")
print(x)
"""

#rindex() - Searches the string for a specified value and returns the last position of where it was found
"""
txt = "Hello world, We are trying to achieve rindex here." 

x = txt.rindex("e", 1, 17)

print(x)
"""

#rjust() - Returns a right justified version of the string
"""
txt = "mango"
x = txt.rjust(10)
print(x, "fruit")
"""

#rpartition - Returns a tuple where the string is parted into three parts
"""
txt = "I like python, python is my favorite programming language"
x= txt.partition("python")
print(x)
"""

#rsptrip() - Returns a right trim version of the string
"""
txt = "abc.py"
x = txt.rstrip('.py')
print(x)
"""

#rsplit - Splits the string at the specified separator, and returns a list
"""
txt = ("apple, banana, mango")
x = txt.rsplit(",")
print(x)
"""

#split() - Splits the string at the specified separator, and returns a list
"""
txt = input("enter the string: ")
x = txt.split(".")
print(x)
"""

#splitlines - Splits the string at line breaks and returns a list
"""
txt = "I am writin to check if the split line works\n I should be in the next line"
x = txt.splitlines()
print(x)
"""

#straswith() - Returns true if the string starts with the specified value
"""
txt = "Hi, welcome all. This is hello world program"
z = txt.startswith(("hello"))
y = txt.startswith("Hi")
print(y)
print(z)
"""

#strip - Returns a trimmed version of the string
""""
t = "hello.py"
x = t.strip(".py")
print(x)
"""

#swapcase - Swaps cases, lower case becomes upper case and vice versa
"""
txt = "I aM cHEcKiNg ThE SwAp CaSe, LOWER, higher"
x = txt.swapcase()
print(x)
"""

#title() - Converts the first character of each word to upper case
""""
t = "hello and welcome everbody to this page"
print(t.title())
"""

#translate _ Returns a translated string
"""
myDict = {83: 80}
txt = "hi, suhas"
print(txt.translate(myDict))
mytable = txt.maketrans("s", "e")
print(txt.translate(mytable))
"""

#upper - Converts a string into upper case
"""
txt = 'i am trying to capitalize'
print(txt.upper())
"""

#zfill() - Fills the string with a specified number of 0 values at the beginning
"""
txt = "hello"
print(txt.zfill(10))
"""































































