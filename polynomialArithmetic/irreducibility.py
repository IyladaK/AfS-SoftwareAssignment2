from utils import Poly
from polynomialArithmetic.extendedEuclideanAlgorithm import eea
from polynomialArithmetic.longDivision import longDivision

def primeDivisors(n : int) -> int:
    if n == 4: return 2
    else: return n

def irreducibilityCheck(f : Poly, modulus : int):
    t = 1
    n = len(f) - 1
    newPoly = [0, -1] + [0] * (modulus - 2) + [1]
    x, y, curGcd = eea(f, newPoly, modulus)
    while curGcd == [1]:
        t += 1
        if t == n:
            return "true"
        newPoly = [0, -1] + [0] * (modulus**t - 2) + [1]
        x, y, curGcd = eea(f, newPoly, modulus)
    return "false"

# not complete but would be faster
def irreducibilityCheck2(f : Poly, modulus : int):
    n = len(f) - 1
    t = primeDivisors(n)
    if n == 0:
        return False
    if n == 1:
        return True

    newPoly = [0, -1] + [0] * (modulus**t - 2) + [1]
    print(newPoly)
    _, _, curGcd = eea(f, newPoly, modulus)
    print(curGcd)
    if curGcd == [1]:
        newPoly = [0, -1] + [0] * (modulus ** n - 2) + [1]
        q, r = longDivision(newPoly, f, modulus)
        if r == [0]:
            return "true"
    return "false"


def nextPermutation(polyArr, mod):
    count = 0
    for i in range(len(polyArr)):
        if (polyArr[i] + 1) % mod == 0:
            count += 1
            polyArr[i] = 0
        else:
            polyArr[i] += 1
            break
        if count == len(polyArr):
            return [-1]
    return polyArr

def irreducibleElementGeneration(n : int, modulus : int):
    curPoly = [0]*(n) + [1]
    nextPerm = curPoly
    while irreducibilityCheck(nextPerm, modulus) == "false":
        nextPerm = nextPermutation(curPoly, modulus)
        if nextPerm == [-1]:
            return "none"
    return nextPerm

