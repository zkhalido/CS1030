"""
This program simulates coin flips until three consecutive flips of the same
side of the coin is tossed.

project: #2_02 CS1030
author: Zack Khalidov
"""

from random import randint

record = [] # Tracks the number of flips to get TTT or HHH.

print("Enter '0' or '' or <0 to exit program.")

def coin_flip(): # This function returns either 1 or 2 randomly.
    return randint(1,2)

while True: # While loop used to hand cases where program exiting.
    # Resets every entry to track new round.
    heads = 0
    tails = 0
    endAt = ""

    repetitions = input("\nEnter how many simulations you want to run: ")

    if repetitions == "": # If nothing is enterred the program exits.
        print("Exiting the program.")
    elif int(repetitions) > 0: # If number of repetitions is larger than 0.
        i = 1
        while int(repetitions) >= i:
            position = coin_flip()

            if position == 1: # 1 is Heads.
                print("H", end = " ")
                heads += 1
                tails = 0 # Resets Tails counter if Heads.
            elif position == 2: # 2 is Tails.
                print("T", end = " ")
                tails += 1
                heads = 0 # Resets Heads counter if Tails.

            # When 3 of a kind is rolled sets endAt to the side and breaks loop.
            if heads == 3:
                endAt = "heads"
                break
            elif tails == 3:
                endAt = "tails"
                break

            i+=1

    if endAt != "": # When endAt is not blank.
        record.append(i)
        print("\nIt took %d flips to get three %s in a row." % (i, endAt))
        print("The maximum is %i, the minimum is %i, the average is %i "
              % (max(record), min(record), (sum(record)/len(record))))
    elif repetitions == "":
        break
    else: # If no TTT or HHH is rolled prints text below.
        print("\nThere was no three consecutive flips of the same side of the coin" +
              " after %s flips." % (repetitions))
