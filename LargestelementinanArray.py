arr=list(map(int,input().split()))
n=len(arr)
largest=arr[0]
for i in range(1,n):
    if(arr[i]>largest):
        largest=arr[i]
print(largest)