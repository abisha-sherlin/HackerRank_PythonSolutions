def product(fracs):
    t = reduce(lambda a,b:a*b,fracs)
    return t.numerator, t.denominator
