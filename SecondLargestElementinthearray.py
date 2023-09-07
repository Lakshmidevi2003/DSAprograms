arr=list(map(int,input().split()))
n=len(arr)
largest=arr[0]
secondlargest=-1
for i in range(1,n):
    if(arr[i]>largest):
        largest=arr[i]
for i in range(0,n):
    if(arr[i]>secondlargest and arr[i]!=largest):
        secondlargest=arr[i]
print(secondlargest)