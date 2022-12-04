def palindrome(sentences):
    for i in (",.'?/><}{'"):
        sentences = sentences.replace(i , "")

    palindrome = []
    words = sentences.split(" ")
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return(palindrome)

input = input("Enter sentences :  ")
print(palindrome(input))



    