import langdetect

from langdetect import detect

text = input("Eter any sentences that you want...\n")
 
print('language of your sentences is ---> ' , detect(text))