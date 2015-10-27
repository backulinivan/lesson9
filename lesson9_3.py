from decimal import Decimal, getcontext
getcontext().prec = 4


def monthlyPayment(S, x, y):
    summ = 0
    for i in range(y*12+1):
        summ += (1 + x/1200)**i
    payment = Decimal(S)*Decimal((1+x/1200)**(y*12))/Decimal(summ)
    return(payment)
    
def overPayment(monthly_payment, yrs, money):
    return(monthly_payment*yrs*12 - Decimal(money))    
    
Summ = input()
plusEveryYear = int(input())
years = int(input())
pay = monthlyPayment(Summ, plusEveryYear, years)
print(pay)
print(overPayment(pay, years, Summ))       
