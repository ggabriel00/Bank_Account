p = float(input("What's the principle? "))
r = float(input("What's the rate? "))
n = float(input("How many periods? "))
t = float(input("How many payments per period? "))
pv = p * (pow((1 + r/100/n),n*t))

print (pv)

def compound_interest(p,r,n,t):
    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    print("Balance at the end of the period ", round(balance,2))
    print("Interest earned is ", round(ci,2))

compoun_interest(5000,10,12,5)


