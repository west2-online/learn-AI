x, y = map(int, input().split())
leap_year_list = []
for year in range(x, y+1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year_list.append(year)
print(len(leap_year_list))
print(' '.join(map(str, leap_year_list)))
