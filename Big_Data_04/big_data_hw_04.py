from datetime import timedelta, date
import os

#-----------------------------------------------
    
with open('ReadMe.txt', 'rb') as file:
    read = file.read()
    for i in range(200):
        lst = bytearray(read)
        for j in range(len(lst)):
            lst[j] ^= i
        try:
            print(f'{i}' + " " + lst.decode())
        except:
            pass

# -----------------------------------------------


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            x = self.y * other.z - self.z * other.y
            y = other.x * self.z - other.z * self.x
            z = self.x * other.y - self.y * other.x
        else:
            x = self.x * other
            y = self.y * other
            z = self.z * other
        return Vector3(x, y, z)

    def show(self):
        print(f'<{self.x} {self.y} {self.z}>')

A = Vector3(2, 6, 7)
B = Vector3(3, 5, 2)
(A + B).show()
(A - B).show()
(A * B).show()
(A * 3).show()
(A * B + B * A).show()

#-----------------------------------------------

def show_dir0(dirs, header=''):
    for dk in dirs:
        os.mkdir(header+dk)
        if isinstance(dirs[dk], dict):
            show_dir0(dirs[dk], header+dk+'/')


time = date(2023, 2, 23)
for i in range(18):
    print(time.strftime('%Y-%m%d'))
    time += timedelta(weeks=1)

def show_dir0(dirs, header=''):
    for dk in dirs:
        os.mkdir(header+dk)
        if isinstance(dirs[dk], dict):
            show_dir0(dirs[dk], header+dk+'/')

dirs = {'my_data': {'jpg': "", 'png': "", 'gif': "", 'data': {'txt': "", 'dat': ""},
                'python': {'py': "", 'ipynb': ""}}}
show_dir0(dirs)
