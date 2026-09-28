students = {'101': '张三', '102': '李四', '103': '王五', '104': '赵六', '105': '钱七'}
key=list(students.keys())
for i in key:
    last=int(i[-1])
    if last%2==0:

        students.pop(i)
print(students)