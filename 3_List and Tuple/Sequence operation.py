# SEQUENCE OPERATION: length , select , slice , count , index , membership , concatenation , max value ,   min value , sum

name = "sankar"
list1 = [1,2,3,4.5,[3,8,9]]
tuple1 = (10,20,30,40)

# # length operation
# print(len(name))
# print(len(list1))
# print(len(tuple1))
# print()

# # select operation
# print(name[0])
# print(list1[1])
# print(list1[-1][-1])
# print(tuple1[-2])
# print()

# # slice operation   [starting index : after last index : number of increment or decrement]
# print(name[1:4])
# print(list1[3:])
# print(list1[:3])
# print(list1[:])
# print(name[::2])
# print(name[::-2])
# print(name[::-1])
# print(tuple1[1:])

# count operation
# print(name.count('a'))
# print(list1.count(3))

# index operation
# print(name.index('S'))
# print(name.index('a'))
# print(name.index('r'))
# print(list1.index(2))
# print(tuple1.index(30))

# # membership operation
# print('a' in name)
# print('a' not in name)
# print(10 in tuple1)

# # concatenation 
# s = " Tamang"
# print(name+s)
# list2 = ['hello',5]
# print(list1+list2)
# tuple2 = (50,60)
# print(tuple1+tuple2)
# list and tuple cannot be concatenated

# # maximum value : (only for similar data type)
# print(max(name))
# # print(max(list1)) #error due to different data types
# print(max(tuple1))

# # minimum value:
# print(min(name))
# print(min(tuple1))

# sum
# print(sum(name))  #error as sum operation cant be performed on string
print(sum(tuple1))
print(sum(list1))