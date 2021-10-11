# num = int(input("Enter a number: "))
# count = 0
# for x in range(1,num+1):
#     if(num%x==0):
#         count +=1
# if (count == 2):
#     print("{0} is prime number.".format(num))
# else:
#     print("{0} is not prime number.".format(num))

# #alternative method
# num = int(input("\nEnter a number again: "))
# if num>1:
#     for i in range (2,num):
#         if(num % i == 0):
#             print(num , " is not a prime number.")
#             break
#     else:
#         print(num , " is prime number.")
# else:
#     print(num, " is not prime number.")

# #range of prime number
n1 = int (input( "Enter starting number of range: "))
n2 = int (input("Enter last number of range: "))
count = 0
if n2>n1:   
    for x in range(n1,n2+1):
            count = 0
            for y in range(1,x+1):
                if x%y==0:
                    count+=1
            if(count ==2 ):
                print(x, end = " ")
else:
    print("Invalid range.")