names=[]
n=int(input())
for i in range(n):
    names.append(input())
m=int(input())
for i in range(m):
    u,v=map(int,input().split())
    names[u-1]="I_love_"+names[v-1]
print(names[0])

