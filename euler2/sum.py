# Gotta find sum of all even fib nums

# starting with just a fib generator that stops under 4 million

fm = 4000000

a = 1
b = 2

total = 0

while(a <= fm):
    # add number if even
    print('consider')
    print(a)
    if ((a % 2) == 0):
        total += a
        print('summing')
        print(a)
    # update a and b
    c = a + b
    a = b
    b = c

print(total)


#r1#
# running out of time. count is close but not accurate - messed up a and b

#r2#
#problem is that we miss 1346269 + 2178309 < 4000000 because of how
#the while statement was made. i replaced while b "blah" with while a "blah"
#
