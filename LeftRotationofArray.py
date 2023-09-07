arr=list(map(int,input().split()))
k=int(input())
def leftrotation(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
leftrotation(arr,0,k-1)
leftrotation(arr,k,len(arr)-1)
leftrotation(arr,0,len(arr)-1)
print(*arr)
