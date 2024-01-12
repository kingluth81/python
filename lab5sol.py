n = input("Enter an integer between 100 and 200")
x= (float(n))
if x < 0:
  print("invalid: [x] is negative")
elif x < 100:
  print("Invalid: [x] is too low")
elif x > 200:
  print("Invalid: [x] is too high")
else: x >= 100 or x<= 200
print("[x] is a valid entry")
if x % 5==0:
  print("[x] is a valid entry")
  b = x % 5
  print(b)
 else:
    print("[x] is NOT divisible by 5")
	