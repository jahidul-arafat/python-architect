# This is a sample Python script.
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # print a greeting message to the user
    print(f'Hi, {name}!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # poor way to do it
    for number in range(2, 101):
        hasFactor = False
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                hasFactor = True
        if not hasFactor:
            print(f'{number} is prime')


    
