import random

top_of_range = input("Enter Number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("pls type number larger than 0 next time !")
        quit()
else:
    print("pls type number larger than 0 next time !")
    quit()
random_number = random.randint(0 , top_of_range)
guess = 0 
while True:
    guess +=1 
    user_guess = input("Make guess :   ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("pls type number larger than 0 next time !")
        continue
    if user_guess == random_number:
        print("Well done! :) you can guess in "+str(guess)+" time")
        break
    elif user_guess > random_number :
        print("guess smaller !")
    elif user_guess < random_number :
        print("guess biger !")




