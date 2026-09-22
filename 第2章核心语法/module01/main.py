# 导入my_fun模块
import my_fun
my_fun.log_se1()
my_fun.log_se2()
my_fun.log_se3()
# 导入my_fun模块的功能
from my_fun import log_se1,log_se2,PI
log_se1()
log_se2()
print(PI)
from my_fun import * #有__all__就表示all里的功能,没有就是所有功能
log_se1()
log_se4(),log_se5()
print(BAI)





