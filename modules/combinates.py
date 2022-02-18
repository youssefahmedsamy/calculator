import os
import sys
dir = str(os.path.join(os.path.dirname(__file__))).replace("./", '')
funcdir = str(dir.replace("modules", ''))
sys.path.append(funcdir)
from functions.combinates import combinate
from functions.fractofloat import fractofloat
from functions.deczeros import deczeros
from functions.superscript import superscript
from functions.subscript import subscript


print("Welcome to the combinates calculator. ⁿCᵣ: n ∈ R; r ∈ N.")

discontinue = int(0)
i = int(1)


def argparse(args):
    if ((type(args) != list) & (type(args) != tuple)):
        args = list(str(args).strip().split(" "))
    for i in range(len(args)):
        if args[i] == "exit":
            return -1


while discontinue == 0:
    if i == 1:
        print("ⁿCᵣ")
        print("Please go ahead and enter n: ")
        n = input("n = ")
        if argparse(n) == -1:
            i = -1
        else:
            n = fractofloat(n)
            i += 1
    elif i == 2:
        print("\nPlease go ahead and enter r: ")
        print('{}Cᵣ'.format(superscript(deczeros(str(n)))))
        r = input("r = ")
        if argparse(r) == -1:
            i = -1
        else:
            r = int(float(r))
            i = 1
            print("\n----------\nAnswer:\n")
            print('{}C{} = {}'.format(superscript(deczeros(str(n))), subscript(deczeros(str(r))), combinate(n, r)))
            print("\n----------\n")
    elif i == -1:
        discontinue = 1
