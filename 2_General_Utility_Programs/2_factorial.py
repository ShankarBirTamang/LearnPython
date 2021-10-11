def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
num= int(input("Enter a number: "))
if num < 0:
    print("Factorial cannot be found for negative number.")
elif num == 0:
    print("Factorial of 0 is 0.")
else:
    print("Factorial of ",num," is ",factorial(num))