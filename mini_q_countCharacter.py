def countch(word):
    counter = {}
    for i in word:
        if i in counter: 
            counter[i] += 1
        else :
            counter[i] = 1

    print(counter)

word = input("print your word pls:   ")

print(countch(word))
