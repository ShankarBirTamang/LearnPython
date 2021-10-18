# QUICK SORT ALGORITHM
# It is the fastest known algorithm .Also known as Partition Exchange Sort. Faster than Heap sort and merge sort.

# Algorithm's steps  :
# 1.select pivot element ==> list[first]
# 2.find the correct positon of pivot element ==> left = first +1 , right = last
    # a.left<=right
    # b. while list[left] < pivot , increment left by 1
    # c. while list[right] > pivot , decrement right by 1
    # d. if left < right , then swap left and right value else break
    # e. if right < left , then swap pivot or first value and right value
# 3.Sort the sublist recursively

# To get the correct position of the pivot elements
def pivot_position(mlist,first , last):
    pivot = mlist[first]
    left = first + 1
    right = last
    while True:
        while left <= right and mlist[left] <= pivot :
            left += 1
        while left <= right and mlist[right] >= pivot :
            right -= 1
        if right < left :
            break
        else: 
            mlist[left],mlist[right] = mlist[right],mlist[left] 
            # print("A: ",mlist)         
    mlist[first],mlist[right] = mlist[right],mlist[first]
    # print("B: ",mlist)
    return right

def quickSort(mlist, first , last):
    # when a list contains single element then first = last ,so stops recursion
    if first < last: 
        p = pivot_position(mlist, first , last)
        # print("position of pivot element : ",p)
        quickSort(mlist, first, p-1)
        quickSort(mlist, p+1 , last)

# main:
num = int(input("Enter the no of elements in the list: "))
list1 = [int(input()) for i in range(num)]
print("Unsorted list: ",list1)
quickSort(list1,0,len(list1)-1)
print("Sorted list: ",list1)