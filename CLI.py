from State import State
from answerManager import AnswerManager
from SearchAlgorithm import SearchAlgorithm
import re


class CLI:

    def __init__(self):
        self.__manager = None
        self.__algorithm = None

    def __inputExchange(self, message: str, validator) -> str:
        print()
        while True:
            userInput = input(message)
            if (validator(userInput)):
                return userInput
            print("Invalid input! Try again.")

    def stateValidator(self, userInput: str) -> bool:
        test = re.search("^(\s*[0-8]\s*){9}$", userInput)
        if test is None: return False
        found = [False]*9
        for character in test.string:
            if (not found[int(character)]): found[int(character)] = True
            else: return False
        return True

    def programLoop(self):
        print("Welcome to The 8-Puzzle Solver!")
        while True:
            startStateText = self.__inputExchange("Please enter a starting state...", self.stateValidator)



cli = CLI()
print(cli.stateValidator("01234568"))