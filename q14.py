'''
An employee’s total weekly pay equals the hourly wage multiplied by the
 total number of regular hours plus any overtime pay. Overtime pay 
 equals the total overtime hours multiplied by 1.5 times the hourly 
 wage. Write a program that takes as inputs the hourly wage, 
 total regular hours, and total overtime hours and displays an 
 employee’s total weekly pay.
'''

hourlywage = float(input("Enter wages"))
totalregularhours = float(input("Enter total regulars hrs"))
totalovertimehours = float(input("Enter total over time hrs"))

totalweeklypay = totalregularhours * hourlywage + totalovertimehours * hourlywage * 1.5
print("The total weekly pay is", totalweeklypay)