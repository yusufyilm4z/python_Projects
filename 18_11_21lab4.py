import random
def is_prime(n):
    is_prime=True
    for i in range(2,n):
        if(n%i==0):
            return False
    return True


print(is_prime(n))

