# Printing True for Leap year And False for non-leap Year
def is_leap(year):
    leap = False
    if year%100==0 and year%400==0: 
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True
    return leap

year = int(input("Enter the Year:"))
leap_year=is_leap(year)
print(leap_year)