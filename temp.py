# 1.select pivot element ==> list[first]
# 2.find the correct positon of pivot element ==> left = first +1 , right = last
    # a.left<=right
    # b. while list[left] < pivot , increment left by 1
    # c. while list[right] > pivot , decrement right by 1
    # d. if left < right , then swap left and right value else break
    # e. if right < left , then swap pivot value and right value
# 3.Sort the sublist recursively

def pivot_location(list, f, l):
    pivot = list[f]
    left = f + 1
    right = l
    while True:
        while left<=right and list[left]<=pivot :
            left +=1
        while left<=right and list[right]>=pivot:
            right-=1
        if left<right:
            list[left],list[right]=list[right],list[left]
        else:
            break
    list[f],list[right]=list[right],list[f]
    return right

def quickSort(list , f , l):
    if f <l:
        p = pivot_location(list , f , l)
        quickSort(list,f,p-1)
        quickSort(list,p+1,l)

mlist = [5 , 4 ,3, 1 ,2 ]
quickSort(mlist,0,len(mlist)-1)
print(mlist)