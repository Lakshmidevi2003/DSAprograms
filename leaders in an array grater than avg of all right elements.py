arr=list(map(int,input().split()))
n=len(arr)
max=n-1
leaders=[]
leaders.append(arr[n-1])
for i in range(n-2,-1,-1):
    if(arr[i]>max):
        leaders.append(arr[i])
        max=(max+(max-1))/2
leaders.reverse()
print(*leaders)

