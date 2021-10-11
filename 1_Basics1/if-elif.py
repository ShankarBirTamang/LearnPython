marks = int(input("Enter your Marks: "))
if marks<35:
	print("Grade 'F': Fail")
elif marks>=35 and marks <=40:
	print("Grade 'D'")
elif marks>=41 and marks<50:
	print("Grade 'C'")
elif marks>=51 and marks<60:
	print("Grade 'B'")
elif marks>=61 and marks<70:
	print("Grade 'B+'")
elif marks>=71 and marks<80:
	print("Grade 'A'")
else:
	print("Grade 'A+'")