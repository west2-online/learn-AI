x,y=map(int, input().split())
sum=0
year=[]
for i in range(x,y+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        sum+=1
        year.append(i)
print(sum)
print(*year)