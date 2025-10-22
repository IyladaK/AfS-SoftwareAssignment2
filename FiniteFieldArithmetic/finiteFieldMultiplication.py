from utils import Poly
from polynomialArithmetic.longDivision import longDivision
from polynomialArithmetic.multiplication import multiplication
from .additionSubtraction import reducePolySize

def finite_field_multiply(f : Poly, g : Poly, polyMod : Poly, intMod : int) -> Poly:
    #polynomial multiplication mod intMod
    product = multiplication(f, g, intMod)
    #long division by polyMod to get remainder
    _,remainder = longDivision(product, polyMod, intMod)
    return reducePolySize(remainder, polyMod)