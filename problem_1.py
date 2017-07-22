# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_brute():
    total = 0
    for i in range(0, 1000):
        r3 = i % 3 == 0
        r5 = i % 5 == 0
        if r3 or r5:
            total += i
    return total

def multiples_sum():
    return sum(x for x in range(0,1000) if x % 3 == 0 or x % 5 == 0)

def multiples_reduce():
    return reduce(lambda x,y: x+y, [x for x in range(0,1000) if x % 3 == 0 or x % 5 == 0])

def multiples_range():
    return sum(set(range(0,1000,3) + range(0,1000,5)))


if __name__ == '__main__':
    print multiples_brute()
    print multiples_sum()
    print multiples_reduce()
    print multiples_range()
