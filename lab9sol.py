def calc_angle(n):
  angle = (n-2)*180/n
  return angle

def main():
  n = int(input("Enter the number of sides in your ploygon: "))
  print('The interior angle of a reular polygon with %d sides is: %.1f '%(n,calc_angle(n)))

if __name__== "__main__":
  main()