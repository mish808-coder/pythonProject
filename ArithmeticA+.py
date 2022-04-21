x = 10 **3
print (x)
y = 10/3
print(y)
z = 10//3
print(z)
w = 10 - 8 * 2 + 9
print (w)
p = 2.9
print(round(p))
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))

price = 10**6
good_credit = True
if good_credit:
    print(10/100 * (price))
else:
    print(20/100 * (price))

price = 10**6
good_credit = True
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')

high_income = False
good_credit = True
if high_income or good_credit:
    print(' Eligible for credit')

name = 5
if name <3 :
    print('name must be atleast 3 characters')
elif name >= 50 :
    print('name can be a maximum of 50 characters')
else:
    print('name looks good')

name = 'prudence'
print(len(name))
if len(name)< 3:
    print(' name must ba atleast 3 characters long ')
elif len(name) >=50:
    print(' name must be a maximum of 50 characters ')
else:
    print(' name looks good !')

i = 1
while i <= 5:
    print(i)
    i = i+1
print('berry')
i = 1
while i<= 5:
    print('*' *i )
    i = i + 1
print('veges')

