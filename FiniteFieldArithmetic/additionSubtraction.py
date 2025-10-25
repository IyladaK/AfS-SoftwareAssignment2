from polynomialArithmetic.longDivision import longDivision
from utils import Poly, checkInputRanges
from polynomialArithmetic.additionSubtraction import addition
from polynomialArithmetic.additionSubtraction import subtraction


"""
takes polynomial array, f, irreducible polynomial (array), polyMod, and integer modulus, intMod
if deg(f) < deg(polyMod), returns f
otherwise, returns a polynomial congruent to f, f', with deg(f') < deg(polyMod)
"""
def reducePolySize(f : Poly, polyMod : Poly, intMod : int) -> Poly:
    # if deg(f) is already < deg(polyMod), just return f
    # if deg(f) >= deg(polyMod), reduce it to a congruent polynomial
    if len(f) >= len(polyMod):
        _, divRem = longDivision(f, polyMod, intMod)
        return divRem
    return f

"""
takes two polynomial arrays, f and g, an irreducible polynomial, polyMod, and integer modulus, intMod
returns f + g in F_{p^n} := Z/(intMod)Z[X] / (polyMod)
"""
def finiteFieldAddition(f : Poly, g : Poly, polyMod : Poly, intMod : int):
    # checks input ranges
    if checkInputRanges(polyMod, intMod) is False:
        return "none"

    # adds polynomials with respect to prime field
    added = addition(f, g, intMod)
    # reduces to congruent polynomial if necessary
    return reducePolySize(added, polyMod, intMod)


"""
takes two polynomial arrays, f and g, an irreducible polynomial, polyMod, and integer modulus, intMod
returns f + g in F_{p^n} := Z/(intMod)Z[X] / (polyMod)
"""
def finiteFieldSubtraction(f : Poly, g : Poly, polyMod : Poly, intMod : int):
    # check input ranges
    if checkInputRanges(polyMod, intMod) is False:
        return "none"

    # adds polynomials with respect to prime field
    subbed = subtraction(f, g, intMod)
    # reduces to congruent polynomial if necessary
    return reducePolySize(subbed, polyMod, intMod)
