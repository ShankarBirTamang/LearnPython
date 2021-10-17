# INSERTION SORT ALGORITHM

# Basic idea: Sorts a list of record by inserting new element into an existed sorted list
# To insert new item into list:
# 1.Search the position in the sorted sublists from last toward first
# 2.While searching , move elements one position right to make a room to insert a[i]
# 3.Place a[i] in its proper place.

def InsertionSort(my_list):
    for i in range(1,len(my_list)) :
        current_element = my_list[i]
        pos = i
        while (current_element < my_list[pos-1] and pos>0):
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element

num = int(input("Enter the number of items in the list: "))
m_list = [int(input()) for i in range(num)]

InsertionSort(m_list)
print(m_list)