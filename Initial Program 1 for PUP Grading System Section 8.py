# Create a program that will ask for grade percentage. 
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def startup():
    user_option1 = input('Do you want to start evaluating student grades? [y/n]: ')
    if user_option1 == 'y':
        gradingsystem()
    elif user_option1 == 'n':
        print('Thank you.')
        exit()

def gradingsystem():
    grade_percentage = float(input('The grade percentage of the student: '))

    if grade_percentage >= 97 or grade_percentage == 100:
        print('Grade/Mark: 1.0')
        print('Description: Excellent')
    else:
        if grade_percentage >= 94 and grade_percentage <= 96:
            print('Grade/Mark: 1.25')
            print('Description: Excellent')

startup()

# Steps:
# 1. Define function startup(). It will ask if you want to start evaluate student grades. If 'y' it will run the function gradingsystem().
# 2. Define function gradingsystem(). It will ask the grade of the student from the user then convert it to float and store it to a variable.
#     Command: grade_percentage = float(input('The grade percentage of the student: '))
# 2. If the grade percentage of the student is ranging from 97 to 100:
#     print: Grade/Mark: 1.0 and Description: Excellent
