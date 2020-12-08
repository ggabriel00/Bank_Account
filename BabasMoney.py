
"""
p = principal
r = rate
n = num of compound periods
t = num of years
balance = total @ the end time
earnings = total amount earned
roi = return on investment

"""
def compound_interest():
    p = float(input("How much is your present value? $"))
    r = float(input("What's the rate? "))
    n = float(input("How many periods per years? "))
    t = int(input("How many years? "))
    balance = p * (pow((1 + r/100/n),n*t))
    earnings = balance - p
    roi = earnings / balance * 100
    
    print("You earned $", round(earnings,2),"during the ",t," year period. ")
    print("Balance at the end of the period  = $", round(balance,2))
    print("This is a ",round(roi,2),"% return on investment")

compound_interest()


