import random


ch=1

while (ch==1):
    c=random.randint(0,101)
    g=False
    while (g==False):
        u=int(input("Enter your guess of no. (The no. is between 0 to 100): "))
    
        if(u==c):
            print("Your guess is right! You win!")
            g=True
        elif(u<c):
            print("Your guess is wrong!")
            print("Hint: Your guess is less than the actual no.")
            continue
        elif(u>c):
            print("Your guess is wrong!")
            print("Hint: Your guess is more than the actual no.")
            continue
        else:
            print("You have enetredd a wrong input format!")
            break
    ch=int(input("Do you want to play more?(Y=1/N=0): "))
print("Thank You!")