def fractofloat(frac_str):
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