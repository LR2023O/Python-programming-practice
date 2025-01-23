citizenship = input("Enter your Citizenship :")
age = int(input("Enter age :"))
if (citizenship in ["Kenyan","Ugandan","Tanzanian"] and age>=18):
    print("Your eligible to vote")
else:
    print("You are not eligible to vote")
