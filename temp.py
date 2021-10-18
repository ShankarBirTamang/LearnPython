def countingSort(list,place):
    size = len(list)
    result = [0]*size
    count = [0]*10
    for i in range(size):
        temp = list[i]//place
        count[temp%10]+=1
    for i in range(1,10):
        count[i] += count[i-1]

    i=size-1
    while i>= 0:
        temp = list[i]//place
        result[count[temp%10]-1]=list[i]
        count[temp%10] -=1
        i -= 1

    for i in range(size):
        list[i]=result[i]

def radixSort(mlist):
    m = max(mlist)
    place = 1
    while m//place>0:
        countingSort(mlist,place)
        place = place * 10

mlist= list(map(int,input("Enter the number: ").split()))
radixSort(mlist)
print("Sorted list: ",mlist)