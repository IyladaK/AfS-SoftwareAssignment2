from utils import Poly
from polynomialArithmetic.extendedEuclideanAlgorithm import eea
from polynomialArithmetic.longDivision import longDivision


"""
takes a polynomial, f, with deg(f) in [1, 5] as a Poly array and an integer modulus q in [1, 13]
returns true if the polynomial is irreducible in the modulus field
return false if the polynomial is reducible
"""
def irreducibilityCheck(f : Poly, q : int):
    n = len(f) - 1 # degree of f

    # check for correct input ranges
    if q < 2 or q > 13 or n < 1 or n > 5:
        return "none"
    # trivial case: linear is always irreducible
    if n == 1:
        return "true"

    # check if f|X^{q^n}
    n = len(f) - 1
    prodPoly = [0, -1] + [0]*(q**n - 2) + [1]
    _, divRem = longDivision(prodPoly, f, q)

    if divRem != [0]:
        return "false"

    # now we check that for all proper prime divisors, d, of n, that
    # EEA(f, X^{q^(n/d)} - X) = 1
    # at this point, n \in {2, 3, 4, 5}, and since {2, 3, 5} do not have any
    # proper prime divisors (excluding itself and 1), we only need to check
    # proper prime divisors if n = 4, and we only need to check for d = 2
    if n == 4:
        # proper prime divisor = {2}
        eeaPoly = [0, -1] + [0]*(q**2 - 2) + [1]
        _, _, gcd = eea(eeaPoly, f, q)
        if gcd != [1]:
            return "false"

    return "true"


"""
takes a polynomial, polyArr, with deg(polyArr) = f as a Poly array and an integer modulus, mod
increments the polynomial to the next smallest polynomial within deg(polyArr') = f
returns the next smallest Poly array if such a polynomial exists
returns [-1] otherwise
"""
def nextPermutation(polyArr : Poly, mod : int):
    # iterates from least to most significant coef
    for i in range(len(polyArr)):
        # if incrementing this coefficient causes a carry forward,
        # set this coef to 0
        if (polyArr[i] + 1) % mod == 0:
            polyArr[i] = 0
        else:
        # if incrementing doesn't cause a carry, increment and exit the loop
        # this successfully increments the first available coef after a chain
        # of carrys
            polyArr[i] += 1
            break
        # if every coef has caused a carry, then this is the maximum value for the
        # given degree. return -1 as magic number.
        if i == len(polyArr) - 1:
            return [-1]

    return polyArr


"""
takes an integer degree, n in [1, 5], and an integer modulus, p in [2, 13]
returns an irreducible polynomial, p, with degree(p) = n
"""
def irreducibleElementGeneration(n : int, p : int):
    # irreducible element generation accepts n \in [1, 5] and p \in [2, 13]
    # check for correct input ranges
    if p < 2 or p > 13 or n < 1 or n > 5:
        return "none"

    # set up for smallest Poly with degree n = X^n
    curPoly = [0]*(n) + [1]

    # We iterate from X^n to pX^n + pX^{n-1} + ... + p until we find an irreducible Poly
    while irreducibilityCheck(curPoly, p) == "false":
        # since the current smallest Poly is reducible, we increment
        curPoly = nextPermutation(curPoly, p)
        # -1 is the magic number returned after the maximum Poly for degree n
        if curPoly == [-1]:
            return "none"
    # only returns when irreducibilityCheck(curPoly, p) gives "true"
    return curPoly
