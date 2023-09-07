arr=list(map(int,input().split()))
n=len(arr)
dict={}
a=n/3
for i in range(n):
    if arr[i] in dict:
        dict[arr[i]]+=1
    else:
        dict[arr[i]]=1

for i in range(len(dict)):
    if(dict[arr[i]]>n/3):
        print(arr[i])
