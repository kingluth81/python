str1 = input("Please enter an alphabetic string in uppercase: ") #asks user to input an alphabetic string
print("You entered:",str1) #tells user what they entered
if str1[0:2] <= 'HM': #tells user which category the first 2 digits belong to
	print(str1,'belongs to group 1.') #tells user if the first 2 digits belong in group 1
elif str1[0:2] <= 'KI': #tells user which category the first 2 digits belong to
	print(str1,'belongs to group 2.') #tells user if the first 2 digits belong in group 2
elif str1[0:2] <= 'TZ' : #tells user which category the first 2 digits belong to
    print(str1,'belongs to group 3.') #tells user if the first 2 digits belong in group 3
elif str1[0:2] >= 'TZ' : #tells user which category the first 2 digits belong to
    print(str1, "belongs to group 4.") #tells user if the first 2 digits belong in group 4