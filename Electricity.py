#Electricity Bill
customerID = input("Enter customer ID: ")
customer_name = input("Customer Name: ")
units = float(input("Enter units consumed: "))
if units <=199:
    charge =1.20
elif units >=200 and units <400:
    charge = 1.50
elif units >=400 and units <600:
    charge = 1.80
else:
    charge = 2.00
    
total=units*charge
if total >400:
    surcharge= total*0.15
    total +=surcharge

if total <100:
    total = 100

print("\nElectricity Bill Summary")
print(f"Customer ID: ",customerID)
print(f"Customer Name: ",customer_name)
print(f"Units consumed: ",units)
print(f"Charges per Unit: Ksh.",charge)
print(f"Total amount due: Ksh.",total)
