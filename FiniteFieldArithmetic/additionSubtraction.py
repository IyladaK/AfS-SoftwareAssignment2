from utils import Poly
from polynomialArithmetic.additionSubtraction import addition
from polynomialArithmetic.additionSubtraction import subtraction

def reducePolySize(f : Poly, polyMod : Poly) -> Poly:
    if len(f) > len(polyMod):
        return f[:len(polyMod)]
    return f


def finiteFieldAddition(f : Poly, g : Poly, polyMod : Poly, intMod : int) -> Poly:
    f = reducePolySize(f, polyMod)
    g = reducePolySize(g, polyMod)
    return addition(f, g, intMod)

def finiteFieldSubtraction(f : Poly, g : Poly, polyMod : Poly, intMod : int) -> Poly:
    f = reducePolySize(f, polyMod)
    g = reducePolySize(g, polyMod)
    return subtraction(f, g, intMod)
