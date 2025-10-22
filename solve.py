import json

from polynomialArithmetic.additionSubtraction import addition, subtraction
from utils import *
from polynomialArithmetic.multiplication import multiplication
from polynomialArithmetic.longDivision import longDivision
from polynomialArithmetic.extendedEuclideanAlgorithm import eea
from polynomialArithmetic.irreducibility import irreducibilityCheck, irreducibleElementGeneration
from FiniteFieldArithmetic.additionSubtraction import finiteFieldAddition, finiteFieldSubtraction
from FiniteFieldArithmetic.primitivityCheck import primitivity_check
from FiniteFieldArithmetic.primitiveElementGeneration import primitive_element_generation

def writeSolution(solPath : str, answersDict : dict[str, str]):
    with open(solPath, "w") as json_file:
        json.dump(answersDict, json_file, indent=4)


def parseExercise(params : dict):
    type = params["type"]
    task = params["task"]
    answers = {"answer" : "null"} # this is the default answer if the inputs do not work
    if type == "polynomial_arithmetic":
        match task:
            case "addition":
                p = params["integer_modulus"]
                f = params["f"]
                g = params["g"]
                answers = {"answer": addition(f, g, p)}
            case "subtraction":
                p = params["integer_modulus"]
                f = params["f"]
                g = params["g"]
                answers = {"answer": subtraction(f, g, p)}
            case "multiplication":
                p = params["integer_modulus"]
                f = params["f"]
                g = params["g"]
                answers = {"answer": multiplication(f, g, p)}
            case "long_division":
                p = params["integer_modulus"]
                f = params["f"]
                g = params["g"]
                q, r = longDivision(f, g, p)
                answers = {"answer-q": q, "answer-r": r}
            case "extended_euclidean_algorithm":
                p = params["integer_modulus"]
                f = params["f"]
                g = params["g"]
                A, B, D = eea(f, g, p)
                answers = {"answer-a":A, "answer-b": B, "answer-gcd":D}
            case "irreducibility_check":
                p = params["integer_modulus"]
                f = params["f"]
                isIrreducible = irreducibilityCheck(f, p)
                answers = {"answer": isIrreducible}
            case "irreducible_element_generation":
                p = params["integer_modulus"]
                degree = params["degree"]
                irreduciblePoly = irreducibleElementGeneration(degree, p)
                answers = {"answer": irreduciblePoly}
            case _:
                print("task does not exist or does not match with type")
    elif type == "finite_field_arithmetic":
        match task:
            case "addition":
                f = params["f"]
                g = params["g"]
                polyMod = params["polynomial_modulus"]
                intMod = params["integer_modulus"]
                added = finiteFieldAddition(f, g, polyMod, intMod)
                answers = {"answer": added}
            case "subtraction":
                f = params["f"]
                g = params["g"]
                polyMod = params["polynomial_modulus"]
                intMod = params["integer_modulus"]
                subbed = finiteFieldSubtraction(f, g, polyMod, intMod)
                answers = {"answer": subbed}
            case "multiplication":
                pass
            case "division":
                pass
            case "inversion":
                pass
            case "primitivity_check":
                f = params["f"]
                integer_modulus = params["integer_modulus"]
                polynomial_modulus = params["polynomial_modulus"]
                result = primitivity_check(f, integer_modulus, polynomial_modulus)
                answers = {"answer": result}
            case "primitive_element_generation":
                f = params["f"]
                integer_modulus = params["integer_modulus"]
                polynomial_modulus = params["polynomial_modulus"]
                result = primitive_element_generation(integer_modulus, polynomial_modulus)
                answers = {"answer": result}
            case _:
                print("task does not exist or does not match with type")
    else:
        print("type does not exist")
    return answers


def solve_exercise(exercise_location : str, answer_location : str):
    try:
        with open(exercise_location, 'r') as file:
            params = json.load(file)

    except json.JSONDecodeError:
        print("Error: Could not load data from specified file")
        exit(0)

    answers = parseExercise(params)

    writeSolution(answer_location, answers)

solve_exercise("./Realistic/Exercises/exercise10.json", "./scratch.json")