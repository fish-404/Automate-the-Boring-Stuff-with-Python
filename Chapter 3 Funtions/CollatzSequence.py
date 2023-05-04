def Collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = number * 3 + 1

    print(result)
    return result

