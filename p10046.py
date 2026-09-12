apples = list(map(int, input().split()))
h = int(input())
max_height = h + 30
count = 0  #计数器，记录摘到的苹果数
for height in apples:
    if height <= max_height:
        count += 1
print(count)
