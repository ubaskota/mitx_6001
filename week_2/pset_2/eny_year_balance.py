

def end_year_balance(balance, interest, monthly_payment):
    
    for i in range(12):
        minimum_payment = balance * monthly_payment
        unpaid_balance = balance - minimum_payment
        total_unpaid_balance = unpaid_balance + (interest/(12)) * unpaid_balance
        balance = total_unpaid_balance
    
    return round(total_unpaid_balance, 2)

print(end_year_balance(balance, annualInterestRate, monthlyPaymentRate))
