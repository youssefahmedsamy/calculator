from math import factorial
from fractions import Fraction

def combinate(a, b):
    nominator = float(1)
    denominator = float(1)
    x = a
    for c in range(int(b)):
        nominator = nominator * x
        x -= 1
    denominator = factorial(int(b))
    floaty = deczeros(str(float(nominator / denominator)))
    retfract = str(Fraction(floaty).limit_denominator(1000))
    if retfract == floaty:
        return floaty
    retstr = str(floaty + " or " + retfract)
    return retstr

if __name__ == "__main__":
    from deczeros import deczeros
    import sys
    print(combinate(float(sys.argv[1]), int(sys.argv[2])))
else:
    from functions.deczeros import deczeros