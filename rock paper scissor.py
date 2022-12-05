import random
option = ["rock" , "paper" , 'scissor']
user_win = 0
pc_win = 0

while True:
    random_number = random.randint( 0 , 2)
    # rock = 0 , paper = 1 , scissors = 2
    if user_win== 3 or pc_win == 3:
        break 
    user_input = input("Type Rock/Paper/Scissor or Q to quit.").lower()
    if user_input == "q":
        quit()
    if user_input not in option:
        continue
    
    pc_pick = option[random_number]
    print("Computer picked" ,pc_pick , "." )

    if user_input == "rock" and pc_pick == "scissor":
        print("You won :) ")
        user_win +=1
        
    elif user_input == "paper" and pc_pick == "rock":
        print("You won :) ")
        user_win +=1
        
    elif user_input == "scissor" and pc_pick == "paper":
        print("You won :) ")
        user_win +=1
    elif (user_input == "scissor" and pc_pick == "scissor") or (user_input == "paper" and pc_pick == "paper") or(user_input == "rock" and pc_pick == "rock"):
        print("equal ")
        
       
    else:
        print("You lost :(")
        pc_win +=1 
    continue     

print("you won" ,user_win , "time. " )
print("computer  won" ,pc_win , "time. " )
if user_win > pc_win:
    print("You defeat machine ! ")
else:
    print("The victory of machines over people continues")
    
print("Good Bye ! ")