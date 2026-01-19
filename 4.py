import numpy as np

def monty(n=10000, switch=True):
    win = 0
    for _ in range(n):
        prize = np.random.randint(3)
        choice = np.random.randint(3)
        if switch:
            opened = [i for i in range(3) if i != choice and i != prize][0]
            choice = [i for i in range(3) if i not in (choice, opened)][0]
        if choice == prize:
            win += 1
    return win / n

print(monty(switch=False))
print(monty(switch=True))