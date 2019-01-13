def HaveFun():
    if __name__ == '__main__':
        print('I am in my domain,my name is %s' % __name__)
    else:
        print('Someone else calls me!,my name is %s' % __name__)


HaveFun()


# __name__这个系统变量显示了当前模块执行过程中的名称，如果当前程序运行在这个模块中，__name__ 的名称就是__main__如果不是，则为这个模块的名称。
# __main__一般作为函数的入口，类似于C语言，尤其在大型工程中，常常有if __name__ == "__main__":来表明整个工程开始运行的入口。