import random


def isSolvable(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if int(state[i]) > int(state[j]) and state[j] != '0':
                inversions += 1
    return inversions % 2 == 0

def generate_random_solvable_state():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random_state = ''.join(map(str, random.sample(digits, len(digits))))
    while not isSolvable(random_state):
        random_state = ''.join(map(str, random.sample(digits, len(digits))))
    return random_state

def generate_random_unSolvable_state():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random_state = ''.join(map(str, random.sample(digits, len(digits))))
    while isSolvable(random_state):
        random_state = ''.join(map(str, random.sample(digits, len(digits))))
    return random_state

def generate():
    states = set()
    while len(states) < 20:
        states.add(generate_random_solvable_state())
    for state in states: print(list(state))
    return states