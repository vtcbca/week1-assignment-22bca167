#Input Any String For Count The Number Vovel
s=input("Enter A Any String:")
b=0
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='A' or
       s[i]=='e' or s[i]=='E' or
       s[i]=='i' or s[i]=='I' or
       s[i]=='o' or s[i]=='O' or
       s[i]=='u' or s[i]=='U'):
        b=b+1
print("Total Vowel In String Is %s."%b)
