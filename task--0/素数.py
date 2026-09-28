N = int(input())



if N>17:

    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print("NO")
            break
    else:
        
        print("YES")
