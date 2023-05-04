from CollatzSequence import Collatz

try:
    keyIn = int(input())
    while keyIn != 1:
        keyIn = Collatz(keyIn)
except:
    print("Error: invalid argument")

