count=0
year=[]
x,y=map(int,input().split())
for i in range(x,y+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        count+=1
        year.append(i)

print(count)
print(*year)