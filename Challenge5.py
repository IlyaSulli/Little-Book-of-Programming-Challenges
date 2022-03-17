import datetime
DOB = input("What is your date of birth (DD/MM/YYYY)? ")
DOB = DOB.split("/")
# DOB = [string of day , string of month , string of year]
DOB[0] = int(DOB[0])
DOB[1] = int(DOB[1])
DOB[2]= int(DOB[2])
#Datetime is in format YYYY-MM-DD
today = datetime.date.today()
birthday = datetime.date(DOB[2],DOB[1],DOB[0])
difference = today - birthday
print("You have been alive for",difference.days,"days")
