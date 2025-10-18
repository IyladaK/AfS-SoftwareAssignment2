from utils import Poly, modP

def addition(f: Poly, g: Poly, modulus: int) -> Poly:
    # make sure f is the longer one
    if len(f) < len(g):
        f, g = g, f

    result = f[:]
    for i in range(len(g)):
        result[i] += g[i]
    
    return modP(result, modulus)

def subtraction(f: Poly, g: Poly, modulus: int) -> Poly:
    for i in range(len(g)):
        g[i] = -g[i]
    return addition(f, g, modulus=modulus)
