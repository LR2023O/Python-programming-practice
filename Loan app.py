print("Loan Application")
age = int(input("Please enter your age: "))
income = int(input("Enter your annual income: "))
if (age >= 21 and income >= 21000):
    print("Congratulations! You qualify for the loan. ")
else:
    print("Unfortunately, we are unable to offer you a loan at this time.")
