from CollatzSequence import Collatz

keyIn = int(input())
while keyIn != 1:
    keyIn = Collatz(keyIn)