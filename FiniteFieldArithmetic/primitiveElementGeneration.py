from utils import Poly, get_prime_factors, leadingZerosArr
from primitivityCheck import primitivity_check
from random import randint

def primitive_element_generation(integer_modulus: int, polynomial_modulus: Poly) -> Poly:
    
    maximum_degree = len(polynomial_modulus) - 1
    p = []
    while True:
        for _ in range(maximum_degree):
            coefficent = randint(0, integer_modulus - 1)
            p.append(coefficent)

        p = leadingZerosArr(p)

        if p == [0]:
            p = [] #reset
            continue

        if primitivity_check(p, integer_modulus, polynomial_modulus):
            break
        p = []
    return p