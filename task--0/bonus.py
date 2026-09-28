x=int(input())
y=int(input())
z=int(input())
numbers=[x,y,z]
numbers.sort(reverse=True)
print(*numbers)