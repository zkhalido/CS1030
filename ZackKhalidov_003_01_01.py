"""
This program takes in height in feet and inches and converts it to meters.

project: #1_01 CS1030
author: Zack Khalidov
"""
#Constant
CENTI_CONV = 2.54
CENTI_TO_METER = 100.00
INCH_IN_FEET = 12
TALL_PERSON = 96
SHUT_DOWN = "Program has shut down!"

while True: #While loop is used to break if no input is entered.

    #Prompt user to enter feet.
    feet = input("Enter feet: ")
    #Checks if there is a value for feet.
    if not feet:
        print(SHUT_DOWN)
        break

    #Prompt user to enter inches.
    inches = input("Enter inches: ")
    #Checks if there is a value for inches.
    if not inches:
        print(SHUT_DOWN)
        break

    feet = int(feet)
    inches = int(inches)

    #Conversions feet to inches, and adds to inches to total.
    total_inches = (feet * INCH_IN_FEET) + inches
    if inches >= TALL_PERSON:
        print("That's one tall person!")

    #Converting total inches to centimenters.
    centimeters = total_inches * CENTI_CONV
    #converting centimeters to meters.
    meters = centimeters / CENTI_TO_METER

    #Prints result of original height and metric conversion.
    #The value for meters is rounded 2 decimal places.
    print("Height in standard: %d'%d, height in metric: %.2f" % (feet, inches, meters))

    #Exits the program.
    break
