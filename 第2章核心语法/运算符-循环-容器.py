# 加+ 减- 乘* 除/ 整除// 余数% 次方**

# x = float(input("数字1:"))
# y = float(input("数字2:"))
# print(f'数字之和:{x-y}')

# x = float(input("数字1:"))
# y = float(input("数字2:"))
# print(f'数字之和:{x-y}', x>y or x==y,not(x>y and x==y),x>y and x==y)

# score=300
# if score>600:
#     print('欢迎你来破头一中读书')
#     print('欢迎来到破头')
# else:
#     print('你可以去死了')

# mun = float(input('请输入成绩:'))
# # mun1 = float(input(''))
# if mun>85:
#     print("优秀")
# elif mun>60 and mun<85:
#     print('及格')
# else:
#     print("不及格")

# match case
# day = input('请输入星期几:')
# match day:
#     case "1":
#         print('周1')
#     case "2":
#         print("周2")
#     case "6"|"7":
#         print("周末")
#     case _:
#         print("666")

# while循环
# i=0
# total=0
# while i <= 100:
#     print('人生苦短,我学python')
#     i += 1
#     if i % 2 == 0:
#         total = i + total
# else:
#     print(f"{total}")

# for:-------
# gei = range(101)
# mun = 0
# for i in gei:
#     if i % 2 != 0:
#         mun = mun + i
#     print(i)
# else:
#     print(f"{mun}")

# gei = range(100, 501)
# mun = 0
# for i in gei:
#     if i % 3 == 0:
#         mun = mun + i
# else:
#     print(f"200到300之间3倍数的数字之和:{mun}")

# m = int(input("请输入长"))
# # n = int(input("请输入宽"))
# # for i in range(n):
# #     for i in range(m):
# #         print("*", end=" ")
# #     print()

# m = int(input("请输入大小:"))
# for h in range(1, m+1):
#     for l in range(1, h+1):
#         print(f"{l}*{h}={l*h}", end=" ")
#     print()

# while True:
#     username = input("请输入正确的用户名:")
#     password = input("请输入正确的密码:")
#     if username == " " or password == " ":
#         print("不能为空,重新输入!")
#         continue
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     else:
#         print("用户密码错误请重新输入:")

# import random
# random = random.randint(a=1, b=100)
# print(f"{random}")
# while True:
#     num = input("请输入数字")
#     if num == "":
#         print("重新输入")
#         continue
#     if int(num) > random:
#         print("数字太大了")
#     elif int(num) < random:
#         print("输入的数字太小了")
#     else:
#         print("猜对了,666")
#         break
# print("生成的随机数字是", random)

#print('第2章核心语法:1.list列表开始')
# s = [20, 30, 40, 50, 39, 92, 4, 9, 3]
# print(s[3])
# print(s[0], s[3], s[-5])
# # 修改 删除 遍历
# s[3] = 100
# del s[2]
# for item in s:
#     print(item, end="  ")

s = [20, 30, 40, 50, 39, 92, 4, 9, 3]
print(s[:-3:-1])
s.append(10)
s.insert(2, 666)
s.remove(40)
B = s.pop(5)
s.sort()
s.reverse()
print(s,B)

# print(添加数字)
# numlist=[]
# for i in range(10):
#     num=int(input("请输入一个数字:"))
#     numlist.append(num)
# numlist.sort()
# print(num,"最小值",numlist[0],"最大值",numlist[9])
# print("平均值",sum(numlist)/len(numlist))
# print(min(numlist),max(numlist))

# list1=[11,12,13,14,15]
# list2=[18,17,16,15,14]
# for num in list2:
#     list1.append(num)
# print(list1)
# list=[]
# for num in list1 :
#     if num not in list:
#         list.append(num)
# print(list)
# list1=[11,12,13,14,15]
# list2=[18,17,16,15,14]
# list3=[*list1,*list2]
# list三=list1+list2
# list=[]
# print(list3)
# for num in list3 :
#     if num not in list:
#         list.append(num)
# print(list)
# not取反对的含义
# in表示元素在不在列表里

# print('把一些数字处理并添加到列表')
# num_list=[]
# for mun in range(1,21):
#     num_list.append(mun**2)
# print(num_list)
# print('简化')
# num_list1=[i**2 for i in range(1,21)]
# print(num_list1)
# print('加强')
# num_list3=[12,32,45,77,80,92,45,26,73,45,25]
# new_list=[i**2 for i in num_list3 if i % 2==0]
# print(new_list)
# print('合并排序.提取平方')
# num_listan=num_list1+num_list+new_list
# num_listan.sort()
# print(num_listan)
# num_listan=[i**2 for i in num_listan if i%3==0 or i%5==0]
# print(num_listan)

# print("str字符串开始 不可替代性,有序性,可迭代性")
# s='hello-python'
# print(s[4],s[-8])
# for i in s:
#     print(i)
# print(s[0:5:12],s[:5],s[:5:1])
# mali=input("输入邮箱:")
# if mali.count("@")==1 and mali.count(".")>=1:
#     print(f"{mali}是合法的邮箱")
# else:
#     print(f"{mali}是非法的邮箱")
# print('------是不是回文,反转大写进列表遍历')
# mali1=input("输入邮箱2:")
# if len(mali1)==len(mali):
#     print('两边对称')
# t='qwertyuiop'
# s=t.upper()
# print(s)
# print(s[-1:-11:-1])
# list=[]
# for i in s[::-1]:
#     list.append(i)
#     print(i)
# print(list)

# print("tuple元组:和列表差不多就是不能修改,重复性,有序性,不可修改性..(可以访问切片索引)")
# tup=("元","组","格","式")
# tup2='元','组',2,'号'
# print(tup[2],tup.count("元"),tup.index("组"),tup2)
# a,b,c,d=tup
# a1,*b1=tup2
# print(a,b,c,d,a1,b1)

# 计算每个学生的总分,各科平均分,然后一起输出出来.
# stu=(
#     ("s001","王林",85,92,78),
#     ("s002","李慕婉",92,88,95),
#     ("s003","十三",78,85,82),
#     ("s004", "曾牛",88,79 ,91),
#     ("s005", "间铁",87,83 ,83),
#     ("s006", "王卓",90,94 ,85),
#     ("s007", "红蝶",83,95 ,86),
#     ("s008", "徐立国",75,72,74 ),
#     ("s009", "许木",97,86 ,96),
#     ("s010", "遁天",68, 73,85),
# )
# print("学生 \t 总分 \t 平均分")
# for s in stu:
#     to=s[2]+s[3]+s[4]
#     aver=to / 3
#     print(f'{s[1]} \t {to} \t {aver:.1f}')
# #统计各科成绩的最低分,最高分并输出.
# stu3=[i[2] for i in stu]
# stu4=[i[3] for i in stu]
# stu5=[i[4] for i in stu]
# print(f"语文最低分:{min(stu3)}\t语文最高分:{max(stu3)}\t语文班级平均分:{sum(stu3) / len(stu3)}")
# print(f"数学最低分:{min(stu4)}\t数学最高分:{max(stu4)}\t数学班级平均分:{sum(stu4) / len(stu4)}")
# print(f"英语最低分:{min(stu5)}\t英语最高分:{max(stu5)}\t英语班级平均分:{sum(stu5) / len(stu5)}")
# #查找平均分大于90分的学生并输出.
# print("优秀学生如下:")
# for s in stu:
#     aver=(s[2]+s[3]+s[4])/3
#     if aver > 90 :
#         print(s[1])

# print("set集合,无序性,不可修改")
# si={5,66,25,63,6,8,3,5,5,5,98}
# print(si)
# s1=set()
# si.add(120)
# print(si,'添加')
# si.remove(63)
# print(si,'删除')
# e=si.pop()
# print(e,'删除')
# si.clear()
# print(si,'清空')
# s1={"A","B","C","D"}
# s2={"C","D","F","Y","Z"}
# print(s1.difference(s2),'差集')
# print(s2.difference(s1),'差集')
# print(s2.union(s1),'并集')
# print(s1.intersection(s2),'交集')
# print(s1.difference(s2),s1.union(s2),s1.intersection(s2) )

#  # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#
# print('交集',french_set.intersection(art_set),french_set &art_set)
# print(f"同时选修了4门课程的学生:{french_set&art_set&basketball_set&football_set},")
# print(f"选择足球但没有选择篮球差集{football_set.difference(basketball_set)}")
# print(f'并集{french_set|football_set|art_set|basketball_set}')
# all_list=[*french_set,*football_set,*art_set,*basketball_set]
# for s in all_list:
#     print(f'{s}选择了{all_list.count(s)}门课程')

# 字典dict,s={"建":"值","建":"值"}建不能重复能修改如果重复了后面的值就会覆盖前面的值,值可以
# dict1={'王林':670,'李慕婉':'680','徐立国':580,'韩立':680,'王林':700}
# print(dict1)
# print(type(dict1))
# print(dict1["王林"])
# # 打印多个值
# # keys=['王林','李慕婉','韩立']
# res=[dict1[k] for k in dict1.keys()]
# # res=[dict1[k] for k in keys]
# print(res)
# # 增删改查
# dict1['涛哥']='增加sb'
# scor=dict1.pop("韩立")
# dict1['徐立国']='修改'
# print(dict1)
# print('查找所有的keys',dict1.keys())
# print('查找所有vale',dict1.values())
# print('查找所有键值对',dict1.items())
# # 遍历
# for k in dict1.items():
#     print(f'{k[0]}:{k[1]}')

# shopping_cart={'大狗叫叫叫':{'price':2,'num':3}}
# menu = """
# ######### 购物车系统 #########
# #       1.添加购物车         #
# #       2.修改购物车         #
# #       3.删除购物车         #
# #       4.查询购物车         #
# #       5.退出购物车         #
# ############################
# """
#
# # 1.菜单
# print('欢迎使用购物车系统')
# while True:
#     print(menu)
#     # 2.具体操作
#     choice = input('请输入要执行的操作(1-5):')
#
#     match choice:
#         case "1":  # 添加购物车
#             goods_name = input("请输入物品名称")
#             if goods_name in shopping_cart:
#                 print("商品已存在")
#             else:
#                 goods_price = float(input("请输入商品价格"))
#                 goods_num = int(input("请输入商品数量"))
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("添加完毕")
#         case "2":  # 修改购物车
#             goods_name = input("请输入物品名称")
#             if goods_name in shopping_cart:
#                 goods_price = float(input("请输入商品新的价格"))
#                 goods_num = int(input("请输入商品新的数量"))
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             else:
#                 print("没有该商品")
#         case "3":  # 删除购物车
#             goods_name = input("请输入商品名称:")
#             if goods_name in shopping_cart:
#                 shopping_cart.pop(goods_name)
#                 print("删除成功")
#             else:
#                 print("没有该商品")
#         case "4":  # 查询购物车
#             for k in shopping_cart.keys():
#                 goods_info = shopping_cart[k]
#                 print(f"商品名称{k},商品价格{goods_info['price']},商品数量{goods_info['num']}")  # goods_info['num'].goods_info['price']
#         case "5":  # 退出购物车
#             break
#         case _:
#             print('操作不支持')


# menu="""
#  ######### 教务管理系统 ###########################
#  #   1.添加学生信息   2.修改学生信息  3.删除学生信息   #
#  #  4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出 #
#  ###############################################
# """
# infor={'王林':{'chinise':91,'math':92,'english':93},'煞星':{'chinise':19,'math':22,'english':83}}
# while True:
#     print(menu)
#     choice = input("请输入要执行的操作:")
#     match choice:
#         case '1':  # 1.添加学生信息
#             infor_name = input("请输入要添加的姓名:")
#             if infor_name in infor:
#                 print("学生信息已录入")
#             else:
#                 chinise_score =float(input("请输入语文成绩:"))
#                 english_score = float(input("请输入英语成绩:"))
#                 math_score = float(input("请输入数学成绩:"))
#                 infor[infor_name] = {'chinise': chinise_score, 'math': math_score, 'english': english_score}
#                 print("录入成功:")
#         case '2':  # 2.修改学生信息
#             infor_name = input("请输入要修改的姓名:")
#             if infor_name in infor:
#                 chinise_score = float(input("请输入语文成绩:"))
#                 english_score = float(input("请输入英语成绩:"))
#                 math_score = float(input("请输入数学成绩:"))
#                 infor[infor_name] = {'chinise': chinise_score, 'math': math_score, 'english': english_score}
#                 print("修改成功:")
#             else:
#                 print("学生信息不存在")
#         case '3':  # 3.删除学生信息
#             infor_name = input("请输入要删除的姓名:")
#             if infor_name in infor:
#                 infor.pop(infor_name)
#             else:
#                 print("学生不存在")
#         case '4':  # 4.查询学生信息
#             infor_name = input("请输入要查询的姓名:")
#             if infor_name in infor:
#                 infor_menu=infor[infor_name]
#                 print(f"学生:{infor_name},语文成绩{infor_menu['chinise']},数学成绩{infor_menu['math']},英语成绩{infor_menu['english']}")
#             else:
#                 print("学生不存在")
#         case '5':  # 5.列出所有学生
#             for k in infor.keys():
#                 print(f"学生:{k},语文成绩{infor[k]['chinise']},数学成绩{infor[k]['math']},英语成绩{infor[k]['english']}")
#         case '6':  # 6.统计班级成绩 最高最低分 平均分 infor={'王林':{'chinise':1,'math':2,'english':3}}
#             chinise_score=[infor[f]['chinise'] for f in infor.keys()]
#             math_score=[infor[f]['math'] for f in infor.keys()]
#             english_score=[infor[f]['english'] for f in infor.keys()]
#             print(type(chinise_score))
#             # print(f"英语最低分考了{min(english_score)},语文最低分考了{min(chinise_score)},数学最低分考了{min(math_score)}")
#             chinise_min=[name for name,score in infor.items() if score['chinise']==min(chinise_score)]
#             chinise_max=[name for name,score in infor.items() if score['chinise']==max(chinise_score)]
#             math_min=[name for name,score in infor.items() if score['math']==min(math_score)]
#             math_max=[name for name,score in infor.items() if score['math']==max(math_score)]
#             english_min=[name for name,score in infor.items() if score['english']==min(english_score)]
#             english_max=[name for name,score in infor.items() if score['english']==max(english_score)]
#             print(f"语文--{chinise_min}考最低分:{min(chinise_score)},{chinise_max}考最高分:{max(chinise_score)},平均分{sum(chinise_score)/len(chinise_score)}")
#             print(f"数学--{math_min}考最低分:{min(math_score)},{math_max}考最高分:{max(math_score)},平均分{sum(math_score)/len(math_score)}")
#             print(f"英语--{english_min}考最低分:{min(english_score)},{english_max}考最高分:{max(english_score)},平均分{sum(english_score)/len(english_score)}")
#         case '7':  # 7.退出
#             break
#         case _:
#             print("操作不支持")



