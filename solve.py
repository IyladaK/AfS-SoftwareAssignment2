import json
from utils import *

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
                pass
            case "subtraction":
                pass
            case "multiplication":
                pass
            case "long_division":
                pass
            case "extended_euclidean_algorithm":
                pass
            case "irreducibility_check":
                pass
            case "irreducible_element_generation":
                pass
            case _:
                print("task does not exist or does not match with type")
    elif type == "finite_field_arithmetic":
        match task:
            case "addition":
                pass
            case "subtraction":
                pass
            case "multiplication":
                pass
            case "division":
                pass
            case "inversion":
                pass
            case "primitivity_check":
                pass
            case "primitive_element_generation":
                pass
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

solve_exercise("Simple/Exercises/exercise0.json", "scratch.json")
