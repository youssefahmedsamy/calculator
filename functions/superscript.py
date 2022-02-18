def superscript(x):
    normal = "0123456789+-=()."
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾·"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)