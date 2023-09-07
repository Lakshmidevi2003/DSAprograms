arr=list(map(int,input().split()))
"""print(arr[: : -1])"""
def swap(arr,start,end):
    n=len(arr)
    l = []
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
swap(arr,0,len(arr)-1)
print(arr)