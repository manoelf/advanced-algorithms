#https://www.urionlinejudge.com.br/judge/pt/problems/view/1807



def modular_pow(base, exponent, modulus):
    if exponent == 0: return 1
    else:
        result = modular_pow(base, exponent/2, modulus)
        result = (result*result) % modulus
        if (exponent % 2 == 1):
            result = (result*base) % modulus
        return result

line = int(raw_input())
print modular_pow(3, line,2147483647)
