from collections.abc import Iterator

class Company(object):

    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyItertor(self.employee)


    # def __getitem__(self, item):
    #     return self.employee[item]

class MyItertor(Iterator):

    # def __iter__(self):
    #     return self

    def __init__(self,employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]

        except IndexError:
            raise StopIteration

        self.index += 1
        return word



if __name__ == '__main__':

    company = Company(["cz1","Cz2","cz3"])
    # iter(company)   iter()首先会去找__iter__这个方法，没有这个的话才去找__getitem__创建一个迭代器，去进行遍历
    my_itor = iter(company)
    # while True:
    #     try:
    #         print(next(my_itor))
    #     except StopIteration:
    #         pass

    for item in company:
        print(item)