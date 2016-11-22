#https://projecteuler.net/problem=4
def is_palindrome(num):
    x = str(num)[::-1]
    if int(x) == num:
        return True
    else:
        return False

max = 0
for i in range (100,999):
    for j in range (100,999):
        x = i*j
        if is_palindrome(x) and x > max:
            max = x
print max
