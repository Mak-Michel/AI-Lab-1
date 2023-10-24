from State import State
from answerManager import AnswerManager
from SearchAlgorithm import SearchAlgorithm
import re


class CLI:

    def __init__(self):
        self.__manager = None
        self.__algorithm = None

    def __inputExchange(message: str, validator: function) -> str:
        print()
        while True:
            userInput = input(message)
            if (validator(userInput)):
                return userInput
            print("Invalid input! Try again.")

    def __stateValidator(userInput: str) -> bool:
        test = re.search("^(\s*[0-8]\s*){9}$", userInput)
        return test is not None

    def programLoop(self):
        print("Welcome to The 8-Puzzle Solver!")
        while True:
            startStateText = self.__inputExchange("Please enter a starting state...", self.__stateValidator)
            


