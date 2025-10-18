from typing import Tuple
from utils import Poly, leadingZerosArr, modP, leadingCoeff
from additionSubtraction import addition, subtraction
#multiply by the X^k
def polyShift(f: Poly, k: int) -> Poly:
    if f == [0]:
        return [0]
    return [0] * k + f[:]

def longDivision(f: Poly, g: Poly, p: int) -> Tuple[Poly, Poly]:
    f = leadingZerosArr(modP(f, p))
    g = leadingZerosArr(modP(g, p))
    
    if g == [0]:
        raise ZeroDivisionError("division by zero polynomial")
    
    deg_f = len(f) - 1
    deg_g = len(g) - 1

    if deg_f < deg_g:
        q = [] #quotient q  = 0
        r = f[:] # remainder r = dividend f
        return q, r
    
    q = [0] *(deg_f - deg_g +1)
    r = f[:]
    lc_g = leadingCoeff(g)
    inv_lc_g = pow(lc_g, p-2, p)
    deg_r = len(r) - 1

    while deg_r >= deg_g and r != [0]:
        r = leadingZerosArr(modP(r, p))
        lc_r = leadingCoeff(r)
        k = deg_r - deg_g

        #the coefficient of the current term (lc(r) * lc(q)^(-1)) % p
        t_coeff = (lc_r * inv_lc_g) % p

        #q ← q + (t_coeff) * X^k)
        q = addition(q, polyShift([t_coeff], k), p)

        #t_coeff * X^k *g
        tg = multiplication([t_coeff], polyShift(g,k), p)

        #r ← r - tg
        r = subtraction(r, tg, p)

    return leadingZerosArr(q), leadingZerosArr(r)


