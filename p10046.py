apples = list(map(int, input().split()))
h = int(input())
max_height = h + 30
count = 0
for height in apples:
    if height <= max_height:
        count += 1
print(count)
