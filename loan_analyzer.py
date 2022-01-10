# coding: utf-8
import csv
from pathlib import Path

### Print the header for the assignment
print("===")
print("Challenge 1 - Loan Analyzer")
print("By Kevin BaRoss")
print("===")

### Part 1: Automate the Calculations.
print("Part 1: Automate the Calculations")

# List of loan costs
loan_costs = [500, 600, 200, 1000, 450]

# Find the number of loans in the list
number_of_loans = len(loan_costs)
print(f"There are a total of {number_of_loans} loans in the list.")

# Find the total value of the loans
total_value_of_loans = sum(loan_costs)
print(f"The total value of loans is ${total_value_of_loans}.")

# Find the average loan amount from the list
average_loan_amount = total_value_of_loans/number_of_loans
print(f"The average loan amount is ${round(average_loan_amount,2)}.")
print("===")

### Part 2: Analyze Loan Data.
print("Part 2: Analyze Loan Data")

# The loan data to be used in the calculation for part 2
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Calculate the future value of the loan
future_value_of_loan = loan.get("future_value")
print(f"The future value of the loan is ${future_value_of_loan}.")

# Calculate the remaining month of the loan
remaining_month_of_loan = loan.get("remaining_months")
print(f"The remaining months of the loan is {remaining_month_of_loan} months.")
print("---")

# Calculate the fair value of the loan with the annual discount rate of 20%
annual_discount_rate = 0.20
fair_value_of_loan = future_value_of_loan / (1 + annual_discount_rate/12) ** remaining_month_of_loan
print(f"The fair value of the loan is ${round(fair_value_of_loan,2)}.") 

# The conditional statement to determine whether the loan is really worth. In other words, does it make sense to buy this loan at its cost?
Loan_price_to_compare = loan.get("loan_price")
print(f"The cost of the loan is ${Loan_price_to_compare}.")
if fair_value_of_loan >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")
print("===")

### Part 3: Perform Financial Calculations.
print("Part 3: Perform Financial Calculations.")

# The loan data to be used in the calculation for part 3
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# A new function that will be used to calculate present value.
def calculate_present_value(future_value,remaining_months,annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return(round(present_value,2))

# Use the function to calculate the present value of the new loan given below.
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
annual_discount_rate = 0.2

present_value = calculate_present_value(future_value,remaining_months,annual_discount_rate)
print(f"The present value of the loan is: {present_value}")
print("===")

### Part 4: Conditionally filter lists of loans.
print("Part 4: Conditionally filter lists of loans.")

# The loan data to be used for calculation in part 4
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Append the loan that cost $500 or less to the `inexpensive_loans` list
for item in loans:
    loan_to_compare = item["loan_price"]
    if(loan_to_compare<=500):
       inexpensive_loans.append(item)

# Print the `inexpensive_loans` list
print("The loans that cost $500 or less is as follows:")
print(inexpensive_loans)

print("===")

### Part 5: Save the results

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")
with open(output_path, 'w', newline='') as csvfile:
    
# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())