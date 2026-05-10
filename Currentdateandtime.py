from datetime import date , time , datetime

# calling the today 
# function of date class
today = date.today()
now = datetime.now()
print("Today's date is", now)
print("\nCurrent Date and Time is", now)


# Printing date's componets
print("\nDate componets", today.year, today.month, today.day)