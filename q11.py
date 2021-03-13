'''
Write a program that takes the radius of a sphere
(a floating point number) as input and then outputs the sphere's 
diameter, circumference, surface area and volume.
'''
pi=22/7
radius = float(input("Enter radius of a sphere"))
diameter =(2 * radius)
circumference = (diameter * pi)
surfacearea = (4 * pi * radius **2)
volume =(4/3) * (pi * radius ** 3)
print(f"Diameter of sphere is {diameter}")
print(f"Circumference of sphere is {circumference}")
print(f"Surface area of sphere is {surfacearea}")
print(f"Volume of sphere is {volume}")
