#x is the number and s is the suffix
def getordinalsuffix(x):
    x = int(x)
    if len(str(x)) >= 1:
        if int(str(repr(x)[-1])) == 1:
            s = str("st")
        elif int(str(repr(x)[-1])) == 2:
            s = str("nd")
        elif int(str(repr(x)[-1])) == 3:
            s = str("rd")
        else:
            s = str("th")
    if len(str(x)) >= 2:
        if int(str(repr(x)[-2] + repr(x)[-1])) in (11, 12, 13):
            s = str("th")
    return s