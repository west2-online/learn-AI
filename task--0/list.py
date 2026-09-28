word=eval(input())
list__=[]
for i in word:
    if  isinstance(i,int):
        list__.append(i)
list__.sort()
print(list__)