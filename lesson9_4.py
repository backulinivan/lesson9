from fractions import Fraction
def recurr(g):
    if g==1:
        return 4
    if g==2:
        return 4.25
    if g==3:
        xn_1 = Fraction(4, 1)
        xn_2 = Fraction(17, 4) 
        return 108 - Fraction((815 - Fraction(1500, xn_1)), xn_2)
    return 108 - Fraction((815 - Fraction(1500, recurr(g-2))), recurr(g-1))
f=recurr(int(input()))
print(f,eval(str(f)))
print(type(f))
