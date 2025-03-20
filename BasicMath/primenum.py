n=int(input("number"))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    i = 4
    while i * i <= n:
 
        if n%i==0:
            return False
        i+=1
    return True
print(is_prime(n))

