from mimetypes import guess_all_extensions
import random
from turtle import back
a=14
tries=0
while a!=15:
    number = 6
    # random.randrange(0,15)
    print("Welcome to this guessing game.")
    guess = int(input("Pick a number between 1 and 15:  "))
    tries= random.randrange(1,2)
    a=a+1

while a!=15:
    def back():
        if tries==1:
            print("The guess was wrong.Try again. You are now at",tries,"try.")
        elif tries==0:
           print("The guess was wrong.Try again. You are now at 1 try.")
        elif guess==number:
            if tries==0:
                # equal
                print("Congrats! You finished the game in 1 try.")
                a=15
            elif tries!=0:
                # not equal
                print("Congrats! You finished the game in",tries,"tries.")
                a=15