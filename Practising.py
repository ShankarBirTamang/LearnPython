# Creating a dictionary getting input from user and returning meaning.

# myDic={"mute":"no speech",
# 	"unmute":"to allow to produce sound",
# 	"mutable":"liable to change",
# 	"immutable":"unliable to change"
# }

# word=input("Enter a word to find the meaning: ")
# if word in myDic:
# 	print("The meaning of ",word,"is",myDic[word],". Thank you !!!\n")
# else:
# 	new = word
# 	print("Sorry , we donot have that word in our dictionary.\n")
# 	ans=input("Do you like to add this word and meaning in our dictionary. \nEnter y for yes and n for no : ")
# 	if ans=="y":
# 		myDic[new]=input("Then please enter its meaning : ")
# 		print("The meaning of ",new,"is",myDic[new],". \nThank you for your contribution.")
# 	else:
# 		print("It's ok !")

# print(myDic)



# list1=[ ["Ram",1], ["Sita",2],["Arjun",3]]
# dict1=dict(list1)
# print(dict1)
# for item,num in list1:
# for item,num in dict1.items():
# 	print(item,"has a number",num)

# for item in dict1:
# 	print(item)

# items=[3,43,"ram","sita",4,45,32,2,int,float]
# for item in items:
# 	if str(item).isnumeric() and item>6:
# 		print(item)

#while loop
#exit the loop when i=4
# i=1
# while i<6:
# 	print(i)
# 	if i==4:
# 		break;
# 	i+=1



#continue to next iteration when i=4
# i=0
# while i<6:
# 	i+=1
# 	if i==4:
# 		continue;
# 	print(i)
	
#Print a message once the condition is false:
# i=1
# while i<6:
# 	print(i)
# 	i+=1
# else:
# 	print("It is no longer less than six.")

 #nested loop
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# def myfunc(fname):
# 	print(fname+" hello")

# myfunc("Ram")
# myfunc("sita")

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# # If the number of keyword arguments is unknown, add a double ** before the parameter name:
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# If we call the function without argument, it uses the default value:
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# # Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# To let a function return a value, use the return statement:
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# def myfunction():
#   pass

# recursion function

# Example 1:
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(7)

# Example 2: factorial of a number
# def factorial(k):
# 	if k==1:
# 		return 1
# 	else:
# 		return (k*factorial(k-1))

# num=int(input("Enter a number to find its factorial: "))
# print("Factorial of",num,"is", factorial(num))


#polymorphism
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

#use of try and except

# num1=input("Enter number 1:\n")
# num2=input("Enter number 2:\n")
# try:
# 	print("The sum of these 2 numbers are:",
# 		int(num1)+int(num2))
# except Exception as e:
# 	print(e)

# print("\nIt is needed.")
def pattern1():
	for i in range(1,6):
		for j in range(1,6):
			print("*",end=" ")
		print()

def pattern2():
	for i in range(1,6):
		for j in range(1,6):
			print(i,end=" ")
		print()


def pattern3():
	for i in range(1,6):
		for j in range(1,6):
			print(j,end=" ")
		print()


def pattern4():
	for i in range(65,70):
		for j in range(1,6):
			print(chr(i),end=" ")
		print()

def pattern5():
	for i in range(1,6):
		for j in range(65,70):
			print(chr(j),end=" ")
		print()

def pattern6():
	for i in range(5,0,-1):
		for j in range(5,0,-1):
			print(i , end=" ")
		print()

def pattern7():
	for i in range(5,0,-1):
		for j in range(5,0,-1):
			print(j,end=" ")
		print()

def pattern8():
	for i in range(69,64,-1):
		for j in range(69,64,-1):
			print(chr(i),end=" ")
		print()

def pattern9():
	for i in range(69,64,-1):
		for j in range(69,64,-1):
			print(chr(j),end=" ")
		print()

def pattern10():
	for i in range(1,6):
		for j in range(1,i+1):
			print("*",end=" ")
		print()

def pattern11():
	for i in range(1,6):
		for j in range(1,i+1):
			print(i,end=" ")
		print()

def pattern12():
	for i in range(1,6):
		for j in range(1,i+1):
			print(j,end=" ")
		print()

def pattern13():
	for i in range(65,70):
		for j in range(65,i+1):
			print(chr(i),end=" ")
		print()

def pattern14():
	for i in range(65,70):
		for j in range(65,i+1):
			print(chr(j),end=" ")
		print()

def pattern15():
	for i in range(1,6):
		for j in range(5,i-1,-1):
			print("*",end=" ")
		print()

def pattern24():
	for i in range(1,6):
		for j in range(5,i,-1):
			print(" " ,end=" ")
		for j in range(0,i):
			print("*",end=" ")
		print()

def pattern24a():
	for i in range(1,6):
		for j in range(5,i,-1):
			print(end=" ")
		for j in range(1,i+1):
			print("*",end=" ")
		print()

def pattern24b():
	for i in range(1,6):
		for j in range(1,6):
			if(j!=5):
				print(" ",end=" ")
			else:
				print("*",end=" ")
		print()

def pattern24c():
	for i in range(1,6):
		for j in range(1,6):
			if(j==3):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()



pattern24()
pattern24()
pattern24b()


pattern24a()
pattern24c()

#pattern1()
#pattern2()
#pattern3()
#pattern4()
#pattern5()
#pattern6()
#pattern7()
#pattern8()
#pattern9()
#pattern10()
