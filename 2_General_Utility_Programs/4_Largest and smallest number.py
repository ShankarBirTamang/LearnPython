a = []
num = int(input("Enter the number of element: "))
for i in range (1,num+1):
    b = int(input("Enter element: "))
    a.append(b)
a.sort()
print("largest element = ",a[num-1])
print("Smallest element = ",a[0])