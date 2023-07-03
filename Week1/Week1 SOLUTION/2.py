#Write a python script to enter any number and print the sum of its digit.
a=int(input('Enter Any Number:'))
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a//10
   
print("Sum Of its Digit Is {}.".format(sum))
