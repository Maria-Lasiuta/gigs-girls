'''Question
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn'''

n = int(input('Введіть ціле число: '))
nn = n * 11
nnn = n * 111
print(n + nn + nnn)
