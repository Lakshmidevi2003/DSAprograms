arr=list(map(int,input().split()))
n=len(arr)
num=0
for i in range(n):
    num^=i
for value in arr:
    num^=value
    print(num)