'''1.Create a dictionary with the city name and its corresponding pin code.  Write a python code to retrieve the pin code given the city name. '''
d1={"delhi":001,"chennai":603202,"mogappeir":34343}
city=input("Enter the city")
if city in d1.keys():
	print (d1[city],"is the pin code")
else:
	print("The city is not found")
