"""patterns for losers"""

import math


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '=' * int(percent) + '-' * (100 - int(percent))
    print(f"\r[{bar}] {percent:.2f}%", end="\r")

numbers = [x * 5 for x in range(2000, 3000)]
results = []


def p1(d):
    o = int(input("[+] Enter the number of lines for the pattern: "))
    for i in range(o):
        for x in range(i + 1):
            print(i, end=" ")
        print()
    
def p2(c):
    o = int(input("[+] Enter the number of lines for the pattern: "))
    for i in range(o):
        for j in range(i, o):
            print(i, end = " ")
        print()

def p3(d):
    o = int(input("[+] Enter the number of lines for the pattern: "))
    for i in range(o-1):
        for j in range(i, o):
            print('', end = '')
        for j in range(i):
            print(i, end = '')
        print()
    for i in range(o):
        for j in range(i+1):
            print('', end = '')
        for j in range(i, o-1):
            print(i, end = '')
        print()
    
def p4(d):
    o = int(input("[+] Enter the number of lines for the pattern: "))
    for i in range(o):
        p = 1
        for j in range(i, o):
            print('', end = '')
        for j in range(i):
            print(p, end = '')
            p += 1
        for j in range(i+1):
            print(p, end = '')
            p += 1
        print()

def dph(d):
    o = 5
    for i in range(o):
        if i == 0 or i == o - 1:
            print('*' * o)
    else:
        print('*' + ' ' * (o - 2) + '*')

def test(d):
    n = 5
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    for i in range(n - 1):
        for j in range(i + 1):
            print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()