n = int(input())
lst = []
for _ in range(n):
    name = input()
    lst.append(name)
m = int(input())
love = 'I_love_'
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    lst[u] = love + lst[v]
print(lst[0])