#读取总人数
n = int(input())
#存储名字
names = [""] * (n + 1)
for i in range(1, n + 1):
    names[i] = input().strip()
#读取记录总数 m
m = int(input())
#处理m条记录
for _ in range(m):
    u,v = map(int,input().split())
    #更新u的名字
    names[u] = "i_love_" + names[v]
#输出1的名字
print(names[1])
