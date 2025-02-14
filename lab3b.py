#!/usr/bin/env python3

# Author ID: pramish kc  

def sum_numbers(number1, number2):
    # This function adds number1 and number2 and returns the value
    return number1 + number2

def subtract_numbers(number1, number2):
    # This function subtracts number2 from number1 and returns the value
    return number1 - number2

def multiply_numbers(number1, number2):
    # This function multiplies number1 and number2 and returns the value
    return number1 * number2

if __name__ == '__main__':
    # The main part of the script calls the functions and prints the results
    print(sum_numbers(10, 5))  # Expected output: 15
    print(subtract_numbers(10, 5))  # Expected output: 5
    print(multiply_numbers(10, 5))  # Expected output: 50
