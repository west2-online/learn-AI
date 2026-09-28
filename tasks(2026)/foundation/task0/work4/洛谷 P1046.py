high=list(map(int, input().split()))
arm=int(input())
arm+=30
sum=0
for i in high:
    if i<=arm:
        sum+=1
print(sum)