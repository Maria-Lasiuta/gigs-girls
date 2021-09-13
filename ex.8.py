#8. Write a program that asks the user to
#enter three numbers: the day of birth, the month of birth and the year
#of birth (use three separate input statements).
#Print out the total number of days from birth.

from datetime import * 
day=int(input('Enter birthday:'))
month=int(input('Enter the month of birth:' ))
year=int(input('Enter year of birth:'))
d1=date(year,month,day)
today = date.today()
x=today-d1

print('Days from birth to today', x.days)
