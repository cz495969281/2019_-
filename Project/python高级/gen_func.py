
#生成器函数，函数里只要有yield关键字
def gen_func():
    yield 1
    yield 2
    yield 3
    yield 4
#惰性求值，延迟求值提供了可能


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

print(fib(3))

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
    return re_list

def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b,a+b
        n += 1

for data in gen_fib(10):
    print(data)

def func():
    return 1

if __name__ == '__main__':
    #返回的是生成器对象，什么时候产生的这个对象的呢？python编译字节码的时候就产生了
    gen = gen_func()
    # print(next(gen))
    # for value in gen:
    #     print(value)
    # # re = func()
    pass