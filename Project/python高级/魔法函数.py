class Company(object):

    def __init__(self,employee_list):
        self.employ = employee_list

    def __getitem__(self, item):
        return self.employ[item]

company = Company(["tom","bob","jane"])

for em in company:
    print(em)

from threading import Condition
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor