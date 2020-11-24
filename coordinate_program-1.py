# coordinate_program.py
# Coordinate solving program for CSCI 111-900
# Last edited 9/23/19 by Pat Doyle

import math     #imports math module

x = float(input("Enter x value. "))
y = float(input("Enter y value. ")) #inputs x and y coordinates

quadrant = 0    #Creates variable quadrant so a value can be assigned

if (x >= 0) and (y >=0):
    quadrant = 1
elif (x <= 0) and (y >= 0): #determines quadrant of coordinate based on
    quadrant = 2            #whether or not x or y is positive or negative
elif (x <= 0) and (y <= 0):
    quadrant = 3
else:
    quadrant = 4
    
distance_from_origin = (math.hypot(x,y))    #uses distance formula to determine distance from origin

print ("This coordinate is located in quadrant", quadrant , "and its distance from origin is", distance_from_origin, ".")   #ouputs data
    
    



