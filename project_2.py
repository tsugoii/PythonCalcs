"""
Week 2: Math and Security Functions
"""
from __future__ import division
import sys
import string
import random
import datetime
import math
MAIN_MENU_QUESTION = "null"

def validator(x_x):
    """Prompts user to validate their input"""
    valid_input = False
    while valid_input is not True:
        print("Is the following input correct:" , x_x , "\tYes or No?")
        validator_correctness = upper_input()
        if validator_correctness == "YES":
            print("Thank you for confirming")
            return True
        if validator_correctness == "NO":
            print("Understood, reprompting...")
            return False
        if validator_correctness == "QUIT":
            print("Are you sure you'd like to Quit?")
            quit_check = upper_input()
            if quit_check == "YES":
                print("Goodbye")
                sys.exit()
            elif quit_check == "NO":
                print("Returning Back")
                break
            else:
                print("Please Enter 'Yes' or 'No'")
        if not validator_correctness.isalpha:
            print("Please Enter 'Yes' or 'No'")

def upper_input():
    """Converts input to uppercase"""
    x_x = input()
    return x_x.upper().strip()

def password_generator():
    """Generates a secure password"""
    print(
        "This Application will generate a secure password based off of the options you will choose")
    valid_input = False
    while valid_input is not True:
        print("Please choose a password length (between 4 and 64 digits)")
        password_length = upper_input()
        if password_length == "QUIT":
            return
        if not password_length.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif int(password_length) > 64 or int(password_length) < 4:
            print("Invalid length, please enter a number between 4 and 64")
        elif validator(password_length):
            valid_input = True
    print(
        "Please choose which password complexity options you'd like to utilize (1-4 , Quit, Done):")
    print("1. Letters")
    print("2. Mixed Case")
    print("3. Numbers")
    print("4. Punctuation")
    letter_bool = False
    number_bool = False
    case_bool = False
    punctuation_bool = False
    valid_input = False
    while valid_input is not True:
        print("Currently selected options:" )
        if letter_bool is True:
            print("Letters")
        if case_bool is True:
            print("Mixed Case")
        if number_bool is True:
            print("Numbers")
        if punctuation_bool is True:
            print("Punctuation")
        print("User Selection: ")
        menu_question = "null"
        menu_question = upper_input()
        if menu_question == "QUIT":
            return
        if menu_question == "1":
            letter_bool = True
        elif menu_question == "2":
            case_bool = True
        elif menu_question == "3":
            number_bool = True
        elif menu_question == "4":
            punctuation_bool = True
        elif menu_question == "DONE":
            break
        else:
            print("Invalid input, Please Enter 1, 2, 3, 4, Quit, or Done")
    characters_chosen = []
    temp_password = ""
    if letter_bool is True:
        characters_chosen += string.ascii_uppercase
    if case_bool is True:
        characters_chosen += string.ascii_lowercase
    if number_bool is True:
        characters_chosen += string.digits
    if punctuation_bool is True:
        characters_chosen += string.punctuation
    for password_length in range(0, int(password_length)):
        temp_password += random.choice(characters_chosen)
    final_password =  "".join(
        temp_password)
    print("Your Generated Password is" , password_length
        , "characters longs and is: " , final_password)

def percentage_calculator():
    """Calculates a percentage"""
    print(
        "This Application will calculate a percentage and display it based off your preferences")
    valid_input = False
    while valid_input is not True:
        print("Please Enter a number for your number to be divided: ")
        numerator_number = upper_input()
        if numerator_number == "QUIT":
            return
        if not numerator_number.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(numerator_number):
            valid_input = True
    valid_input = False
    while valid_input is not True:
        print("Please Enter a number for you to divide by: ")
        denumerator_number = upper_input()
        if denumerator_number == "QUIT":
            return
        if not denumerator_number.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(denumerator_number):
            valid_input = True
    valid_input = False
    while valid_input is not True:
        print("Please Enter a number for the amount of decimal places you'd like to see: ")
        decimal_number = upper_input()
        if decimal_number == "QUIT":
            return
        if not decimal_number.isnumeric():
            print(
                "Invalid Input: Please enter a number or 'Quit'")
        elif validator(decimal_number):
            valid_input = True
    final_number = float(numerator_number)/float(denumerator_number) * 100
    print("Your Percentage for '" , numerator_number , "' Divided by '"
        , denumerator_number , "' Rounded to '" , decimal_number , "' is: ")
    print(f"{final_number:.{decimal_number}f}")

def date_calculator():
    """Calculates difference in dates"""
    print("This Application will return the number of days until July 4, 2025")
    menu_question = "null"
    valid_input = False
    while valid_input is not True:
        print("Would you like to continue?")
        menu_question = upper_input()
        if menu_question == "QUIT":
            return
        if menu_question == "NO":
            print("Returning to main menu")
            return
        if validator(menu_question):
            valid_input = True
        else:
            print("Invalid Input: Please enter 'Yes' , 'No' , or 'Quit'")
    date_today = datetime.date.today()
    date_future = datetime.date(2025, 7, 4)
    date_difference = date_future - date_today
    print("Today's Date is:" , date_today
        , "\t There are:" , date_difference.days , "\t Days until:" , date_future)

def triangle_calculator():
    """Calculates a triangle side using cosine"""
    print("This Application will utilize the law of Cosines to calculate the leg of a Triangle")
    valid_input = False
    while valid_input is not True:
        print("Please Enter your triangle's first side: ")
        triangle_side_a = upper_input()
        if triangle_side_a == "QUIT":
            return
        if not triangle_side_a.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(triangle_side_a):
            valid_input = True
    valid_input = False
    while valid_input is not True:
        print("Please Enter your triangle's second side: ")
        triangle_side_b = upper_input()
        if triangle_side_b == "QUIT":
            return
        if not triangle_side_b.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(triangle_side_b):
            valid_input = True
    valid_input = False
    while valid_input is not True:
        print("Please Enter your triangle's angle: ")
        triangle_angle_degrees = upper_input()
        if triangle_angle_degrees == "QUIT":
            return
        if not triangle_angle_degrees.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(triangle_angle_degrees):
            valid_input = True
    triangle_angle_radians = int(triangle_angle_degrees) * (math.pi / 180)
    triangle_side_c_pre = math.pow(int(triangle_side_a), 2) + math.pow(int(
        triangle_side_b), 2) - 2 * int(triangle_side_a) * int(triangle_side_b) * math.cos(
            float(triangle_angle_radians))
    triangle_side_c_post = math.sqrt(triangle_side_c_pre)
    print("Given your triangle's first side:" , triangle_side_a
        , "\t Your Triangle's second side:" , triangle_side_b
        , "\t And Your Triangle's angle:" , triangle_angle_degrees
        , "\t Your Triangle's last side is: " , triangle_side_c_post)

def cylinder_calculator():
    """calculates cylinder volumer"""
    print("This Application will calculate the volume of a right cylinder based off your input")
    valid_input = False
    while valid_input is not True:
        print("Please enter the cylinder's height: ")
        cylinder_height = upper_input()
        if cylinder_height == "QUIT":
            return
        if not cylinder_height.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(cylinder_height):
            valid_input = True
    valid_input = False
    while valid_input is not True:
        print("Please enter the cylinder's radius: ")
        cylinder_radius = upper_input()
        if cylinder_radius == "QUIT":
            return
        if not cylinder_radius.isnumeric():
            print("Invalid Input: Please enter a number or 'Quit'")
        elif validator(cylinder_radius):
            valid_input = True
        cylinder_volume = math.pi * math.pow(int(cylinder_radius), 2) * int(cylinder_height)
    print("Given your cylinder's height: " , cylinder_height
        , "\t And your cylinder's Raidus: " , cylinder_radius
        , "\t Your cylinder's volume is: " , cylinder_volume)

print("******************************")
print("Welcome to the Math and Security function application")

while MAIN_MENU_QUESTION != "QUIT":
    print("Please select the specific application you'd like to utilize OR Quit: ")
    print("1. Secure Password Generator")
    print("2. Percentage Calculator")
    print("3. Date Calculator")
    print("4. Triangle Calculator")
    print("5. Cylinder Calculator")
    MAIN_MENU_QUESTION = upper_input()
    if MAIN_MENU_QUESTION == "PASSWORD":
        validator(MAIN_MENU_QUESTION)
        password_generator()
    elif MAIN_MENU_QUESTION == "PERCENTAGE":
        validator(MAIN_MENU_QUESTION)
        percentage_calculator()
    elif MAIN_MENU_QUESTION == "DATE":
        validator(MAIN_MENU_QUESTION)
        date_calculator()
    elif MAIN_MENU_QUESTION == "TRIANGLE":
        validator(MAIN_MENU_QUESTION)
        triangle_calculator()
    elif MAIN_MENU_QUESTION == "CYLINDER":
        validator(MAIN_MENU_QUESTION)
        cylinder_calculator()
    elif MAIN_MENU_QUESTION == "QUIT":
        validator(MAIN_MENU_QUESTION)
        print("Thank you for utilizing the Math and Security function application!")
        sys.exit()
    else:
        print("***Invalid Input***")
        print("Please Enter 'Password', 'Percentage', 'Date', 'Triange', 'Cylinder', or 'Quit'\t")
