#!/usr/bin/python3
from math import factorial
from fractions import Fraction
#from combinates import combinate

import os
import sys

dir = os.path.join(os.path.dirname(__file__))
dir = dir.replace('./', '')
funcdir = dir + "/../"
print(funcdir)
sys.path.append(funcdir)
from functions.combinates import combinate
from functions.fractofloat import fractofloat
from functions.deczeros import deczeros



discontinue = int(0)
i = int(1)


def get_super(x):
    normal = "0123456789+-=()."
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾·"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


def get_sub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)





print("Welcome to the combinates calculator. Please note that the combinate structure is denoted by: ⁿCᵣ where n and "
      "r are numbers you input. Please not that n can be a real number while r is an integer and r > 0."
      "\nEnter 'e' at any time to exit")

while discontinue == 0:
    if i == 1:
        print("ⁿCᵣ")
        print("Please go ahead and enter n: ")
        n = fractofloat(input("n = "))
        i += 1
    elif i == 2:
        print("\nPlease go ahead and enter r: ")
        ntostr = deczeros(str(n))
        print('{}Cᵣ'.format(get_super(ntostr)))
        r = int(float(input("r = ")))
        rtostr = str(r)
        print("\n----------\nAnswer:\n")
        print('{}C{} = {}'.format(get_super(ntostr), get_sub(rtostr), combinate(n, r)))
        print("\n----------\n")
        i = 1
    elif i == -1:
        discontinue = 1