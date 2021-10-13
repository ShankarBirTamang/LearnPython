# Palindrome program to check if the string is palindrome or not

# Solution : Find reverse of string and check if the reverse and original are same or not.

# 1st method to reverse string: using slicing technique
# def isPalindrome(s):
#     return s == s[::-1]

# 2nd method to reverse string : run a loop from start to length/2 and chek 1st char to last char of string and sec to sec last and so on
# def isPalindrome(str):
#     for i in range(0,int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True

# 3rd method to reverse string : using predefined funtion '.join(reversed(string))'
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    else:
        return False

# driver code
s = input("Enter any string or number: ")
ans = isPalindrome(s)

if ans :
    print("Yes, it is palindrome.")
else:
    print("no , it's not palindrome.")