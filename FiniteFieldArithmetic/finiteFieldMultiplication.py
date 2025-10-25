from utils import Poly, checkInputRanges
from additionSubtraction import reducePolySize
from polynomialArithmetic.multiplication import multiplication


def finite_field_multiply(f : Poly, g : Poly, polyMod : Poly, intMod : int):
    if checkInputRanges(polyMod, intMod) is False:
        return "none"
    #polynomial multiplication mod intMod
    product = multiplication(f, g, intMod)
    #long division by polyMod to get remainder if necessary
    return reducePolySize(product, polyMod, intMod)
