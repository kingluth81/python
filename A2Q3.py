L1 = ['apple', 'ball', 'camera', 'dog', 'elephant', 'flower', 'go'] #list with 7 strings
print("L1 =",L1) #prints the list
n = input("Enter an integer between 0 and 6: ") #asks user to input an integer
x = (int(n)) #assigns as an integer
if x > 6:
  print("Invalid [x] is too high") #if x is greater than 6 it prints suitable message
elif x < 0:
  print("invalid [x] is too low") #if x is less than 0 it prints suitable message
elif x >= 0 or x <= 6:
  print("[x] is a valid entry") #if x fits the criteria it prints suitable message
  print("The element of L1 with index", x, "is",L1[x]) #prints the element of L1 with index
if L1[int(n)][-1] != "a" or "e" :
  print("The number of characters:",len(L1[int(n)]))
else :
  print("The selected element in uppercase is:",L1[x].upper()) #prints the element in uppercase