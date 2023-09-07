n=int(input())
arr=list(map(int,input().split()))
flag= True
for i in range(len(arr)-1):
    if flag is True:
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    else:
        if(arr[i]<arr[i+1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    flag=bool(1-flag)
print(arr)