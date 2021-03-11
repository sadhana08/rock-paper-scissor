#Rock paper scissor

import random 

def game():
    # r>s;s>p;p>r
    player = input("Enter your choice 'r' for rock, 's' for scissors,'p' for paper: ")

    comp = random.choice(['r','p','s'])
    print("Choice made by computer: ",comp)

    if player == comp :
        return "Hey it's a tie!"

    if  (player=='r' and  comp == 's') or (player == 's' and comp == 'p') or (player == 'p'and comp == 'r'):
        return "You won!"

    else:
        return "Sorry you lost!"

print(game()) 
