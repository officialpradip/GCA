'''
Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs
 who like to buy LP record albums. The store rents new videos for  
 3.00anight,andoldiesfor 2.00 a night.

Write a program that the clerks at Five Star Retro Video can use to 
calculate the total charge for a customer’s video rentals.

The program should prompt the user for the number of each type of video
 and output the total cost.
'''

n1= float(input("Enter number of videos"))
n2= float(input("Enter the number of oldies"))
result = (n1*3+n2*2)
print(result)