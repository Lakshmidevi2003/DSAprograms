start=int(input())
stop=int(input())
count=0
while(start<=stop):
    if(start%4==0 and start%100!=0):
        count+=1
    elif(start%400==0):
        count+=1
    start+=1
print(count)
