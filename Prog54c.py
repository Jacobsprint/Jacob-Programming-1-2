Radius= float(input("Please enter the Radius: "))

print( "The Radius of the circle ", Radius)

PieValue= 3.14159

Area = PieValue * Radius * Radius
Circumference = 2 * PieValue * Radius

Area = "{:.3f}".format(Area)
Circumference = "{:.3f}".format(Circumference)

print("The Area of the circle is ", Area )
print("The Circumference of the circle is ", Circumference )
