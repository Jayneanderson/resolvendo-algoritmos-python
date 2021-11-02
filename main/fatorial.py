
def extraLongFactorials(n):
    factorial = n

    while (n > 1 ):
        n = n - 1

        factorial = factorial * n 
        
    return factorial

print(extraLongFactorials(25))