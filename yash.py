def check(gmail):
    if "@gmail.com" not in gmail:
        print("Enter valid email !  like :'abc@gmail.com'")
    else:
        print("account created succesfully ")
        return 1

count = 0
while(count == 0):
    Gmail=input("Enter your gmail : ")
    res=check(Gmail)
    if(res==1):
        break
        
        
