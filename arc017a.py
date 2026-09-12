n = int(input())
nums = list(map(int, input().split()))
is_ok = True

for i in range(n - 1):
    current = nums[i]
    next_num = nums[i + 1]
    if next_num <= current:
        is_ok = False    
        break
        
if is_ok:
    print("YES")
else:
    print("NO")
