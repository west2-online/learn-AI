apple_heights = list(map(int,input().split()))
#苹果高度输入
reach_height = int(input())
#输入最大高度
max_reach = 30 + reach_height
#踩凳子
count = 0
for height in apple_heights:
    if height <= max_reach:
        count += 1

print(count)
#输出能摘得苹果数