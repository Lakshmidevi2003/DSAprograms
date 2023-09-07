n = int(input())
arr = list(map(int, input().split()))
zeros=[]
ones=[]
for i in range(len(arr)):
    if(arr[i]==0):
        zeros.append(arr[i])
    else:
        ones.append(arr[i])
i,j,k=0,0,0
while(i<len(zeros)):
    arr[k]=zeros[i]
    k+=1
    i+=1
while(j<len(ones)):
    arr[k]=ones[j]
    k+=1
    j+=1
print(arr)
