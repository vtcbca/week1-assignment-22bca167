#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
def palindrome(n):
    n=int(n)
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==temp:
        print("Enter number is palindrome.")
    else:
        print("Enter number is not palindrome.")

n=input("Enter any number:")
if (n.isnumeric()):
    palindrome(n)
else:
    print("The given value is invalid.")