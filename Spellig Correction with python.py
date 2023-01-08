from textblob import TextBlob

def convert(string):
    li = list(string.split())
    return li
input_words = input(" Enter your word to cheking the spelling: ")
words = convert(input_words)
correct_word = []

for i in words:
    correct_word.append(TextBlob(i))

print("wrong words are : " , end = " ")
for i in correct_word:
    if i.correct() not in words:
        print(i, end = " ")   
 
print()
print("Corrected Word are : ")
for i in correct_word:
    print(i.correct() , end = ' ')
    