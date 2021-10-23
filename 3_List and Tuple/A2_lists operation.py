# LIST OPERATION : Replace, Insert , Sort , Delete , Append , Reverse

# Replace:
list1 = [10,20,3,40,50]
list1[2] = 30
print(list1)

# Insert:
list2 = [10,20,40,50]
list2.insert(2,30)      # 2 represent index of list, 30 represents values
print(list2)

# Sort: (if the list contains similar data types , then sort operation can be used.)
animals = ['monkey','zebra','lion','cat']
list3 = [10,50,40,30,20]
animals.sort()      #sorts in alhpabetical order
list3.sort()  #sorts in ascending order
print(animals)
print(list3)

# Delete operation:
del list3[4]
print(list3)

# Append operation: (inserts at the end of list)
animals.append('donkey')
print(animals)

# Reverse operation:
animals.reverse()
print(animals)