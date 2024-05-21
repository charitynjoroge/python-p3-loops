#!/usr/bin/env python3

def happy_new_year():
    for countdown in range(10, 0, -1):
        print(countdown)
    print("Happy New Year!")


happy_new_year()


def square_integers(nums):
    squared_nums = [num ** 2 for num in nums]
    return squared_nums


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    
