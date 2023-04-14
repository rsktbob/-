import datetime as dt
import pytz

class Triangle:
    def __init__(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            self.a = 1
            self.b = 1
            self.c = 1
        else:
            self.a = a
            self.b = b
            self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def about(self):
        result = "class Triangle"
        result += '\n' + f"area: {self.area():2f}\nperimeter: {self.perimeter()}"
        print(result)

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    triangle.about()
    print("-------------------")
    print(" Su Mo Tu We Th Fr Sa")
    time = dt.date(2002, 11, 1)
    start = 0
    day = 1
    next_month = time.month + 1
    while start <= time.weekday():
        print("   ", end='')
        start += 1
    while time.month < next_month:
        print(f'{day:3}', end='')
        if time.weekday() == 5:
            print()
        time += dt.timedelta(days=1)
        day += 1
    print("\n-------------------")
    region = {}
    for i in pytz.all_timezones:
        lst = i.split('/')
        if len(lst) == 2:
            if lst[0] not in region:
                region[lst[0]] = [lst[1]]
            else:
                region[lst[0]].append(lst[1])
    html = '<table border="1">'
    for i, j in region.items():
        html += '\n\t<tr>'
        html += f'\n\t\t<th>{i}</th>'
        for k in range(len(j)):
            if (k+1) % 5 == 0:
                j[k] += '<br>'
        str = ','.join(j)
        html += f'\n\t\t<td>{str}</td>'
        html += '\n\t</tr>'
    html += '\n</table>'
    print("\n-------------------")
    with open('BigData-Seat-2023-0302.txt', 'r+', encoding='utf-8') as seat:
        print(seat.tell())
        seat.seek(0, 0)
        lst = seat.readlines()
        arr = []
        for i in range(len(lst)):
            if lst[i][-5] == ',':
                lst[i] = lst[i][:-3] + '*' + lst[i][-2:]
            elif i == len(lst) - 1 and lst[i][-4] == ',':
                lst[i] = lst[i][:-2] + '*' + lst[i][-1]
            else:
                lst[i] = lst[i][:-2] + '*' + lst[i][-1]
    with open('BigData-Seat-2023-0302.txt', 'w+', encoding='utf-8') as seat:
	    seat.writelines(lst)