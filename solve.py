import json
from utils import *

def writeSolution(solPath : str, answersDict : dict[str, str]):
    with open(solPath, "w") as json_file:
        json.dump(answersDict, json_file, indent=4)


def parseExercise():
    answers = {}
    return answers


def solve_exercise(exercise_location : str, answer_location : str):
    try:
        with open(exercise_location, 'r') as file:
            params = json.load(file)

    except json.JSONDecodeError:
        print("Error: Could not load data from specified file")
        exit(0)

    answers = parseExercise()

    writeSolution(answer_location, answers)

solve_exercise("Simple/Exercises/exercise0.json", "scratch.json")
