import random
number=random.randint(1,10)
a=13
tries=0
while a!=14:
    
    guess=int(input("What is your guess? The number can be from 1 to 10. You have a total of 5 tries    "))
    if tries==4:
        print("You are out of tries! Good Luck next time")
        break
    if guess==number:
        tries=tries+1
        print("Congrats! You guessed the right number in ",tries," tries.")
        a=a+1
    elif guess!=number:
        tries=tries+1
        print("Your guess is wrong! Try again")