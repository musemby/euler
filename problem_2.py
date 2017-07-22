# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci():
    starter, new, even_sum = (1,2), 0, 2
    while new < 4000000:
        new = starter[0] + starter[1]
        starter = starter[1], new
        if new % 2 == 0:
            even_sum += new
    return even_sum
