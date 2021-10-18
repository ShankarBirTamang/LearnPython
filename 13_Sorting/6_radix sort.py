# RADIX SORT ALGORITHM
# ==> Radix sort is a sorting technique that sorts the elements by first grouping the individual digits of the same place value.
# Then sort the elements according to increasing or decreasing order.
# It is not comparision sort algorithm
# Instead it uses counting sort algorithm


def counting_sort( mlist , P):
    size = len(mlist)
    result = [0]*size
    count = [0]*10
    # getting count value for individual digit
    for i in range(size):
        temp = mlist[i]//P
        count[temp%10]+=1
    print("count: ",count,"\t",P)
    # cumulative count value
    for i in range(1,10):
        count[i]+=count[i-1]
    print("count: ",count,"\t",P)

    i = size -1
    while i>=0:
        temp = mlist[i]//P
        result[count[temp%10]-1] = mlist[i]
        count[temp%10] -= 1
        i = i - 1
        print(result)
    for i in range(size):
        mlist[i] = result[i]
    print()
def radixSort(mlist):
    maximum = max(mlist)
    place = 1 # unit place
    while maximum//place > 0 :
        counting_sort(mlist,place)
        print("A: ",mlist,"\t",place)
        place = place * 10

mlist = list(map(int,input("Enter the elements of the list: ").split()))
print("Unsorted list: ",mlist)
radixSort(mlist)
print("Sorted list: ",mlist)