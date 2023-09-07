t=int(input())
for i in range(0, t):
    age = int(input())
    if age<13:
        print("You are young.")
        if age>=13 and age<18:
            print("You are a teenager.")
    else:
        print("You are old.")
        for j in range(0, 3):
            age=age+1
            if age<13:
                print("You are young.")
                if age>=13 and age<18:
                    print("You are a teenager.")
            else:
                print("You are old.")
        
