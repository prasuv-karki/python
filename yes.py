import numbers
import random
number=random.randint(1,10)
a=13
tries=5
triesa=0
while a!=14:
    
    guess=int(input("What is your guess? The number can be from 1 to 10."))
    if tries>1:
        b=0
        if b==0:
            tries=tries-1
            b=1
        print("You have",tries,"tries.")
    else:
        print("You have 1 try.")
    if tries==1:
        print("You are out of tries! Good Luck next time")
        break
    if guess==number:
        triesa=triesa+1
        tries=tries-1
        print("Congrats! You guessed the right number in ",tries," tries.")
        a=a+1
    elif guess!=number:
        triesa=triesa+1
        tries=tries-1
        print("Your guess is wrong! Try again")