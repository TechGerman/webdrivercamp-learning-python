#!/usr/bin/python3

def fizz_buzz():
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' ')
        elif number % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(number, end=' ')


fizz_buzz()
