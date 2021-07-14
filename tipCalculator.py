bill_amount = float(input("What's the amount you've payed?"))
nr_people_splitting_bill = int(input("How many people share the bill?"))
tip = int(input("Choose tip: 10, 15 or 20 percent?"))
amount_of_tip = tip * bill_amount /100
total_amount = bill_amount + amount_of_tip
to_pay_by_person = total_amount / nr_people_splitting_bill
to_pay_by_person_rounded = round(to_pay_by_person,2)

print(f"One person needs to pay {to_pay_by_person_rounded}")
