from fractions import Fraction
def recurr(g):
    if g==1:
        return 4
    if g==2:
        return 4.25
    if g==3:
        xn_1=4
        xn_2=4.25
        return 108-Fraction(Fraction(815-Fraction(1500,Fraction(xn_1))),Fraction(xn_2))
    return 108-Fraction(Fraction(815-Fraction(1500,Fraction(recurr(g-2)))),Fraction(recurr(g-1)))
f=recurr(int(input()))
print(f,eval(str(f)))
