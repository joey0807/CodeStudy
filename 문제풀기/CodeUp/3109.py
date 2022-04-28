class Student:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self,no):
        self.__no=no
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

n = int(input())
data = []
num = []
for i in range(n):
    c, no, name = input().split()

    if c == 'I':
        if int(no) not in num:
            num.append(int(no))
            data.append(Student(int(no),name))
        else:
            num.append(int(no))
            data.insert(0,Student(int(no),name))
    elif c == 'D':
        if int(no) in num:
            num.remove(int(no))
            for j in range(len(data)):
                if data[j].no == int(no):
                    del data[j]
                    break

print_arr = input().split()

#sort_data = sorted(data, key=lambda x:x.no)
data.sort(key=lambda x:x.no)

for x in range(len(print_arr)):
    print(data[int(print_arr[x])-1].no, data[int(print_arr[x])-1].name)