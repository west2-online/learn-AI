n = int(input())

names = [""]
for _ in range(n):
    s = input().strip()
    names.append(s)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    names[u] = f"I_love_{names[v]}"

print(names[1])
