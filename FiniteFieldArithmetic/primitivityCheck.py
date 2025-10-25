from utils import Poly, get_prime_factors
from .finiteFieldMultiplication import finite_field_multiply

# Check if a polynomial is primitive in a finite field
def primitivity_check(f: Poly, integer_modulus: int, polynomial_modulus: Poly) -> bool:
    # A polynomial f is primitive if its order is equal to the order of the multiplicative group of the finite field
    if f == [0] or f == [] or f == None:
        return False
    
    p = len(polynomial_modulus)
    # The order of the multiplicative group of the finite field GF(p^n) is p^n - 1
    order = integer_modulus**(p - 1) - 1
    primeFactors = get_prime_factors(order)
    # Check the condition for primitivity
    for i in primeFactors:
        power = order // i
        temp = f[:]
        # Compute f^power mod polynomial_modulus
        while power > 0:
            # power is even
            if power % 2 == 0:
                temp = finite_field_multiply(temp, temp, polynomial_modulus, integer_modulus)
                power //= 2
            # power is odd
            else:
                temp = finite_field_multiply(temp, f, polynomial_modulus, integer_modulus)
                power -= 1
        # If f^power mod polynomial_modulus == 1, then f is not primitive
        if temp == [1]:
            return False
    return True
