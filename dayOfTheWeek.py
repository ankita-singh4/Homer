def dayOfTheWeek(day, month, year):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if year % 4 == 0:
        count = 1
    else: count = 0
    print(count)
    daysofmonths = [31, 28, 31,30,31,30,31,31,30,31,30,31]
    sumofMonths = sum(daysofmonths[0:month-1])
    print(sumofMonths)
    count = day + sumofMonths + count
    print(count)
    print(count, count % 7)
    return days[count % 7]


day = 20
month = 4
year = 2020
print(dayOfTheWeek(day, month, year))
