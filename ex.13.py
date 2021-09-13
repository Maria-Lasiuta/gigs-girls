#13.Write a program that asks the user to enter an angle in
#degrees and prints out the sine of that angle.

from math import *
deg=float(input('Enter an angle in degrees: '))
radians=radians(deg)
print('sin angle =',sin(radians))
