from typing import List

Poly = List[int] #from the coefficient of lowest degree to coefficient of highest degree


# all finite field arithmetic funcitons except primitivity ones have  value ranges
# p \in [2, 509] and deg(h) \in [2, 256]
# returns true of input values fit, false otherwise
def checkInputRanges(polyMod, intMod):
    degH = len(polyMod) - 1
    if intMod < 2 or intMod > 509 or degH < 2 or degH > 256:
        return False
    return True


#remove leading zeros
def leadingZerosArr (x:Poly) -> Poly:
    i = len(x)-1
    while i > 0 and x[i] == 0:
        i-=1
        if i < 0 :
            return [0]
    return x[:i+1]
        
# compute x mod p
def modP (f:Poly, p:int) -> Poly:
    return leadingZerosArr([c % p for c in f])

# take the last element from the Poly list which returns to leading coefficent
def leadingCoeff(f: Poly) -> int:
    f = leadingZerosArr(f)
    return 0 if not f else f[-1]

def get_prime_factors(n: int) -> List[int]:
    factors = []
    d = 2
    temp_n = n
    # Standard trial division up to sqrt(n)
    while d * d <= temp_n:
        if temp_n % d == 0:
            factors.append(d)
            temp_n //= d
        else:
            d += 1
    # The last remaining number is also a prime factor
    if temp_n > 1:
        factors.append(temp_n)
    return factors