# # import random as 别名(模块名)导入模块,调用方式:模块名.功能名/别名.功能名
# import random as rd
# for i in range(100):
#     print(rd.randint(1, 100))
# from 模块名 import导入模块的所有功能,调用方式:功能名
from random import randint as rdt
for i in range(100):
    print(rdt(1, 100))
from random import *
print(randint(1, 100))
