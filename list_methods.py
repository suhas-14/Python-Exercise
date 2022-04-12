# Implementing list methods

#APPEND - Adds an element at the end of the list
"""
l1 = []
l1.append("orange")
l1.append("mango")
l1.append("banana")

print(l1)
"""

#clear() - Removes all the elements from the list
"""
l1.clear()

print(l1)
"""

#copy() - Returns a copy of the list
"""
l2 = ["apple", "mango", "orange", "banana"]
print(l2)

x = l2.copy()
print(x)
"""

#count() - Returns the number of elements repeated in a list
"""
l3 = ['apple', 'mango', 'orange', 'cherry', 'banana']
x = l3.count("banana")
print(x)
"""

#extend() - Add the elements of a list (or any iterable), to the end of the current list
"""
l4 = ['apple', 'mango', 'orange', 'cherry', 'banana']
l5 = ['car', 'bike', 'train']

l4.extend(l5)

print(l4)
"""

#index() - Returns the index of the first element with the specified value
"""
l6 = ['apple', 'mango', 'orange', 'cherry', 'banana']

x = l6.index("mango")

print(x)
"""

#insert() - Adds an element at the specified position
"""
l7 = ['apple', 'mango', 'orange', 'cherry', 'banana']

l7.insert(3, "pineapple")
print(l7)
"""

#pop() - Removes the element at the specified position
"""
l8 = ['apple', 'mango', 'orange', 'cherry', 'banana']

l8.pop(3)

print(l8)
"""

#remove() - Removes the first item with the specified value
"""
l9 = ['apple', 'mango', 'orange', 'cherry', 'banana']

l9.remove("orange")

print(l9)
"""

#reverse() - Reverses the order of the list
"""
l10 = ['apple', 'mango', 'orange', 'cherry', 'banana']

l10.reverse()

print(l10)
"""

#sort() - Sorts the list
"""
l11 = ['apple', 'mango', 'orange', 'cherry', 'banana']

l11.sort()  #asc order 'default'

l11.sort(reverse=True) #desc order

print(l11)
"""






