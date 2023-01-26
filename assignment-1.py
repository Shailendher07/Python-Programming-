8# program which accepts the radius of a circle from the user and computes teh area
radius = float(input('Enter the radius of the circle: '))
print("The radius of the circle is " ,radius)
area = (22/7)*(radius**2)
print("The area of the circle is " ,area)

# program to accept a filename from the user and print the extension of that
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
