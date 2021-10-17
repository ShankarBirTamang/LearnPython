# SELECTION SORT ALGORITHM
# This algorithm divides the list into 2 small lists. One represent sorted elements. The other list contains unsorted elements.
# The selection sort find the smallest or highest values in each iteration and moves those values to the ordered list.

def selectionSort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if(list[j]<list[min]):
                min = j
        # Swapping
        current_element = list[i]
        list[i]=list[min]
        list[min] = current_element
        print("Iteration ",i," : ",list)

num = int(input("Enter the no of items in the list: "))
mlist= [int(input()) for i in range(num)]

print("Unsorted list: ",mlist)
selectionSort(mlist)
print("Sorted list: ",mlist)
