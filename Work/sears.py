bill_thickness = 0.11 * 0.001  # metres (0.11 mm)
sears_height = 442  # height (metres)

day = 1
num_bills = 1
bills_height = 0.11

while bills_height < sears_height:
    print(day, num_bills, bills_height)
    day = day + 1
    num_bills = 2 * num_bills
    bills_height = num_bills * bill_thickness

print('No. of days:', day) 
print('No. of bills:', num_bills)
print('Final bills height:', bills_height) 
