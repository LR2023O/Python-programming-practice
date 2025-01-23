#Discount Program
amount = int(input("Enter amount:"))
if (amount>=5000):
    discount=amount*0.1
    print("Discount",discount)
    final_amount=amount-discount
    print("Final amount=",final_amount)
elif (4999>amount>1000):
    discount=amount*0.05
    print("Discount",discount)
    final_amount=amount-discount
    print("Final amount=",final_amount)
else:
    print("No discount")
    print("Final amount=",amount)

                                                  
