"""
This program converts a list of letter grades entered by a user to a GPA.

project: #2_01 CS1030
author: Zack Khalidov
"""

grade_record = [] # Initializing array to append point to.
quit = False

# This function turns letter grades into points.
def grade_translator(grade):
    translator = {
        "A+" : 4.2,
        "A" : 4.0,
        "A-" : 3.9,
        "B+" : 3.7,
        "B" : 3.2,
        "B-" : 3.0,
        "C+" : 2.8,
        "C" : 2.2,
        "C-" : 2.0,
        "D+" : 1.8,
        "D" : 1.2,
        "F" : 0
        }
    return translator.get(grade)

# This function checks if the input grade is accepted.
def accepted_grades(grade):
    if (grade == "A+" or grade == "A" or grade == "A-" or grade == "B+"
        or grade == "B" or grade == "B-" or grade == "C+" or grade == "C"
        or grade == "C-" or grade == "D+" or grade == "D" or grade == "D"
        or grade == "F"):
        return True
    else:
        return False

print("Enter capital letter grade to calculate your GPA (ex. A+, B, C-)",
      "\nEnter '' to calculate GPA, enter 'quit' to close program.")

while True: # Outer loop calculates the overall GPS for the grades enterred.

    while True: # Inner loop prints the current GPA.
        grade = input("Enter a grade: ")

        if grade == "": # Breaks the loop if nothing is enterred.
            break
        if grade == "quit":
            quit = True
            break

        # Calls accepted_grades function and returns True if grade is accepted.
        if accepted_grades(grade):
            grade_record.append(grade_translator(grade))
        else:
            print("The grade enterred '%s' is invalid" % (grade))

    if len(grade_record) > 0:
        gpa = sum(grade_record) / float(len(grade_record))
        print ("Your GPA is %.2f" % (gpa))
    else:
        print ("No GPA calculated")

    if quit == True:
        break
