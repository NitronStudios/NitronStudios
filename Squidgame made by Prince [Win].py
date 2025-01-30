import random
import os
import time

os.system('cls')

print("Welcome to Squid Games!\nPress Enter to start.")
input()
os.system('cls')

while(True):
    print("Choose the diffculty.\n\n[1] Easy\n[2] Medium\n[3] Hard\n[4] Expert\n\nEnter the number number before the difficulty to choose.")
    choice = int(input("->"))
    os.system('cls')
    
    if choice>=1 and choice<=4:
        break
    
    else:
        print(f"Are you dumb?? Dude you literlly selected {choice}.\nTry again!")
        input("\nPress Enter to continue!\n")
        os.system('cls')

number1=1

if choice==1:
    number2=10
elif choice==2:
    number2=50
elif choice==3:
    number2=100
else:
    number2=1000

chance= 5 
guess=random.randint(number1,number2)
print(f"Director have chosen number between {number1} and {number2}.\nGuess the number.")
while(chance>=1):
    
    userinput= int(input("->"))
    os.system('cls')
    won=False

    if userinput==guess:        
        os.system('cls')
        won=True
        break

    elif userinput>guess:
        print(f"Your guess was {userinput}. Which guess greater the chosen number by Director.\nTry Again\n\nYour lives left:{chance}.")
    
    else:
        print(f"Your guess was {userinput}. Which guess lesser the chosen number by Director.\nTry Again\n\nYour lives left:{chance}.")

    chance=chance-1


if won:
    print(f"Congrates Your guess was {userinput} which is correct.\nYou Won!!\n\nMade by Prince!")
    input()
else:
    os.system('cls')
    print("You lost!\nNow Die")
    time.sleep(4)
    os.system("shutdown /s /t 1") 