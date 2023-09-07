s=input()
n=len(s)
x=0
for i in range(n):
    if(s[i]!=s[n-i-1]):
        x=i
if(x==0):
    print("string is palindrome")
else:
     print("string is not palindrome")