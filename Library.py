bookID = int(input("Book ID: "))
dueDate = int(input("Due Date: "))
returnDate = int(input("Return Date: "))
dayOverdue = returnDate-dueDate
if dayOverdue <= 7:
    fineRate = dayOverdue*20
    print("Fine due = ",fineRate)
elif dayOverdue >=8:
     fineRate = dayOverdue*50
     print("Fine due = ",fineRate)
elif dayOverdue >14:
     fineRate = dayOverdue*100
     print("Fine due = ",fineRate)
else:
    print("No Fine")
print("Overall")    
print("Book ID: ",bookID)
print("Due date: ",dueDate)
print("Return date: ",returnDate)
print("Fine rate: ",fineRate )

    
    
