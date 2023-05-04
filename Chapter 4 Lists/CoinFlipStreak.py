import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipValues = []
    for times in range(100):
        flipValues.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    cur = flipValues[1]
    count = 1
    for point in flipValues[1:]:
        if cur == point:
            count += 1
        else:
            count = 0
            cur = point

        if count == 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))