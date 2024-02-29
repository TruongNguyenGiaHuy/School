def instruction():
    print('''
                *** INSTRUCTION ***
- Users can either choose the number of rounds or they can opt for infinite mode.

- If users press the exit code ‘xxx’ or play the requested number of rounds, then the game should end.

- When the game ends, you should be able to choose to see your game history.

- During the game, you are able to type either the full word (rock / paper / scissors) or the first letter of the word (R / P / S) to indicate your choice.

- Remember that…

    * Paper beats rock

    * Rock beats scissors

    * Scissors beats paper''')
def yes_no(question):
    r=input(question + "  ").lower
    while True:
        if r == "y" or r== "yes":
            return True
        elif r=="n" or r=="no":
            return False
        else:
            print("You did not choose the valid response")
import random
def cp():
    return random.randint(1, 3)
def cook(decision) :
    while True:
        if decision == "r" or decision == "rock" or decision==1:
            return "rock" , "paper"
        elif decision == "p" or decision == "paper" or decision == 2:
            return  "paper" , "scissor"
        elif decision == "s" or decision == "scissor" or decision == 3:
            return "scissor" , "rock"
        else:
            print("You did not choose the valid response")
            return 0 , 0
def check_int():
    print("How many rounds would you like? Press 0 to join the infinite mode")
    while True:
        try:
            error="Please enter an integer bigger than 0 to play a requested rounds, or choose 0 to start inf mode"
            choose=int(input())
            if(choose<0):
                print(error)
            else:
                return choose
        except ValueError:
            print(error)

def game_play():
    #player's turn
    print("Please input your decision:  ")
    while True:
        temp=input();
        if(temp=="xxx"):
            return "exit"
        player=cook(temp);
        if(player[0]==0):
            continue;
        break;
    print("You choose " +player[0])
    #computer's turn
    print("It's computer turn 🤖")
    print("Please press <Enter> to continue....")
    input()
    computer=cook(cp())
    print("Computer choose "+ player[0])
    #win or lose
    if(player[1]==computer[0]):
        return "Computer"
    elif(player[0]==computer[0]):
        return "Tie"
    else:
        return "Player"
#main 
print("💎📰✂️ Rock Paper Scissors ✂️📰💎") 
if yes_no("Do you want to read the instruction?"):
    instruction()
#round choose
loop=check_int()
temps=0
if(loop==0):
    loop=loop-1
while loop!=0:
    temps=temps+1
    input("Press <Enter> to start this round....")
    print("\n"*10+f"👾👾   Round {temps}  👾👾 ")
    res=game_play()
    if(res=="exit"):
        print("You chose exit...")
        break;
    if(res=="Computer"):
        print("Computer win this round  🤖")
    elif(res=="Player"):
        print("Player win this round 🤫 🧏️")
    else:
        print("You guys are tie 🤝")
    loop=loop-1
#Stat 
print("📊📊 Game Statistics 📊📊")

    

    
    
    
    