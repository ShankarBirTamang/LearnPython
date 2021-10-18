# BUBBLE SORT ALGORITHM
# Basic Idea: Pass through the list sequentially several times. At each pass , each element in the list is compared to its successor and they are
# interchanged if they are not in proper order.

# Steps:
# 1.Starting with the first element compare the current element with the next element of the list.
# 2.If the current element is greater than the next element of the list swap them.
# 3.If the current element is less than the next element , move to the next element. Repeat step 1.


def bubbleSort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-j-1):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
        #         print("A: ",list1)
        #     else:
        #         print("B: ",list1)
        # print()

num = int(input("Enter the number of elements in the list: "))
mlist = [ int(input()) for i in range(num)]
print("Unsorted list: ",mlist)
bubbleSort(mlist)
print("Sorted list: ",mlist)