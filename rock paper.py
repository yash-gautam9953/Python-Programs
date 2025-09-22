import random as r
count = 1
while count == 1:
 userChoice=int(input("\nChoose Rock,Paper,Scissor & Exit any one 1,2,3 & 0 Respectivily = "))
 if(userChoice== 0):
    count = 0
    print("\n\n\nThanks for playing This game  .............\n\n\n")
 compChoice=r.randint(1,3)
 a=["a","Rock","Paper","Scissor"]
 def playGame(u,c):
    if(u==c):
        print("\nMatch is Draw !  Because comp choice =",a[c]," & user choice =",a[u])
    elif((u==1 and c==2) or (u==2 and c==3) or (u==3 and c==1)):
        print("\nYou Lose Because comp choice =",a[c]," & user choice =",a[u])
    elif(u > 3):
       print(" \n\n ",u ,"This is not a valid number Please Enter a Valid number ...\n\n")
    else:
        print("\nYou win Because comp choice =",a[c]," & user choice =",a[u])
 playGame(userChoice,compChoice)


