# QUICK SORT ALGORITHM
# It is the fastest known algorithm .Also known as Partition Exchange Sort. Faster than Heap sort and merge sort.

# Algorithm's steps  :
# 1.Select the pivot element.
# 2.Find out the correct position of pivot element in the list by rearranging it.
# 3.Divide the list based on pivot element.
# 4.Sort the sublist recursively.

# condition to find the place of pivot element: 
# 1. left<= right
# 2. a[left] <= pivot , then increment left by 1 
# 3. a[right] >= pivot , then decrement right by 1
# 4. if above condition fails and right > left swap left and right value
# 5. If right < left , then swap pivot and right value of the list

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