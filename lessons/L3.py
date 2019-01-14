#The third lesson from PYTeach will be about Data Structures

#lists
list1 = [0, 1, 2, 3, 4, 5]
print(list1)

#List Comprehensions
#Lets say you want to fill a list from numbers 0 to 99 you would not
# want to type that in digit by digit so you use list Comprehensions
list2 = [i for i in range(0, 100)]
print(list2)

#Tuples
#Once declared cannot be changed (Immuatable)
tups1 = ("Hello", "World")
print(tups1)

#Sets
set_example = {"rose", "daisy", "iris"}
#Unique thing about sets is that they can only have unique values
list_repeat = [0, 0, 1, 1, 2, 2, 3, 3]
#Lets say we want all the unique values from list_repeat
#Todo that we convert it to a set
set1 = set(list_repeat)

#Dictionaries
dict1 = {'FirstName': 'John', 'LastName': 'Smith', 'Grade': 12}
