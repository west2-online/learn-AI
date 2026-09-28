x=int(input())
y=int(input())
z=int(input())
if x>=y and x>=z:
    if y>=z:
        max_value,mid_value,min_value=x,y,z
    else:
        max_value,mid_value,min_value=x,z,y
if y>=z and y>=x:
    if x>=z:
        max_value,mid_value,min_value=y,x,z
    else:
        max_value,mid_value,min_value=y,z,x
if  z>=y and z>=x:
    if x>=y:
        max_value,mid_value,min_value=z,x,y
    else:
        max_value,mid_value,min_value=z,y,x
print(max_value,mid_value,min_value)


