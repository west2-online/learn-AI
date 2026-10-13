import math
N = int(input())
is_prime = True
if N <= 1:
    is_prime = False
else:
   limit = int(math.sqrt(N)) + 1
   for i in range (2,limit):
      if N % i == 0:
         is_prime = False
         break

if is_prime:
   print("Yes")
else:
   print("NO")