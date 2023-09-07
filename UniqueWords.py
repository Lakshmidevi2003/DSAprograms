def unique_words(str1, length):
    list1=[]
    list2=[]
    list1=str1.split(" ")
    for i in list1:
        if(list1.count(i)==1):
            list2.append(i)
            list3=[]
    for i in list2:
        if(len(i)>=length):
            list3.append(i)
    print(list3)
str1=input("enter a string:")
length=int(input("enter a length:"))
unique_words(str1, length)
