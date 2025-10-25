from typing import Tuple
from utils import leadingZerosArr, modP, leadingCoeff
from .additionSubtraction import addition
from .multiplication import multiplication
from .longDivision import longDivision

def scalarMul(f, c: int, p: int):
    return [(c*a) % p for a in f]

def neg(f, p: int):
    return [(-1*c) % p for c in f]

def eea(f, g, p: int):

    #A*f + B*g = D and D = gcd(f,g) as monic, it returns to (A,B,D)

    f = leadingZerosArr(modP(f, p))
    g = leadingZerosArr(modP(g, p))

    if f == [0] and g == [0]:
        return [0], [0], [0]
    
    if g == [0]:
        lc_f = leadingCoeff(f) % p
        if lc_f != 0:
            inv_lc_f = pow(lc_f, p-2, p) #to compute lc(f)^(-1) with Fermat's Little Theorem
        else:
            inv_lc_f = 0
        D = scalarMul(f, inv_lc_f, p) #gcd(f,0) = monic(f)
        #A*f + B*0 = D  
        A = [inv_lc_f] # A = lc(f)^-1 
        B = [0]      # B = 0
        return A,B,D
    
    if f == [0]:
        lc_g = leadingCoeff(g) % p
        if lc_g != 0:
            inv_lc_g = pow(lc_g, p-2, p) #to compute lc(g)^(-1) with Fermat's Little Theorem
        else:
            inv_lc_g = 0
        D = scalarMul(g, inv_lc_g, p) #gcd(0,g) = monic(g)
        #A*0 + B*g = D  
        A = [0] # A = 0
        B = [inv_lc_g] # B = lc(g)^-1 
        return A,B,D
    

    # initials: a0 = f = 1*f + 0*g ; b0 = g = 0*f + 1*g
    A, B = [1], [0] #(A,B) = (1,0) for a0
    U, V = [0], [1] #(U,V) = (0,1) for b0
    a, b = f[:], g[:] # polynomials a and b

    while b != [0]:
        quot, rem = longDivision(a,b,p)
        a = b
        b = rem

        #updating Bezout coefficients
        #A = U, U = A - quot * U
        qU = multiplication(quot, U, p)
        A, U = U, addition(A, neg(qU, p),p)

        #B = V, V = B - quot * V
        qV = multiplication(quot, V, p)
        B, V = V, addition(B, neg(qV, p), p)

    # a = gcd(f, g), make A, B, D monic

    lc_a = leadingCoeff(a) % p

    if lc_a != 0:
        inv_lc_a = pow(lc_a, p-2, p) #lc(g)^(-1) with Fermat's Little Theorem
    else:
        inv_lc_a = 0
    
    D = scalarMul(a, inv_lc_a, p)
    A = scalarMul(A, inv_lc_a, p)
    B = scalarMul(B, inv_lc_a, p)

    return leadingZerosArr(A), leadingZerosArr(B), leadingZerosArr(D)

