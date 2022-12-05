def least_commen_multiple(a ,b):
    if a > b :
        grater = a 
    elif b > a : 
        grater = b
    while True:
        if ((grater % a == 0 ) and (grater % b == 0)):
            lcm = grater
            break
        grater += 1
    return lcm

a = int(input("Enter a :  "))
b = int(input("Enter b :  "))
print("least commen multiple between " , a ," ", b ,"is " ,least_commen_multiple(a , b) )

