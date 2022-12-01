
def main():
  numeggs = int(input("Enter number of Eggs Purchased:" ))
  dozleft = numeggs % 12
  doz = float(numeggs) / 12
  p = 0
  if doz < 4:
    p = .50
  if doz > 4 and doz < 6:
    p = .45
  if doz > 6 and doz < 11:
    p = .40
  if doz > 11:
    p = .35

  dozp = doz * p

  sin = float(p) / 12
  sin = round(sin, 2)
  sinp = dozleft * sin
  
  total = sinp + dozp
  total = round(total,2)
  print("The bill is equal to $", total)
  
  
  
  pass


if __name__ == "__main__":
  main()