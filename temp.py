def insertionSort(mlist):
    for i in range(1,len(mlist)):
        current_element = mlist[i]
        posn = i
        print(mlist)
        while (current_element < mlist[posn-1] and posn>0):
            mlist[posn] = mlist[posn-1]
            posn = posn - 1
            print(mlist)
        mlist[posn] = current_element
    
num = int(input("Enter the number of items in the list: "))
myList = [int(input()) for i in range(num)]

insertionSort(myList)
print("sorted list: ",myList)
