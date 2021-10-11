while (1):
    print("Enter a number (<=100) to find its square.")
    print("Press 0 to exit: ")
    num = int(input())
    if num == 0: 
        print("Program's End. Thank you!")
        break;
    elif num>100:
        print("Number is greater than 100. Try again!")
        continue;
    print("\nSquare of ",num," is ",num*num)
