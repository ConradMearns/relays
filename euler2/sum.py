# Gotta find sum of all even fib nums

# starting with just a fib generator that stops under 4 million

fm = 4000000

a = 1
b = 2

total = 0

while(b < fm):
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



# running out of time. count is close but not accurate - messed up a and b
