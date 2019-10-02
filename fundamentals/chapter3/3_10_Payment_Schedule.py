listed_price = float(input("Enter the listed purchase price: "))
down_payment = 0.10 * listed_price
rate = 0.12
current_balance = listed_price - down_payment
monthly_payment = 0.05 * current_balance
interest_month = current_balance * rate / 12
principal_month = monthly_payment - interest_month

print("%10s%30s%28s%30s%30s%30s"%("Month","Current_Balance","Interest_Owed_Month","Principal_Owed_Month","Payment_Month","Balance_after_payment"))
i=0

def isEqualFloat(f1, f2):
    return abs(f1 - f2) <= 1e-5

while(isEqualFloat(current_balance, 0.0) != True):
    i+=1
    print("%10s%30s%28s%30s%30s%30s"%(i, round(current_balance,2), round(interest_month,2), round(principal_month,2), round(monthly_payment,2), round(current_balance,2) - round(monthly_payment,2)))
    current_balance -= principal_month
    interest_month = current_balance * rate / 12
    monthly_payment = 0.05 * current_balance
    principal_month = monthly_payment - interest_month

     