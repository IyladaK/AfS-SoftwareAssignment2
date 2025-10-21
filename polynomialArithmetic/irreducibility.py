from utils import Poly
from polynomialArithmetic.extendedEuclideanAlgorithm import eea

def irreducibilityCheck(f : Poly, modulus : int):
    t = 1
    n = len(f) - 1
    newPoly = [0, -1] + [0] * (modulus - 2) + [1]
    x, y, curGcd = eea(f, newPoly, modulus)
    while curGcd[0] == 1:
        t += 1
        if t == n:
            return "true"
        newPoly = [0, -1] + [0] * (modulus**t - 2) + [1]
        x, y, curGcd = eea(f, newPoly, modulus)
    return "false"

def irreducibleElementGeneration():
    return
