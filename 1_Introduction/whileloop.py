n=0

while n != 1:
	print("You are inside the while loop.")
	while n<=10 :
		print(n)
		n += 1
	print("Press 1 for exit from the while loop.")
	n = int(input())
print("You are out of the while loop.")

#Square of the number using while loop
while n != 0:
	print("Square of ",n, " is ", n*n)
	n = int(input("Enter another number: "))
print("End of Program")