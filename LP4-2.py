def main():
  weight = int(input(" Enter weight in kilograms:"))
  length = int(input(" Enter length in centimeters:"))
  width = int(input(" Enter width in centimeters:"))
  height = int(input(" Enter height in centimeters:"))
  cube = 0.0
  
  if weight >= 27:
    print("Too Heavy")
  else:
    return True
  cube = length * width * height
  if cube >= 100000:
    print("Too Large")
  else: 
    return True
  if cube >= 100000 and weight >= 27:
    print("Too Heavy and Too Large")
    
  pass


if __name__ == "__main__":
  main()