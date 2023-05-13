import os
from functools import reduce

with open('DirectoryStructure.txt', 'r') as contents:

    lst = contents.read()
    lst = lst.split('\n')
    header = []
    contents = ''
    for i in range(len(lst)):
        num = lst[i].count('\t')
        header = header[:num]
        header.append(lst[i].strip())
        if i < len(lst) - 1:
            contents += '/'.join(header) + '\n'
        else:
            contents += '/'.join(header)

    print(contents)

# ------------------------------------------------

'''
with open('DirectoryStructure.txt', 'r') as contents:

    lst = contents.read()
    lst = lst.split('\n')
    header = []
    contents = ''
    for i in range(len(lst)):
        num = 0
        num = lst[i].count('\t')
        header = header[:num]
        header.append(lst[i].strip())
        if i < len(lst) - 1:
            contents += '/'.join(header) + '\n'
        else:
            contents += '/'.join(header)

    contents_lst = contents.split()

    for i in contents_lst:
        os.mkdir(i)


        
# ------------------------------------------------

with open('DirectoryStructure.txt', 'r') as contents:

    lst = contents.read()
    lst = lst.split('\n')
    header = []
    contents = ''
    for i in range(len(lst)):
        num = 0
        num = lst[i].count('\t')
        header = header[:num]
        header.append(lst[i].strip())
        if i < len(lst) - 1:
            contents += '/'.join(header) + '\n'
        else:
            contents += '/'.join(header)

    contents_lst = contents.split()

    length = len(contents_lst)

    for i in range(length):
        contents_lst[i] = contents_lst[i].split('/')


    contents_dict = {}
    for i in range(length):
        link = contents_dict
        for j in range(len(contents_lst[i])-1):
            link = link[contents_lst[i][j]]
        if i < length-1:
            if len(contents_lst[i]) < len(contents_lst[i+1]):
                link[contents_lst[i][-1]] = {}
            else:
                link[contents_lst[i][-1]] = ''
        else:
            link[contents_lst[i][-1]] = ''

    print(contents_dict)

# ------------------------------------------------


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z , self.x*other.y - self.y*other.x)
        return Vector3(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other):
        return Vector3(self.x*other, self.y*other, self.z*other)
 
    def show(self):
        print(f'<{self.x}, {self.y}, {self.z}>')

A = Vector3(2, 6, 7)
B = Vector3(3, 5, 2)

(A + B).show()
(A - B).show()
(A * B).show()
(A * 3.0).show()
(4 * B).show()
(A * B + B * A).show()
'''