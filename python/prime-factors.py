def prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"

prime_factors(100)