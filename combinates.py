#!/usr/bin/python3
from math import factorial
from fractions import Fraction

discontinue = int(0)
i = int(1)


def uselessdecimalzeros(x):
    if "." in x:
        while not x.endswith("."):
            if x.endswith("0"):
                x = x[:-1]
            else:
                break
        if x.endswith("."):
            x = x[:-1]
    return x


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


def combinate(a, b):
    nominator = float(1)
    denominator = float(1)
    x = a
    for c in range(int(b)):
        nominator = nominator * x
        x -= 1
    denominator = factorial(int(b))
    floaty = uselessdecimalzeros(str(float(nominator / denominator)))
    retfract = str(Fraction(floaty).limit_denominator(1000))
    if retfract == floaty:
        return floaty
    retstr = str(floaty + " or " + retfract)
    return retstr


def parseNumber(frac_str):
    if frac_str == "e":
        global i
        i = -2
    else:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split('/')
            try:
                leading, num = num.split(' ')
                whole = float(leading)
            except ValueError:
                whole = 0
                frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac


print("Welcome to the combinates calculator. Please note that the combinate structure is denoted by: ⁿCᵣ where n and "
      "r are numbers you input. Please not that n can be a real number while r is an integer and r > 0."
      "\nEnter 'e' at any time to exit")

while discontinue == 0:
    if i == 1:
        print("ⁿCᵣ")
        print("Please go ahead and enter n: ")
        n = parseNumber(input("n = "))
        i += 1
    elif i == 2:
        print("\nPlease go ahead and enter r: ")
        ntostr = uselessdecimalzeros(str(n))
        print('{}Cᵣ'.format(get_super(ntostr)))
        r = int(float(input("r = ")))
        rtostr = str(r)
        print("\n----------\nAnswer:\n")
        print('{}C{} = {}'.format(get_super(ntostr), get_sub(rtostr), combinate(n, r)))
        print("\n----------\n")
        i = 1
    elif i == -1:
        discontinue = 1
