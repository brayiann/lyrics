import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Wait wait", 0.08),
        ("I wana jammin' with you", 0.06),
        ("I wanna sing for you ", 0.06),
        ("Gettig in trouble with you", 0.06),

        ("I really miss your perfume ", 0.09),
        ("No digas nada", 0.06),

        ("(sh)", 0.08),
        ("Be quiet", 0.08),
        ("Now i will tell you the truth", 0.08),
        ("Como si nada", 0.07),
        ("I really miss you i do", 0.08),
        ("Uhh", 0.08),

    ]

    delays = [0.2, 0.1, 0.1, 0.1,
              0.1, 0.1, 
              1.4, 0.8, 0.4, 0.9, 0.5, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()