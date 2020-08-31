from time import sleep

question = '''
Problem Statement\n
In a given election involving fve candidates: Alice, Bob, Carol, Dave and Eli, a sample of votes
were tabulated from ten diﬀerent polling points as follows:
'''


table ='''
TABLE________________________________\n
Alice = 10 92 23 17  2 44 33 41 19 54
Bob   = 21 91 10  9 12 21 52 18 34 78
Carol = 10 81  8 28 53 53 10 11 40 36
Dave  = 48 12 40 30 33 37 81 29 28 32
Eli   = 12  9 21 44 13 17 21 34 33 62
_____________________________________
'''

directive = '''
Given the formula for computing margin of error above, write a program to obtain the vote shares
for each of the candidates (as a percentage of all votes cast) and compute the margin of error for
each of those estimates correct to two decimal places
'''

print(question)
sleep(1.5)
print(table)
sleep(1.5)
print(directive)
sleep(1.8)
print('The Proposed Solution for the PVT question is :')
sleep(1.5)

