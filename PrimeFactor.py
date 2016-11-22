#https://projecteuler.net/problem=3
def is_prime(a):
    return all(a % i for i in xrange(2, a))

max = 0
z = 600851475143
y = 600851475143 // 2
for x in xrange(2,y):
    #print is_prime(x)
    if is_prime(x) and z%x == 0:
        print x
        max = x
print max
