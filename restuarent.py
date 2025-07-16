bill amount = float(input("enter total_bill_amount"))
tip_percent = int(input("enter tip_percentage(10 t0 50):"))
friends = int(input("enter the number of friends to slit the bill "))
if tip_percent ,10 or tip_percent>50:
print("tip percent is betwen 10 and 50")
else:
tip_amount = (tip_percent/100)*bill amount
total_bill = bill amount+tip_amount
eah_person = total_bill/friends
print("\n---bill sumarry---")
print(f"bill amount : {bill_amount:.2f}")
print(f"tip({tip_percnt}%):{tip_amount:.2f}")
print(f"total with tip:{total_bill:.2f}")
print(f"each person share:{each_person:.2f}")
