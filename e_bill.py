mon_arr = ["January","February","March","April","May","June","July","August","September","October","November","December"]
input_decider = int(input(""" Select Input method
                          press 1 for month wise input
                          press 2 for annual input
                          :>"""))
units=[]
if input_decider ==1:
    for i in range(12):
        value = input(f"Enter the electricity bill for {mon_arr[i]} :> ")
        units.append(value)
elif input_decider == 2:
    units = list(map(int,(input("Enter the electricity bill for all months:> ").split())))
bill=0

#FUNCTION FOR BILL CALCULATION:

def cal_bill(a):
    if a>=0 and a<=100:
        bill = 3*a
    elif a>100 and a<=300:
        bill = ((100*3) + (5*(a-100)))
    else:
        bill = (((100*3) + (5*200))+(7*(a-300)))
    if bill > 1500:
        bill = bill + (0.10 * bill)

    return bill
amounts=[]

#CALCULATE PRICE PER UNITS

for i in range(12):
    unis = int(units[i])
    val = cal_bill(unis)
    amounts.append(val)

#CALCULATE ANNUAL BILL:

sum =0
for i in range(12):
    sum = sum+amounts[i]
#PRINT MONTHS WISE BILL
for i in range(12):
    print(f"{mon_arr[i]} = {amounts[i]}")

#PRINT ANNUAL BILL

print("ANNUAL BILL => ",sum)

#PRINT FLAGGED MONTHS

print("FLAGGED MONTHS :>")
avg_consumption = (sum/12)
for i in range(12):
    mon_bill = amounts[i]
    if mon_bill>(1.5*avg_consumption):
        print(mon_arr[i])
