total =0
max=0
count=0
while (true):
	num = (input("Please enter a positive integer (digits only) to continue: "))
	if (num.isnumeric()):
		print(int(num))
	total = total + int(num)
	count+=1
	if int(num) > max_:
		max_=int(num)
	else:
		break
	else:
		break
if (count>0):
	x = total/count
print("Maximum value entered is: ",max_)
print("Sum of all entered inputs is: ", total)
print("The total number of inouts entered is: ", =count)
print("The average of entered number is: ",x)

#******************************************************
str1 = input("Please enter a string with at least 7 characters: ")
print("You entered: ",str1)
j = 0
x = 1
n = 0
y = len(str1)

while(j != len(str1)):
  print(str1[x:y] + str1[n:j+1])
  j+=1
  x+=1


#**************************************************
L1 = [2, 15, 'Carol', 7.4, 0, -10, -6, 42, 27, -1, 2.0, 'hello', [2, 4], 23]
odd = []
even = []
L2 = []
print("L1 =",L1)
e = 0 #even counter
j = 0
o = 0 #odd counter
n = 0
for int in L1:
  if L1[n]:
    L2.append(L1)
  n+=1

print(L2)
while(j != len(L1)):

  if L1[j] is str :
    even.append(L1[j])
    e+=1
  else:
    odd.append(L1[j])
    o+=1
  j+=1
print("The list of odd numbers: ", odd)
print("The list of even numbers: ", even)
