import math

# Ask user to choose if they want to calculate an Investment or a Bond
print("Choose either 'Investment' or 'Bond' from the menu below to proceed:\n")
print("investment       - to calculate the amount of interest you'll earn on interest")
print("Bond             - to calculate the amount you'll have to pay back on a home loan")

financial_calculation = input("Please enter either Investment or Bond? \n").lower()
 
# If user input is investments calculate either compound or simple interest of user input
if financial_calculation == "investment":
    investment_amount = (float(input("How much money would you like to invest? \n ")))
    interest_rate = (float(input("What is the interest rate?  \n ")))
    interest_time = (float(input("How many years do you plan on investing? \n")))
    interest = input("Wound you like compound or simple? \n").lower()
    interest_rate_formula = interest_rate / 100                                                         # Formula to take the interest rate and convert it into a percentage (Interest rate divided by 100)
    simple_interest = investment_amount * (1+interest_rate_formula*interest_time)                       # Formula to Calculate simple Interest (simple_interest =Investment_amount*(1+Interest_Rate*Interest_time) )                         
    compound_interest = investment_amount * math.pow((1+interest_rate_formula), interest_time)          # Formula to calculate the compound interest compound_interest = investmenr_amount* math.pow((1+interest)-rate, interest_time)
    if interest == "simple":
        print(round(simple_interest,2))
    else:
        print(round(compound_interest,2))
elif financial_calculation == "bond":
    house_value = float(input("What is the current value of the house? "))
    bond_interest_rate = float(input("What is the interest rate?  \n "))
    investment_months = float(input("how many months would you like to repay the bond? "))
    bond_interest = bond_interest_rate /100 /12
    monthly_repay = (bond_interest * house_value) / (1 - (1+bond_interest)**(-investment_months))
    print(math.ceil(monthly_repay))                                                                    # calculate the bond repayment x = (interest_rate*house_value)/(1 - (1+interest_rate)^(-interest_time))
else: 
    print("Please select either Investment or Bond to continue Further.")









