from countryinfo import CountryInfo

count = input("Enter your country name: ")

count_info = CountryInfo(count)

print("Capital of" , count , " is " , count_info.capital())
language = count_info.languages()
print("The langue of ",count ,"is" , language[0])
border = count_info.borders()
print('The border of ' , count , 'is ' , border[::])
curancy = count_info.currencies()
print( "The currencies of " , count , 'is' , curancy[0])

