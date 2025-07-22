def game():
    print("Lets play rock paper scissor")
    import random
    AI=random.choice([1,0,-1])
    you=input("YOU CHOOSE: ")                               #1 for ROCK
    d1={1:"ROCK",0:"PAPER",-1:"SCISSOR"}                    #0 for PAPER
    d2={"ROCK":1,"PAPER":0,"SCISSOR":-1}                    #-1 for SCISSOR
    your=d2[you.upper()]
    print(f"YOUR APPONENT CHOOSE: {d1[AI]}")
    if(AI==your):
        print("Its an draw")
    else:
        if(AI==1 and your==-1):
            print("you lose")
        elif(AI==1 and your==0):
              print("you win")
        elif(AI==0 and your==-1):
            print('you win')
        elif(AI==0 and your==1):
            print("you lose")
        elif(AI==-1 and your==0):
            print("you lose")
        elif(AI==-1 and your==1):
            print("you win")
        else:
            print("Something is wrong")
game()