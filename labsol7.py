list1 = [7.5, 10, 6, 23.2, 1, -3, 9.7] 
print("List1 =",list1)
for i in range(len(list1)):
  print(list1[i])
  if list1[i] is float :
    print(list1[i])
    print("2 * list1[i] = ",2 *list1[i])
  elif i is int :
    print(list1[i])
    list1[i] = list1[i] **3
  elif i == 10:
    print(list1[i])
print("The updated list is:",list1)