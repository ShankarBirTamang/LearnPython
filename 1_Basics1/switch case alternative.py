myswitch = {
	1: "ONE",
	2: "TWO",
	3: "THREE",
	4: "FOUR",
	5: "FIVE"
}

num = int(input("Enter any no. (1 to 5): "))
print('You enter: ',myswitch.get(num,"Invalid Number"))

