def calculate(Y , M , D ):
    import datetime
    today = datetime.datetime.now().date()
    born = datetime.date(Y, M , D)
    age = int((today - born).days/365.25)
    print(age)

while True:
    counter = input("Do you want to calculate the age ? [y , n]")
    if counter =='y':
        input_age_year = int(input("Enter the year that you born : "))
        input_age_month = int(input("Enter the month that you born : "))
        input_age_day = int(input("Enter the day that you born : "))
    else:
        break
    calculate(input_age_year , input_age_month , input_age_day)
