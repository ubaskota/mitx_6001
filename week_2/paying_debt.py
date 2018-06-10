

def monthly_payment(balance, annual_rate):
    
    fixed_min = 0
    monthly_balance = balance
    
    while (unpaid_balance > 0):
        
        for i in range(12):
            
            unpaid_balance = balance - fixed_min
            interest = unpaid_balance * annual_rate/12
            total_balance = unpaid_balance + interest
            monthly_balance = total_balance
        
        if total_balance <= 0:
            return fixed_min
        else:
            fixed_min = fixed_min + 10

print(monthly_payment(balance, annualInterestRate))
