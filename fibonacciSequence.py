"""
Author: Lani Hurley
Date: 3/30/22
Filename: fibonacciSequence.py
Python program takes user input and displays the Fibonacci sequence starting from 0 up to nth-term desired.
"""
# input the number of terms desired
nthTerm = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
# accumulator variable
count = 0

# check if the number of terms is valid
if nthTerm <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nthTerm == 1:
    print("Fibonacci sequence up to", nthTerm, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nthTerm:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
