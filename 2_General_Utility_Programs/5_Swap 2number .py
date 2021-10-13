a = int(input("Enter value of first variable(a): "))
b = int(input("Enter value of second variable(b): "))

# without 3rd variable
a = a + b
b = a - b
a = a - b
print("a : ",a,"\t b : ",b)

# with 3rd variable
temp = a
a = b
b = temp
print("a : ",a,"\t b : ",b)