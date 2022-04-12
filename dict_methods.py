#Dictionary Methods

#clear() -  Removes all the elements from the dictionary
"""
car = {"brand": "Benz", "Model" : "GLS"}

car.clear()

print(car)
"""

#copy - Returns a copy of the dictionary
"""
car = {"brand": "Benz", "Model" : "GLS"}

y = car.copy()

print(y)
"""

#fromkeys() - Returns a dictionary with the specified keys and value
"""
#creating an empty dict set with no values assigned to it
x = ('car', 'bike', 'train')
y = 0   

thisdict = dict.fromkeys(x,y)   #assigns 0 as a value to all the keys

print(thisdict)
"""

#get() - Returns the value of the specified key
"""
car = {"brand": "Benz", "Model" : "GLS"}

x = car.get("brand")
print(x)
"""

#items() - Returns a list containing a tuple for each key value pair
"""
car = {"brand": "Benz", "Model" : "GLS"}

z = car.items()
print(z)
"""

#keys() - Returns a list containing the dictionary's keys
"""
car = {"brand": "Benz", "Model" : "GLS"}

a = car.keys()
print(a)
"""

#pop() - Removes the element with the specified key
"""
car = {"brand": "Benz", "model" : "GLS"}

car.pop("model")

print(car)
"""

#popitem() - Removes the last inserted key-value pair
"""
car = {"brand": "Benz", "model" : "GLS"}

car["speed"] = "250" #appending the dict

print(car) 

car.popitem()
print(car)
"""

#setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
"""
car = {"brand": "Benz", "model": "GLS"}

b = car.setdefault("model","GLE")
print(b)
"""

#update() - Updates the dictionary with the specified key-value pairs
"""
car = {"brand": "Benz", "model": "GLS"}

car.update({"color":"white"})
print(car)
"""

#values() - Returns a list of all the values in the dictionary
"""
car = {"brand": "Benz", "model": "GLS"}

x = car.values()
print(x)
"""


