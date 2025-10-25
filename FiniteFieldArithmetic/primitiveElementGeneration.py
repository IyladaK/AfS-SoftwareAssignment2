from utils import get_prime_factors, leadingZerosArr
from .primitivityCheck import primitivity_check
from random import randint

# Generate a primitive element in a finite field
def primitive_element_generation(integer_modulus: int, polynomial_modulus):
    
    # The degree of the polynomial modulus
    maximum_degree = len(polynomial_modulus) - 1
    p = []
    while True:
        # Generate a random polynomial of degree less than maximum_degree
        for _ in range(maximum_degree):
            coefficent = randint(0, integer_modulus - 1)
            p.append(coefficent)

        # Remove leading zeros
        p = leadingZerosArr(p)

        # Check for the zero polynomial
        if p == [0]:
            p = [] #reset
            continue
        
        # Check if the generated polynomial is primitive
        if primitivity_check(p, integer_modulus, polynomial_modulus):
            break
        # Reset the polynomial
        p = []
    return p
