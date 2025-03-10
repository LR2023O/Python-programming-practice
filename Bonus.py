#Bonus
salary = int(input("Enter your salary: "))
time = int(input("Enter years of service: "))
if time > 10:
    bonus = salary*(10/100)
    total = salary+bonus
    print("your net bonus amount is: ",bonus)
    print("your total salary is: ",total)
elif time >=6 and time<=10:
    bonus = salary*(8/100)
    total = salary+bonus
    print("your net bonus amount is: ",bonus)
    print("your total salary is: ",total)
else:
    bonus = salary*(5/100)
    total = salary+bonus
    print("your net bonus amount is: ",bonus)
    print("your total salary is: ",total)
    
