def p(bill_amount, amount_amount):
    due = bill_amount - amount_amount
    return max(due,0)

Bill=int(input("Enter the bill amount: "))
payment=int(input("Enter the payment amount: "))

due = p(Bill,payment)
print((f"The total to be paid is: {due}"))


