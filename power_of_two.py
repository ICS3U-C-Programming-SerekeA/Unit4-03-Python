# !/usr/bin/env python3
# created by: Sereke Asfeday
# Created on: 13, November 2026
# This program calculates the power of two from 0 to the the user whole number


def main():

    # Get user input as string for the whole number
    user_num_as_str = input("Enter a whole number: ")

    # Use try to catch any run time errors or exception.
    try:
        # cast the user input from string  to an integer
        user_num_int = int(user_num_as_str)

        # here im making acondition that checks if user input is aq negative number or not,
        # if it is negative it will print the message below and if its false it will go to else block.
        if user_num_int < 0:
            print("{}, is not a valid whole number.".format(user_num_int))

        # This Else block it will run after the if condition is false, which mean user input is a valid whole number.
        else:

            # This is for loop that will run from 0 to the user input number and calculate the power of two for each number.
            for counter in range(user_num_int + 1):
                power_of_two = counter**2

                # This will print the result of the power of two for each number from 0 to the user input number.
                print("{}^2 = {}".format(counter, power_of_two))

    # This is exception block it will run after try to casting to intyeger falis,
    # which means user input is not a valid whole number.
    except ValueError:

        # This will print the message below if user input is not a valid whole number.
        print("{}, is not a valid whole number.".format(user_num_as_str))

    # finally block this is a thank message for using this program and
    #  it will display whether the user input is valid or not.
    finally:
        print("Thank you for using this program.")


# callling the main function to run the program.
if __name__ == "__main__":
    main()
