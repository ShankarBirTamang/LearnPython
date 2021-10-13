#fibonacci sequence : 0 1 1 2 3 5 8 13 ....

def fibo(n):
    if (n<=1):
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

nterms = int(input("Enter the no of terms: "))
if (nterms<=0):
    print("Enter postive integer")
else:
    for i in range(nterms):
        print(fibo(i), end=" ")
