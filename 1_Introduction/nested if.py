n = int(input("Enter a number:"))

if n>10:
	print("Number is greater than 10.")
	if n%2==0:
		print("Number is Even.")
	else:
		print("Number is Odd.")
else:
	print("Number is smaller than or equal to 10.")