print("welcome to the tip calculator")
bill= float(input ("What was the total bill? "))
people= int(input("how many people were there? "))
tip = float(input (" what percentage would you like to tip? "))

tip_by_percent= tip/100
print(tip_by_percent)
total_bill= (bill)+(bill*tip_by_percent)
print(total_bill)
split_bill= total_bill/people
final_amount= round(split_bill, 2)
print ("each person owes:", final_amount)
