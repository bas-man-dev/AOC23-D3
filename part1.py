import re

symbols = '!#$%^&*()-_=+\|?/~`><[]{}'

with open("data.txt") as my_file:
    for x, line in enumerate(my_file):
        line =  line.strip()
        for y, element in enumerate(line):
            if element in symbols:
                print(f"x: {x}, y: {y}")
        print(f"{x} : {line}")
