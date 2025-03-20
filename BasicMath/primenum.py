# n=int(input())
# def evenOrPrime(n):
#     for i in range(2,n+1):
#         compl=n-i
#         ans=[]
#         if is_prime(compl) and is_prime(i):
#             ans.append(i)
#             ans.append(compl)
#             return ans
            
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# for i in evenOrPrime(n):
#     print(i,end=" ")

