# 函数开始
# def out_line():
#     print("________")
# out_line()
# def circle_area_len(r):
#     """
#     根据半径r计算面积和周长
#     :param r: 半径
#     :return: 面积,周长
#     """
#     return round(3.14*r*r,1),round(2*3.14*r,1)
# def tecttangle_area(l,w):
#     """
#     根据长l,宽w计算长方形面积
#     :param l:长
#     :param w:宽
#     :return:长方形面积
#     """
#     return l*w
# print(tecttangle_area(3,4))
# print(f"长方形面积{tecttangle_area(20,10)},圆形面积和周长:{circle_area_len(8)}")
#
# #函数嵌套使用,后进先出
# def function_a():
#     print("a...before")
#     function_b()
#     print("a...after")
# def function_b():
#     print("b...before")
#     function_c()
#     print("b...after")
# def function_c():
#     print("c...before")
# function_a()

# 案例
# 根据底和高来计算三角形面积
# def triangle_area(a,h):
#     """
#     基于底a高h计算三角形面积
#     :param a: 底
#     :param h: 高
#     :return: 三角形面积
#     """
#     return round(a*h/2,1)
# a=4#float(input('请输入三角形的底:'))
# h=5#float(input('请输入三角形的高:'))
# print(triangle_area(a,h))
# # 计算传入字符串中元音字母个数
# text="fjajjejflejofijo"#input("输入字符串:")
# def def_vowel(s):
#     """
#     计算字符串s的元音字母的个数
#     :param s:字符串
#     :return:字符串个数
#     """
#     num=0
#     for w in s:
#         if w in 'aoeiuAOEIU':
#             num +=1
#     return num
#     # vowels=['a','o','e','i','u','A','O','e','I','U']
#     # return sum([s.count(v) for v in vowels])
# print(def_vowel(text))
# # 计算传入学生高考成绩的最高最低分平均分
# s_list=[600,500,300,200,100,400]
# def calc_score(score_list):
#     """
#     计算传入学生高考成绩的最高最低分平均分
#     :param score_list: 成绩列表
#     :return: 最高,最低分,平均分
#     """
#     return min(score_list),max(score_list),round(sum(score_list)/len(score_list),1)
# min_score,max_score,sum_score=calc_score(s_list)
# print(f'最高分{min_score},最低分{max_score},平均分{sum_score}')

# 进阶函数1变量作用域 2参数详解 3匿名函数
# # 1变量作用域
# num=10000#全局变量
# def fun(k):
#     global num
#     num=100#局部变量
#     return num
# print(num)
# fun("调用函数global使num变成全局变量")
# print(num)
#
# #2参数详解 传参方式 默认函数 不定长参数 参数类型
# # 方式:位置参数按位置传参数,关键字参数如name='关键字参数'
# def reg(name,age,gender,city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {'name':name,'age':age,'gender':gender,'city':city}
# stu=reg('位置参数',18,'男','北京')
# stu2=reg(age=18,gender='男',name='关键字参数',city='广州')
# print(stu2,stu)
# # 默认参数:默认值必须在最后,可不赋值赋值替代默认值
# def reg(age,city,gender='默认值男',name='默认值名字'):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {'name':name,'age':age,'gender':gender,'city':city}
# print(reg(age=30,city='广州'))
# #不定长参数:位置参数传递*args主要是处理数据,关键字传递的**kargs数据的选项
# def calc_data(*args,**kwargs):
#     min_data=min(args)
#     max_data=max(args)
#     aver_data=sum(args)/len(args)
#     if kwargs.get('round') is not None:
#         aver_data=round(aver_data,kwargs.get('round'))
#     if kwargs.get('print'):
#         print(f'最小值{min_data},最大值{max_data},平均值{aver_data}')
#     return min_data, max_data, aver_data
# print(calc_data(1, 3, 5, 7, 9, 20, 33, round=2, print=True))
# # 参数类型 还可以是函数
# def add(x,y):
#     return x+y
# def sud(x,y):
#     return x-y
# def calc(x,y,oper):
#     return oper(x,y)
# print(calc(10,20,sud))
#
# # 3匿名函数lambda,单行
# out_line=lambda:print("--------")
# add=lambda x,y:x+y
# out_line()
# print(add(199,198))
# # 用在排序sort方法中key的参数,lambda会接收到列表的所有参数,是key发出的
# data_list=['c++','c','python','jack','pyp','java','go','rust']
# data_list.sort()
# print(data_list)
# data_list.sort(key=lambda item:len(item),reverse=False)
# print(data_list)
# 案例1定义一个函数,计算传入数据的阶层
def jc(n):
    if n==1:
        return n
    return n*jc(n-1)
print(jc(10))
#案例2+类型注解
"""
 根据传入的商品信息(商品名,价格,数量),优惠(优惠卷,积分抵扣),运费信息计算订单总金额
 优惠方案
 1.优惠卷需要价格满5000,且优惠价格不能超过商品金额
 2.积分也需要价格满5000,100积分=1元,积分只能整百抵扣且抵扣金额不能超过总价
"""
def calc_cost(*args:tuple[str,float,int],cpupon:int=0,score:int =0,express:float=0)->float:
    '''
    根据传入的商品信息(商品名,价格,数量),优惠(优惠卷,积分抵扣),运费信息计算订单总金额
    :param args:商品信息如(商品名,价格,数量)
    :param cpupon:优惠卷
    :param score:积分
    :param express:邮费
    :return:优惠后总价格
    '''
    total_price=[goods[1]*goods[2] for goods in args]
    total_cost=sum(total_price)
    #优惠卷
    if cpupon>=5000 and cpupon<=total_cost:
        total_cost=total_cost-cpupon
    # 积分
    if score//100<total_cost and total_cost>=5000:
        total_cost=total_cost-score//100
    #邮费
    total_cost = total_cost-express
    return total_cost
print(calc_cost(('手机',2500,2),('手机壳',10,2),cpupon=100,score=5000,express=5))
# 类型注解def a(scores:类型)->返回值类型:
def calc(scores:float)->float:
    return sum(scores)/len(scores)
def calc_data(scores:list[int])->tuple[int,int,float]:
    max_v=max(scores)
    min_v=min(scores)
    avg_v=sum(scores)/len(scores)
    return max_v,min_v,avg_v

