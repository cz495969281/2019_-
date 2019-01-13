from collections import defaultdict
from pprint import pprint
# user_dict = {"cz1":1}
user_dict = {}
users = ["cz1","cz2","cz3","cz1","cz2","cz2"]

for user in users:

#把这块的代码做进一步的精简呢？
#这块代码实际上还是有问题的，如果这里面的代码写的过于复杂，逻辑过多可能影响代码的可读性，有哪种方法可以把这块代码
#写的更加清晰也更加简单
################################
    # if user not in user_dict:
    #     user_dict[user] = 1
    #
    # else:
    #     user_dict[user] +=1
################################


#有什么方向可以把 user_dict.setdefault(user,0)这步操作再次简化
###################################
    user_dict.setdefault(user,0)  #setdefault()更加高效，因为少做一次查询
    user_dict[user] += 1

###################################
# default_dict = defaultdict(int)
# for user in users:
    # default_dict[user] +=1
# pass

def gen_default():
    return {
        "name":"",
        "nums":0
    }

default_dict = defaultdict(gen_default)
default_dict["cz"]
pprint(default_dict)