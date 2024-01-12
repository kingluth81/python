list1 = [7.512, 0, 6, 23.62, 1, -3, 9.777] #elements in list1
print("list 1 =",list1) #prints the original list
n = int(input("Please enter an integer: ")) #asks user to inout an integer
list1.insert(3, n) #inserts integer of users choice into position 3
print("Updated list1:",list1) #prints updated list
sum = sum(list1) #calculates the sum of the list
print("The sum of all elements in list1: ", sum) #prints the sum of the list
print("The sum of all elements rounded in list1: ", round(sum)) #prints the sum of the list rounded
print("The highest number in list1:", max(list1)) #prints the highest number in the list
print("The lowest number in list1 is:",min(list1)) #prints the lowest number in the list
print("The reversed list is:",list1[::-1]) #prints the reverse of the updated list