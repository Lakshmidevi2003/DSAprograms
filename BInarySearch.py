arr=list(map(int,input().split()))
num=int(input())
n= len(arr)
def binarysearch(arr,num):
    start=0
    end=n-1
    mid=0
    while(start<=end):
        mid = (start + end) // 2
        midnum=arr[mid]
        if(midnum==num):
            return mid
        if mid<num:
            start=mid+1
        else:
            end=mid-1
    return -1
index=binarysearch(arr,num)
print(index)

