# Python program to calculate gross salary of an employee for the following allowance:
# DA = 25% of Basic,
# HRA = 15% of Basic,
# PF = 12% of Basic,
# TA = 7.50% of Basic.
# Net Pay = Basic + DA + HRA + TA
# Gross Pay = Net Pay – PF


basic_salary=int(input("Enter basic pay: "))
DA=(25/100)*basic_salary
HRA=(15/100)*basic_salary
PF=(12/100)*basic_salary
TA=(7.50/100)*basic_salary
NetPay = basic_salary+DA+HRA+TA+PF
GrossPay=NetPay-PF

print(f"Basic salary is {basic_salary}\nNet pay is {NetPay}\n and Gross pay is {GrossPay}")
