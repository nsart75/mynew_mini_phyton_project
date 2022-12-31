import random 

number_1 = 1
number_6 = 6


again = input("Do you want to roll send [y] or [yes]? ")
while again == 'yes' or 'y' :
    print("Rolling the Dices.................\n")
    print("Your number issssss:   ")
    print('#-----------#',random.randint(number_1 , number_6) , '#-----------#\n')
    again = input("Do you want to  again roll [yes] or [no] ? ").lower()
  