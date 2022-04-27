import random
a=0
computer_points=0
player_points=0
while a==0:
    choice=int(input("Type 1 for rock, 2 for paper and 3 for scissors.  "))
    computer=random.randint(0,2)
    if computer==0:
        computer="rock"
    elif computer==1:
        computer="paper"
    elif computer==2:
        computer="scissors"
    print("The computer picked", computer)

    if computer=="scissors" and choice==2:
        print("You win!")
        player_points=player_points+1
    elif computer=="rock" and choice==3:
        print("You win!")
        player_points=player_points+1
    elif computer=="paper" and choice==1:
        print("You win!")
        player_points=player_points+1
    elif computer=="rock" and choice==2:
        print("You lose!")
        computer_points=computer_points+1
    elif computer=="paper" and choice==3:
        print("You lose!")
        computer_points=computer_points+1
    elif computer=="scissors" and choice==1:
        print("You lose!")
        computer_points=computer_points+1
    elif computer=="paper" and choice==2:
        print("Its a tie!")
    elif computer=="rock" and choice==1:
        print("Its a tie!")
    elif computer=="scissors" and choice==3:
        print("Its a tie!")
    b=int(input("If you want to start again and save points type 1. If you want to stop and show the points now, type 2."))
    if b==1:
        a=0
        continue
    elif b==2:
        print("Thanks for playing")
        print("The computer has",computer_points,"points.")
        print("You have",player_points,"points.")
        a=a+1