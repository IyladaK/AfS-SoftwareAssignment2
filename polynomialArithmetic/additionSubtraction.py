from utils import Poly, modP

# Polynomial Addition and Subtraction
def addition(f: Poly, g: Poly, modulus: int) -> Poly:
    # make sure f is the longer one
    if len(f) < len(g):
        f, g = g, f

    # initialize result with f
    result = f[:]
    # add coefficients of g to result
    for i in range(len(g)):
        result[i] += g[i]
    
    return modP(result, modulus)

    # Polynomial Subtraction
def subtraction(f: Poly, g: Poly, modulus: int) -> Poly:
    # negate coefficients of g
    for i in range(len(g)):
        g[i] = -g[i]
    # perform addition with negated g
    return addition(f, g, modulus=modulus)
