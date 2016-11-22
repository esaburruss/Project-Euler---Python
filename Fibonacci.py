#https://projecteuler.net/problem=2
x = 0
y = 1
sum = 0
while y < 4000000:
    t = x + y
    if t > 4000000:
        break
    x = y
    y = t
    if y % 2 == 0:
        sum += y
print sum
