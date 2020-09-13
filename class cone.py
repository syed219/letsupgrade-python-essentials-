# python program to calculate volume and surface area of cone
# importing math library for value of Pi
import math
pi=math.pi
# function to calculate volume of cone
def volume(r,h):
    return (1/3)*pi*r**2*h
# function to calculate surface area of cone
def surface_area(r,s):
    return pi*r*s+pi*r**2
#driver code
radius=float(input("Enter radius:"))
height=float(input("Enter height:"))
slat_height=float(input("Enter slat height:"))
print("Volume of cone:",volume(radius,height))
print("Surface area of cone:",surface_area(radius,slat_height))
