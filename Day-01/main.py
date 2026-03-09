import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Program Started. Type '0' to stop.")
    while True:
        n_input = input("Enter the number: ").strip()
        n=int(n_input)
        if n == 0:
            print("shutting down")
            break
        if n % 2 != 0:
            print("Weird")
        elif n >=2 and n <=5:
            print("Not Weird")
        elif n >=6 and n <=20:
            print("Weird")
        elif n >20:
            print("Not Weird")