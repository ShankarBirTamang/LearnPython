# num = input("Enter 0: ")

# if int(num)==0:
# 	print("Zero is Entered")
# else:
# 	print("You enter another number.")

# num = input("Enter any number: ")

# if int(num)<=50:
# 	print("Number is less than or equal to 50.")
# else:
# 	print("Number is greater than 50.")

#if else with OR operator
gen = input("Are you a Male (y/n): ")

if gen == 'y' or gen == 'Y':
	print("Gender:Male")
else:
	print("Gender:Female")

age = int(input("Enter your age: "))

if age>=18 and age<=120:
	print("You are eligible for voting.")
else:
	print("You are not eligible for voting.")