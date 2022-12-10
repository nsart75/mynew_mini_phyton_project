tallies = {'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def roman(Roman_Numberal):
    sum = 0 
    for i in range (len(Roman_Numberal) -1):
        left = Roman_Numberal[i]
        right = Roman_Numberal[i +1]
        if tallies[left] < tallies[right] :
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[Roman_Numberal[-1]]
    return sum

roman_num = input("Enter Roman Number:  ")
print("your number is : " , roman(roman_num))