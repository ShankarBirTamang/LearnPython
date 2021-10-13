# This program takes a number and checks whether it is a palindrome or not.

# Solution:
# 1. Take the value of integer and store in a variable.
# 2. Transfer the value of integer into another temp variable.
# 3. Using a while loop get each digit of the number and store the reversed no in another variable.
# 4. Check if the reverse of number is equal to the one in temp variable.
# 5. Print the final result.
# 6. Exit

num = int(input("Enter a number: "))
temp = num
rev = 0 
while(num>0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10         # // ==> floor division - division that results into whole no adjusted to the left in number line

if (temp == rev):
    print(" The number is palindrome.")
    print("reverse no = ",rev)
else:
    print("The number is not palindrome.")
    print("reverse no = ",rev)
