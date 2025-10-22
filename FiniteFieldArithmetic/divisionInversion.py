from typing import Tuple
from utils import Poly, modP, leadingZerosArr, leadingCoeff
from polynomialArithmetic.additionSubtraction import subtraction
from polynomialArithmetic.multiplication import multiplication
from polynomialArithmetic.longDivision import longDivision

def _poly_mod_h(f: Poly, h: Poly, p: int) -> Poly:
    f = modP(f, p)
    _, r = longDivision(f, h, p)
    return leadingZerosArr(modP(r, p))

def _egcd_poly(a: Poly, b: Poly, p: int) -> Tuple[Poly, Poly, Poly]:
    # r0, r1 setup
    r0 = leadingZerosArr(modP(a, p))
    r1 = leadingZerosArr(modP(b, p))
    s0, s1 = [1], [0]
    t0, t1 = [0], [1]

    while r1 != [0]:
        q, r2 = longDivision(r0, r1, p)
        r0, r1 = r1, r2
        s0, s1 = s1, subtraction(s0, multiplication(q, s1, p), p)
        t0, t1 = t1, subtraction(t0, multiplication(q, t1, p), p)

    # make gcd monic
    lc = leadingCoeff(r0)             # nonzero because r0 != [0]
    inv_lc = pow(lc, p - 2, p)        # inverse in F_p
    r0 = multiplication([inv_lc], r0, p)
    s0 = multiplication([inv_lc], s0, p)
    t0 = multiplication([inv_lc], t0, p)
    return leadingZerosArr(r0), leadingZerosArr(s0), leadingZerosArr(t0)

def finiteFieldInverse(f: Poly, h: Poly, p: int) -> Poly:
    f = _poly_mod_h(f, h, p)
    if f == [0]:
        raise ZeroDivisionError("inverse of zero polynomial in F_p[X]/(h)")
    if f == [1]:
        return [1]
    _g, s, _t = _egcd_poly(f, h, p)   # s*f + t*h = 1
    return _poly_mod_h(s, h, p)       # s is the inverse mod h

def finiteFieldDivision(f: Poly, g: Poly, h: Poly, p: int) -> Poly:
    f = _poly_mod_h(f, h, p)
    g = _poly_mod_h(g, h, p)
    if g == [0]:
        raise ZeroDivisionError("division by zero in F_p[X]/(h)")
    if g == [1]:
        return f
    return _poly_mod_h(multiplication(f, finiteFieldInverse(g, h, p), p), h, p)
