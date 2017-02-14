def modular_pow(base, exponent, modulus):
    if exponent == 0: return 1
    else:
        result = modular_pow(base, exponent/2, modulus)
        result = (result*result) % modulus
        if (exponent % 2 == 1):
            result = (result*base) % modulus
        return result

exp = int(raw_input())

print modular_pow(3,exp,2147483647)
