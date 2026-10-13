def is_leap_year(year):
    """判断一年是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
x,y = map(int,input().split())

leap_years = []
for year in range(x, y + 1):
    if is_leap_year(year):
        leap_years.append(year)
print(len(leap_years))
print(" ".join(map(str, leap_years)))