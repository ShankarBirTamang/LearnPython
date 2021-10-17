# BINARY SEARCH ALGORITHM

# To do the binary search , first we have to sort the list elements
# Logic of binary search:
# 1.First find the middle element of the list
# 2.Compare the middle element with an item.
# 3.There are 3 cases:
#   a.If it is desired elements then search is successful.
#   b.If it is less than desired elements then search only in the first half of the list.
#   c.If it is greater than the desired item, search in the second half of the array.
# 4.Repeat the same steps until an element is found or search area is exhausted.

pos = -1

def search(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l+u)//2
        # If mid is desired elements
        if (list[mid] == n):
           globals()['pos'] = mid
           return True
        # If mid is less than desired element
        elif list[mid] < n :
            l = mid + 1     # skipping mid value
        # If mid is greater than desired element
        else:
            u = mid - 1     # skipping mid value
    return False

def InsertionSort(my_list):
    for i in range(1,len(my_list)) :
        current_element = my_list[i]
        posn = i
        while (current_element < my_list[posn-1] and posn>0):
            my_list[posn] = my_list[posn-1]
            posn = posn - 1
        my_list[posn] = current_element

# input from user
num = int(input("Enter the number of items in the list: "))
m_list = [int(input()) for i in range(num)]

#1st list are sorted
InsertionSort(m_list)
print("Sorted list: ",m_list)

n = int(input("Enter the item to be searched: "))
if search(m_list , n):
    print ("Found at ", pos+1)
else:
    print("Not Found")