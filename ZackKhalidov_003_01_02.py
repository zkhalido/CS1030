"""
This program converts miles per gallon to liters per kilometer.

project: #1_02 CS1030
author: Zack Khalidov
"""
#Constants
MILE_TO_KILO = 1.609
GALLON_TO_LITER = 3.785

while True: #While loop is used to break if no input is entered.

    #Takes the input for mpg and converts to an integer.
    mpg = input("Enter the miles per gallon: ")

    #Checks for no value entry.
    if not mpg:
        print("The mpg entered is invalid!")
        break

    #Cast to float to check if mpg <= 0.
    mpg = float(mpg)

    #Checks if the enterred value is <= 0.
    if mpg <= 0:
        print("The mpg entered is invalid!")
        break

    #Converting mpg to kmL.
    kmL = ((mpg * MILE_TO_KILO) / GALLON_TO_LITER)

    #Print the input mpg and converted result.
    print("Mpg entered: %.1f, converted to km/L: %.1f" % (mpg, kmL))

    #Shuts the program down
    break
