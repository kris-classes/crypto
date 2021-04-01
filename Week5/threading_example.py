"""
HTCS6702 Cryptography - Kris Pritchard / @krp

This file shows a simple example of how we use threads so that our programs can use concurrency.
"""
import fire
import threading
import time


def slow_function():
    print('This function takes 5 seconds to run.')
    time.sleep(5)  # Make the function sleep for 5 seconds


def slow_functions_without_threads():
    print('Running slow_function 4 times without using threads.')
    for i in range(4):
        print(f'Running slow_function: {i+1}')
        slow_function()
    print('This should take 20 seconds to finish.')


def slow_functions_with_four_threads():
    print('Running slow_function 4 times using threads (concurrency)')
    for i in range(4):
        print(f'Running slow_function: {i+1}')
        t = threading.Thread(target=slow_function)
        t.start()
    print('This should take 5 seconds to finish.')


def slow_functions_with_forty_threads():
    print('Running slow_function 40 times using threads (concurrency)')
    for i in range(40):
        print(f'Running slow_function: {i+1}')
        t = threading.Thread(target=slow_function)
        t.start()
    print('This should take 5 seconds to finish.')


# You don't need to change below this line.
if __name__ == '__main__':
    fire.Fire(name='threading_example')
