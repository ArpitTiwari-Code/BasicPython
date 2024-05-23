def compound_interest(principal, rate, time):
    """
    Calculate compound interest.
    """

    amount = principal * (1 + rate) ** time
    return amount - principal

principal = float(input("enter principal amount")
rate = float(input("enter rate of interest")
time = float(input("enter time period")
ci = compound_interest(principal, rate, time)
print("Compound Interest:", ci)

