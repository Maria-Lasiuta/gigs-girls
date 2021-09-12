'''Question 11
Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy.'''

from random import uniform

random_number = uniform(1, 10)
print(round(random_number, 2))
