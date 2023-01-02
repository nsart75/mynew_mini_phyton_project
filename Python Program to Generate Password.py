import random
paslen = int(input("Enter the len of password that you want\n "))
s = 'qwertyuiop[]asdfghjkljhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM'
password = "".join(random.sample(s , paslen))
print('Your password is --> ' , password , ' <--')