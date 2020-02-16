"""
This program tells the color on a chessboard, based on the position enterred.

project: #1_03 CS1030
author: Zack Khalidov
"""

#Constant
SHUT_DOWN = "Program has shut down!"
INVALID = "Invalid entry!"
WHITE = "Square %s is white."
BLACK = "Square %s is black."

#parity_translator method takes in the xPlane input and translates it to
#either odd or even based on its position from left to right.
#example: a = 1 = odd, d = 4 = even
def parity_translator (parity):
    translator = {
        "a" : "odd",
        "b" : "even",
        "c" : "odd",
        "d" : "even",
        "e" : "odd",
        "f" : "even",
        "g" : "odd",
        "h" : "even"
        }
    return translator.get(parity)

print("Enter a position (a-h and 1-8) on a cheessboard to print the color.")
print("Example: 'a1' is black, 'd3' is white.")
print("Empty entry will shut the program down.")

#Loops until a break is introduced. Breaks will be called when there is an
#error with the input, and at the end of the program.
while True:
    position = input("Enter a position: ")

    #If nothing is entered the program shuts down.
    if not position:
        print(SHUT_DOWN)
        break

    #xPane is a-h
    xPlane = position[0:1]
    #yPlane is 1-8
    yPlane = position[1:2]

    #If the input is not a-h the program shuts down.
    if not (xPlane == "a" or xPlane == "b" or xPlane == "c" or xPlane == "d" or
        xPlane == "e" or xPlane == "f" or xPlane == "g" or xPlane == "h"):
        print(INVALID)
        break

    #If the input is not 1-8 the program shuts down.
    if (int(yPlane) < 1 or int(yPlane) > 8):
        print(INVALID)
        break

    #Calling parity_translator to translate input into parity.
    parity = parity_translator(xPlane)

    #On odd parity the modulus of the yPlane == 0 is white, != 0 is black.
    if parity == "odd":
        if (int(yPlane) % 2) == 0:
            print(WHITE % (position))
        else:
            print(BLACK % (position))

    #On even parity the modulus of the yPlant == 0 is black, != is white.
    else:
        if (int(yPlane) % 2) == 0:
            print(BLACK % (position))
        else:
            print(WHITE % (position))

    #Exits the program
    print(SHUT_DOWN)
    break
