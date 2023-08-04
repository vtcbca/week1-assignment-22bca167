#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not armstrong.
def armstrong(n):
    n=int(n)
    temp=n
    arm=0
    l=len(str(n))
    while n>0:
        r=n%10
        arm=arm+(r**l)
        n=n//10
    if temp==arm:
        print("Enter number is armstrong.")
    else:
        print("Enter number is not armstrong.")

n=input("Enter any number:")
if (n.isnumeric()):
    armstrong(n)
else:
    print("The given value is invalid.")