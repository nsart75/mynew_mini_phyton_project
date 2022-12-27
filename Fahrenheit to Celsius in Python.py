def convert(C):
    f = float(C)
    f_result = (f-32)*5/9
    return f_result

celsius = input("Enter fahrnheit to convert:  ")

print(convert(celsius))

