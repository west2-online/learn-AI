apple=list(map(int,input().split()))
hand=int(input())
height_hand=hand+30
count=0
for height in apple:
    if height <=height_hand :
        count+=1
print(count)
