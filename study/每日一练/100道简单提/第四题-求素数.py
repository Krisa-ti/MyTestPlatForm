arr = []
i = 0
def is_prime(number):
    if number in (1,2):
        return True
    for idx in range(2,number):
        if number % idx  == 0:
            return False
    return True

def sushu(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number}是素数")
sushu(11,25)