heghit = float(input("Enter your heghit in centimeters: "))
weghit = float(input("Enter your weghit in kg: "))
heghit = heghit /100
bmi = weghit/heghit**2
print("Your BMI is : " , bmi)
print("#-----------------------#")
if bmi > 0 :
    if bmi <= 16 :
        print("You are severely underweight")
    elif bmi <= 18.5 :
        print("You are underweight")
    elif bmi <= 25 :
        print("You are Healthy")
    elif bmi <= 30 :
        print("You are overweight")
    else :
        print("You are severely overweight")
else: 
    print("Enter valid details")