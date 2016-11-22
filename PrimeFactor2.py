#https://projecteuler.net/problem=3
#Better Solution that doesn't take hours

def is_prime(a):
    return all(a % i for i in xrange(2, a))

x = 600851475143 // 2
prime = False
while prime == False:
    if is_prime(x):
        prime = True
    x+=-1
print x
