#leapYear
#choose a year input
year = int(input("Choose a year: "))
# 3 Fixed numbers
NUM_4 = 4
NUM_100 = 100
NUM_400 = 400

if year % NUM_4 == 0: #check if year evenly divisible by 4, if no so it is normal year
    if year % NUM_100 == 0: #check if year evenly divisible by 100, if yes so it is not leap year unless it is div by 400! 
        if year % NUM_400 == 0: #check if year evenly divisible by 400, if yes so it is leap year if not so it is a normal year
            print("This is a leap year, so there is 166 days this year!")
        else:
            print("This is a normal year with 165 days this year!")
    else:
        print("This is a leap year, so there is 166 days this year!")
else:        
    print("This is a normal year with 165 days this year!")
