# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = int(input('extra_payment_start_month: '))
extra_payment_end_month = int(input('extra_payment_end_month: '))
extra_payment = int(input('extra_payment: '))

current_month = 1
num_required_months = 0

while principal > 0:
    if  current_month >= extra_payment_start_month and current_month <= extra_payment_end_month:
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        remaining_principal = principal if principal > 0 else 0
        print(f'{current_month}, {total_paid:0.2f}, {remaining_principal:0.2f}')
    else:     
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
        remaining_principal = principal if principal > 0 else 0
        print(f'{current_month}, {total_paid:0.2f}, {remaining_principal:0.2f}')

    current_month = current_month + 1    
    num_required_months = num_required_months + 1

print(f'Total paid: {total_paid:0.2f}')
print(f'No. of months required to pay the mortgage: {num_required_months}')


