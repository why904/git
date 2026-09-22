# __all__表示*中导入的功能
__all__=["log_se4","log_se5","BAI","log_se1"]
# 大写为常量
PI = 3.14159
BAI = "海里恒鱼"
# 函数
def log_se1():
    print("+ " * 30)
def log_se2():
    print("- " * 30)
def log_se3():
    print("* " * 30)
def log_se4():
    print("$ " * 30)
def log_se5():
    print("# " * 30)
# __name__在本模块是main,在导入模块是被导模块名称
if __name__ == '__main__':
    log_se1()
