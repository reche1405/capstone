"""

Check what type of calculation the user would like to run


if the usser wants to check an investemnt:
    ask for the deposit amount
    interest rate and divide by 100
    years investing 
    and which interest type they are using.
    if the investment is simple:
        use A = P(1 + r * x)
    else:
        use A = P(1 + r)^t

    print the total return value of the investment.

otherwise if the user wants to check their bonds
    ask house value in pounds
    ask for interest rate
    ask for how many months the repayment schedule is
    ask what the yearly interest rate is and convert to decimal and devide by 12
    calculate the monthly repayments with (i * P)/(1 - (1 + i) ** (-n))
    
    print the monthly repayments

"""


import math 

intro_msg1 = "investment - to calculate the amount of interest you'll earn on your investment"
intro_msg2 = "bond - -to calculate the amount you'll have to pay on the home loan"
print(intro_msg1)
print(intro_msg2)
print(" ")
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").upper()

if option == 'INVESTMENT':
    deposit_amount = int(input("Deposit amount (£): "))
    interest_rate = int(input("Interest rate (%):"))/ 100
    years_invested = int(input("How many years will you invest: "))
    interest_type = input("please enter 'simple' or 'compound' for your interest type: ").lower()
    if interest_type == 'simple':
        total_return = f"Your total return is: £{round(deposit_amount * (1 + interest_rate * years_invested), 2)}"
    elif interest_type == 'compound':
        total_return = f"Your total return is: £{round(deposit_amount * math.pow((1+ interest_rate), years_invested), 2)}"
    else: 
        total_return = "invalid option."
    print(total_return)
elif option == "BOND":
    house_value = int(input("House value: "))
    interest_rate = int(input("Interest rate (integer): "))/ 100
    repayment_months = int(input("Months repaying: "))
    interest_rate = interest_rate / 12
    monthlyl_repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-repayment_months))
    print(f"Your monthly repayments are: £{round(monthlyl_repayment, 2)}")

