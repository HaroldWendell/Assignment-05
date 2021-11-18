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
    if grade_percentage >= 96.5 or grade_percentage == 100:
        print('Equivalent Grade/Mark: 1.0')
        print('Description: Excellent')
    else:
        if grade_percentage >= 93.5 and grade_percentage < 96.5:
            print('Equivalent Grade/Mark: 1.25')
            print('Description: Excellent')
        else:
            if grade_percentage >= 90.5 and grade_percentage < 93.5:
                print('Equivalent Grade/Mark: 1.5')
                print('Description: Very Good')
            else:
                if grade_percentage >= 87.5 and grade_percentage < 90.5:
                    print('Equivalent Grade/Mark: 1.75')
                    print('Description: Very Good')
                else:
                    if grade_percentage >= 84.5 and grade_percentage < 87.5:
                        print('Equivalent Grade/Mark: 2.0')
                        print('Description: Good')
                    else:
                        if grade_percentage >= 81.5 and grade_percentage < 84.5:
                            print('Equivalent Grade/Mark: 2.25')
                            print('Description: Good')
                        else:
                            if grade_percentage >= 78.5 and grade_percentage < 81.5:
                                print('Equivalent Grade/Mark: 2.5')
                                print('Description: Satisfactory')
                            else:
                                if grade_percentage >= 75.5 and grade_percentage < 78.5:
                                    print('Equivalent Grade/Mark: 2.75')
                                    print('Description: Satisfactory')
                                else:
                                    if grade_percentage >= 74.5 or grade_percentage == 75:
                                        print('Equivalent Grade/Mark: 3.0')
                                        print('Description: Passing')
                                    else:
                                        if grade_percentage >= 64.5 and grade_percentage < 74.5:
                                            print('Equivalent Grade/Mark: 5.0')
                                            print('Description: Failure')
                                        else:
                                            if grade_percentage < 64.5:
                                                print('Possible Grade/Mark: Inc., W, or D')
                                                print('Possible Description: Incomplete, Withdrawn, or Dropped')
    repeater()

def repeater():
    user_option2 = input('Do you want to continue evaluating student grades? [y/n]: ')
    if user_option2 == 'y':
        grade_repeat()
    else:
        if user_option2 == 'n':
            print('Thank you for evaluating student grades.')
            exit()

def grade_repeat():
    gradingsystem()

startup()

# Steps:
# 1. Define function startup(). It will ask if you want to start evaluate student grades. If 'y' it will run the function gradingsystem().
# 2. Define function gradingsystem(). It will ask the grade of the student from the user then convert it to float and store it to a variable.
#     Command: grade_percentage = float(input('The grade percentage of the student: '))
# 3. If the grade percentage of the student is ranging from 97 to 100. It will print Grade/Mark: 1.0 and Description: Excellent
# 4. If the grade percentage of the student is ranging from 94 to 96. It will print Grade/Mark: 1.25 and Description: Excellent
# 5. If the grade percentage of the student is ranging from 91 to 93. It will print Grade/Mark: 1.5 and Description: Very Good
# 6. If the grade percentage of the student is ranging from 88 to 90. It will print Grade/Mark: 1.75 and Description: Very Good
# 7. If the grade percentage of the student is ranging from 85 to 87. It will print Grade/Mark: 2.0 and Description: Good
# 8. If the grade percentage of the student is ranging from 82 to 84. It will print Grade/Mark: 2.25 and Description: Good
# 9. If the grade percentage of the student is ranging from 79 to 81. It will print Grade/Mark: 2.5 and Description: Satisfactory
# 10. If the grade percentage of the student is ranging from 76 to 78. It will print Grade/Mark: 2.75 and Description: Satisfactory
# 11. If the grade percentage of the student is equal to 75. It will print Grade/Mark: 3.0 and Description: Passing
# 12. If the grade percentage of the student is ranging from 65 to 74. It will print Grade/Mark: 5.0 and Description: Failure
# 13. If the grade percentage of the student is below 65. It will print Possible Grade/Mark: Inc., W, or D and Possible Description: Incomplete, Withdrawn, or Dropped
# 14. Define function repeater() that will inquire user if he/she wants to continue evaluating grades.
# 15. If the yes = ('y') it will run the define function grade_repeat() that will redo the function gradingsystem().
# 16. If the no = ('n') it will print Thank you for evaluating student grades.