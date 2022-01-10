def deczeros(x):
    if "." in x:
        while not x.endswith("."):
            if x.endswith("0"):
                x = x[:-1]
            else:
                break
        if x.endswith("."):
            x = x[:-1]
    return x