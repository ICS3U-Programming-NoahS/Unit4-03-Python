#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 13th, 2023
# This program asks the user to enter a whole number
# then tells the user every number squared from 0 to that number


def main():
    # Get the whole number
    user_num_string = input("Enter a whole number: ")

    # Making sure the number is an integer
    try:
        user_num_int = int(user_num_string)

        # Check if the number is negative
        if user_num_int < 0:
            print("{} is not a whole number.".format(user_num_int))
        # Check if the number is 0
        elif user_num_int == 0:
            print("0^2 = 0")
        else:
            # For loop to find the powers
            for counter in range(0, (user_num_int + 1)):
                power = counter * counter
                print("{}^2 = {}".format(counter, power))
                if counter > user_num_int:
                    break
    except:
        print("{} is not an integer!".format(user_num_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
