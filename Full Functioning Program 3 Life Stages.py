# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

def startupage():
    user_option1 = input('Are you a human? [y/n]: ')
    if user_option1 == 'y':
        ageF()
    elif user_option1 == 'n':
        print('Welcome to planet earth.')
        exit()

def ageF():
    age = int(input('Input your age: '))
    if age >= 0 and age <= 12: # Possible your a just a kid.
        print('Your a Kid.')
    else: # There's a possibility that your a teen.
        if age >= 13 and age <= 17:
            print('Your a Teen.')
        else: # There's a possibility your a debutant.
            if age == 18:
                print('Debut')
            else: # Possible your an Adult
                if age >= 19:
                    print('Your an Adult.')
    repeat()

def repeat():
    user_opt1 = input('Do you want to input another age? [y/n]: ')
    if user_opt1 == 'y':
        age_repeat()
    else:
        if user_opt1 == 'n':
            print('Thank you.')
            exit()

def age_repeat():
    ageF()

startupage()

# Steps:
# 1. Define function startupage(). It will ask if you are a human. If 'y' it will run the function ageF().
# 2. Define function gradingsystem(). It will ask the age from the user then convert it to integer and store it to a variable.
#     Command: age = int(input('Input your age: '))
# 3. If your age is ranging from 0 to 12. It will print Your a Kid.
# 4. If your age is ranging from 13 to 17. It will print Your a Teen.
# 5. If your age is equal to 18. It will print Debut.
# 6. Otherwise if your age is 19 above. It will print Your an Adult.
# 7. Define function repeater() that will inquire user if he/she wants to input another age.
# 8. If the yes = ('y') it will run the define function age_repeat() that will redo the function ageF().
# 9. If the no = ('n') it will print Thank you.