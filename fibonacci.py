# 0 1 1 2 3 5 8 13 21...

def fibonacci(nr):
    n_1 = 0
    n_2 = 1
    if nr < 0:
        return "Insert a number > 0"
    elif nr == 0 or nr == 1:
        print(nr)
    else:
        fibonacci(0)
        fibonacci(1)
        for number in range(2, nr):
            n_sum = n_1 + n_2
            n_1 = n_2
            n_2 = n_sum
            print(n_sum)

print(fibonacci(8))
