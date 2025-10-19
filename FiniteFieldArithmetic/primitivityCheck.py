from utils import Poly, get_prime_factors

def primitivity_check(f: Poly, integer_modulus: int, polynomial_modulus: Poly) -> bool:
    p = len(polynomial_modulus)
    order = integer_modulus**(p - 1) - 1
    primeFactors = get_prime_factors(order)
    for i in primeFactors:
        power = order // i
        temp = f[:]
        while power > 0:
            if power % 2 == 0:
                temp = finite_field_multiply(temp, temp, integer_modulus, polynomial_modulus)
                power //= 2
            else:
                temp = finite_field_multiply(temp, f, integer_modulus, polynomial_modulus)
                power -= 1
        if temp == [1]:
            return False
    return True


        