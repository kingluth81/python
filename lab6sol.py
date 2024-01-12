count = 0
colors = []
response = ('y' , 'n')
while colors not in colors:
  colors = input("Would you like to enter 3 of your favorite colors? (y/n): ")
  if response == 'y' :
    print(colors)
  elif response == 'n' :
    print("You have entered (0) colors.")