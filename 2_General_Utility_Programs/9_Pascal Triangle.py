# Pascal's triangle is a triangular array of numbers in which the values at the end of 
# the rows are 1 and each of the others is the sum of the nearest two numbers in the row
# above. 
#             1
#         1       1
#     1       2       1
# 1       3       3       1

#1st method : using factorial function [x!/(y!*(x-y)!)] , x rows , y column
# def facto(n):
#     f = 1
#     i = 1
#     while (i<=n):
#         f = f * i
#         i += 1
#     return f

# nLines = int (input("Enter the no of lines of pascal triangle: "))
# for x in range(nLines):
#     print(" "*(n-i),end=" ")
#     for y in range(x+1):
#         print(facto(x)//(facto(y)*facto(x-y)),end=" ")    #nCr = n! / ((n-r)!*r!)
#     print()
# ********************************************************************************

#2nd method: 
# 1.Get an input value from user
# 2.Using for loop which ranges from 0 to n-1, append the sublist into list
# 3.Then append 1 into sublists
# 4.Then use a for loop to determine the value of the number inside the triangle.
# 5.Print Pascals triangle according to format
# 6.Exit

n = int(input("Enter the number: "))
a = [] # an empty list 
for i in range(n):
    a.append([])
    a[i].append(1)
    for  j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(i+1):
        print(a[i][j] , end = " ")
    print()
# print(a)


# 3rd Method: Most optimized approach based on power of 11
# 11**0 = 1
# 11**1 = 11
# 11**2 = 121
# 11**3 = 1331

# input n
# n = 5

# # iterarte upto n
# for i in range(n):
# 	# adjust space
# 	print(' '*(n-i), end='')

# 	# compute power of 11
# 	print(' '.join(map(str, str(11**i))))
