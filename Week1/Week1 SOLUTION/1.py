#input number from user to check it's prime or not
i=int(input("Enter a Any Number:"))
prime=True
for n in range(2,i):
    if i%n==0:
        prime=False
if prime:
    print("{} it's Prime Number.".format(i))
else:
    print("{} it's not Prime Number.".format(i))
