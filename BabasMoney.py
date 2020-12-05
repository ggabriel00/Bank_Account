p = float(input("What's the principle? "))
r = float(input("What's the rate? "))
n = float(input("How many periods? "))
t = float(input("How many payments per period? "))
pv = p * (pow((1 + r/100/n),n*t))

print (pv)
