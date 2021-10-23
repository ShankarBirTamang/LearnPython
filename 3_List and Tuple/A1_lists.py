# LISTS : group of different types of elements

# Characteristics:
# 1.Mutable : data can be changed
# 2.Linear Data structure : elements are arranged in linear order
# 3.Mixed Type Elements : elements can be int, float ,string or even list.
# 4.Variable Length
# 5.Zero based indexing

# list of strings
fruit= ['orange','apple','banana','mango']
print(fruit)
print(fruit[0])

# nested list
lists = [[2,4,6,8],[1,3,5,7,9],[2,3,5,7]]
print(lists)
print(lists[0][0])

# list of mixed types
list1 = [1,'car',50.5,[2,'van']]
print(list1)
print(list1[-1])

# taking list from users as an string by default
list2 = list(input("Enter your lists of string: ").split())
print(list2)

# taking list from users after mapping into int
list3 = list(map(int,input("Enter your lists of integer: ").split()))
print(list3)


