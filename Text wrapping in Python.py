import textwrap

value = input("Enter your paragraph to wrap :   ")
width = int(input("Enter the width that you want for paragraph:   "))

waraper = textwrap.TextWrapper(width= width)

word_list = waraper.wrap(text=value)

for element in word_list:
    print(element)

    