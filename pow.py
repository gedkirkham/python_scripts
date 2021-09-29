def power(base, exponent):
    ans = base

    if exponent > 1:
        ans = base * base
        exponent -= 1

        while exponent > 1:
            ans = ans * base
            exponent -= 1

    print(f'Answer: {ans}\n')


while True:
    print('Power calculator.')
    base = int(input('Base: '))
    exponent = int(input('Exponent: '))
    power(base, exponent)
