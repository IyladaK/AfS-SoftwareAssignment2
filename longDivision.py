from typing import List, Tuple

Poly = List[int] #from the coefficient of lowest degree to coefficient of highest degree

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


