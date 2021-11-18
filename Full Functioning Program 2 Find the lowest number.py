# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number.

First_Number = int(input('First Number: '))
Second_Number = int(input('Second Number: '))
Third_Number = int(input('Third Number: '))

if First_Number < Second_Number and First_Number < Third_Number: # The First_Number may be the lowest number.
    print(f'The lowest number is {First_Number}.')
else: # The Second_Number may be the lowest number. 
    if Second_Number < First_Number and Second_Number < Third_Number:
        print(f'The lowest number is {Second_Number}.')
    else: # The Third_Number may be the lowest number.
        if Third_Number < First_Number and Third_Number < Second_Number:
            print(f'The lowest number is {Third_Number}.')
            exit()

# Steps
# 1. Inquire about the first number from the user.
# 2. Inquire about the first number from the user.
# 3. Inquire about the first number from the user.
# 4. If the first number is less than the second and third numbers, print the first number as the lowest number.
# 5. Else if the second number is less than the first and third numbers, print the second number as the lowest number.
# 6. Otherwise, if the first and second numbers are both greater than the third number, the third number should be printed as the lowest number.