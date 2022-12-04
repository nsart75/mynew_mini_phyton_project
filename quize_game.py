print("Welcome to my game !!!!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okey Let's play :]")
score = 0
answer = input("what does CPU satand for? ").lower()
if answer == "central processing unit":
    print("correct! ")
    score += 1 
else:
    print("Incorrect ! ")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct! ")
    score += 1 
else:
    print("Incorrect ! ")

answer = input("What does RAM stand for? ").lower()
if answer == "ramdom access memory":
    print("correct! ")
    score += 1 
else:
    print("Incorrect ! ")

print('you got ' +str(score) + '  score')
print('you got ' +str(score/4 * 100) + '  percent')