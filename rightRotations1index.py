arr=list(map(int,input().split()))
k = int(input())
def swap(arr,start,end):
    n=len(arr)
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
swap(arr,0,len(arr)-k-1)
swap(arr,len(arr)-k,len(arr)-1)
swap(arr,0,len(arr)-1)
print(arr)

