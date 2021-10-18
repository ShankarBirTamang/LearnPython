# MERGE SORT ALGORITHM
# If size of list is greater than 1
    # 1.Divide the list into two sublists of size nearly equal as possible 
    # 2.Recursively split the sublist separately.
    # 3.Merge the two unsorted sublists into a single sorted list recursively

def mergeSort(list1):
    if len(list1)>1 :
        # divided the list into two equal half until 1 elements remains in the list
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        # recursively splitted the sublists into half
        mergeSort(left_list)
        mergeSort(right_list)

        # compare the two unsorted list and merge them by sorting in list1
        i = 0
        j = 0
        k = 0
        while len(left_list)>i and len(right_list)>j:
            if left_list[i]<right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1
        
        # merge the leftout elements in the sorted list
        while len(left_list) > i :
            list1[k] = left_list[i]
            i += 1
            k += 1
        while len(right_list) > j :
            list1[k] = right_list[j]
            j += 1
            k += 1

# input from user
num = int(input("Enter the number of elements in the list: "))
mlist = [int(input()) for i in range(num)]

print("Unsorted list: ",mlist)
mergeSort(mlist)
print("Sorted list: ", mlist)