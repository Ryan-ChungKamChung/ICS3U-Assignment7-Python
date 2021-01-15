#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program generates random numbers and checks for matches with user input


import random

import constants


def match(random_numbers, number):
    # Checks if there are any matches

    for single_element in random_numbers:
        if number == single_element:
            match = 1
            break
        else:
            match = 0

    return match


def main():
    # Generates random numbers and displays a match

    random_numbers = []

    print("I check if your number matches a number in ",
          "a random list of elements!")

    for loop_counter in range(0, constants.NUMBER_OF_ELEMENTS):
        random_numbers.append(random.randint(1, 100))

        if loop_counter < constants.NUMBER_OF_ELEMENTS - 1:
            print(random_numbers[loop_counter], end=", ")
        else:
            print(random_numbers[loop_counter], '\n')

    while True:
        number_string = input("Number to check: ")
        try:
            number = int(number_string)
            break
        except Exception:
            print("This isn't a valid input")

    match_number = match(random_numbers, number)

    if match_number == 1:
        print("Your number matches at least one element in the list!")
    else:
        print("Your number does not match any number in the list!")


if __name__ == "__main__":
    main()
