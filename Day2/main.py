print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
perc_tip = int(input("What percentage tip would you like to give?"))
num_ppl = int(input("How many people to split the bill?"))

each_bill = (total_bill + (total_bill*perc_tip/100))/num_ppl
each_bill_final = round(each_bill, 2)

print(f"Each person should pay: {each_bill_final}")