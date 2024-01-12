str1 = input("Please enter alphabetic string: ") #asks user to input a string 
print(str1) #prints the string
if str1.isalpha(): #checks if string is aplhabetic
  print(str1,"is a valid string") #prints if the string is valid
  print(str1.center(25, '#')) #prints and pads the string to the center
else:
  print(str1,"is NOT valid") #prints if the string is not valid
  print(str1.center(25, '#')) #prints and pads the string to the center
if str1[0].islower(): #checks if first character of string is lower case
  print(str1, "in lower case is:", str1.lower()) #prints string in lower case
elif str1[0].isupper(): #chekcs if first character of string is upper case
  print(str1, "in upper case is:", str1.upper()) #prints string in upper case