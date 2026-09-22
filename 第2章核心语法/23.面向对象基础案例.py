"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已存在, 如果学生不存在, 再添加 (存在则, 不添加)
        1.3 验证成绩范围（0-100分）
        1.4 创建学生对象并添加到系统
    2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生, 显示该生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式为: "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
    5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""
# class Student:
#     def __init__(self,name,chinese,math,english):
#         self.name=name
#         self.chinese=chinese
#         self.math=math
#         self.english=english
#     def __str__(self):
#         return f'姓名:{self.name} | 语文成绩:{self.chinese} | 数学成绩:{self.math} | 英语成绩:{self.english}'
#     #修改成绩
#     def update_score(self, chinese = None, math = None, english = None):
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english
# # c1=Student("王林",30,40,50)
# # print(c1)
# # print(c1.update_score(100),c1)
#
# class EduManagement:
#     system_version="1.0"
#     system_name="教务系统"
#
#     def __init__(self):
#         self.student_list=[]
#     #添加学生
#     def add_student(self):
#         name=input("请输入学生姓名:")
#         for s in self.student_list:
#             if s.name==name:
#                 print('该学生已经存在',s)
#                 return
#         chinese=int(input("请输入学生语文成绩:"))
#         math=int(input("请输入学生数学成绩:"))
#         english=int(input("请输入学生英语成绩:"))
#         if 0<=math<=100 and 0<=chinese<=100 and 0<=english<=100:
#             stu = Student(name,chinese, math, english)
#             self.student_list.append(stu)
#             print("添加成功")
#         else:
#             print('成绩必须在0-100之间')
#     #修改成绩
#     def mou_student(self):
#         name = input("请输入要修改学生姓名:")
#         for s in self.student_list:
#             if s.name==name:
#                 print("当前成绩:",s)
#                 chinese = int(input("请输入学生语文成绩:"))
#                 math = int(input("请输入学生数学成绩:"))
#                 english = int(input("请输入学生英语成绩:"))
#                 if 0 <= math <= 100 and 0 <= chinese <= 100 and 0 <= english <= 100:
#                     s.update_score(chinese,math,english)
#                     print("修改成功")
#                     print("修改后成绩:",s)
#                     return
#                 else:
#                     print('成绩必须在0-100之间')
#                     return
#         print("未找到学生")
#     #删除学生
#     def delete_student(self):
#         name = input("请输入要删除学生姓名:")
#         for s in self.student_list:
#             if s.name==name:
#                 self.student_list.remove(s)
#                 print("删除成功")
#                 return
#         print('未找到该学生')
#     #查询指定学生
#     def query_student(self):
#         name = input("请输入要查询学生姓名:")
#         for s in self.student_list:
#             if s.name==name:
#                 print(s)
#                 return
#         print('未找到该学生')
#     # 打印所有学生
#     def all_student(self):
#         for s in self.student_list:
#             print(s)
#
#     def run(self):
#         print("欢迎使用教务系统")
#         while True:
#             print()
#             print("###################################################################")
#             print("#1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生 6.退出系统#")
#             print("###################################################################")
#             print()
#             choice=input("请输入要执行的操作,1-6:")
#             match choice:
#                 case "1":
#                     self.add_student()
#                 case "2":
#                     self.mou_student()
#                 case "3":
#                     self.delete_student()
#                 case "4":
#                     self.query_student()
#                 case "5":
#                     self.all_student()
#                 case "6":
#                     print("bye~")
#                     break
#                 case _:
#                     print("输入错误")


"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""
#购物车系统
class Goods:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.quantity}"
    #修改购物车
    def update_info(self,price=None,quantity=None):
        if price is not None:
            self.price=price
        if quantity is not None:
            self.quantity=quantity

class Shopping_cart():
    def __init__(self):
        self.goods_list=[]

    def add_goods(self):# 添加购物车
        name=input("请输入商品名称:")
        for s in self.goods_list:
            if s.name==name:
                print('要添加的该学生已经存在')
                return
        price=float(input("请输入商品价格:"))
        quantity=int(input("请输入商品数量:"))
        goods=Goods(name,price,quantity)
        self.goods_list.append(goods)
        print("商品添加成功")

    def mou_goods(self):#修改商品
        name=input("请输入要修改的商品名称:")
        for s in self.goods_list:
            if s.name==name:
                price =float(input("请输入商品价格:"))
                quantity = int(input("请输入商品数量:"))
                s.update_info(price,quantity)
                print('修改成功')
                return
        print("未找到要修改的商品")
    def delete_goods(self):#删除购物车
        name=input("请输入要删除的商品名称:")
        for s in self.goods_list:
            if s.name==name:
                self.goods_list.remove(s)
                print('删除成功')
                return
        print('未找到要删除的该商品')
    def query_goods(self):#查询商品
        name = input("请输入要查询的商品名称:")
        for s in self.goods_list:
            if s.name == name:
                print(s)
                return
        print('查找商品不存在')
    def all_goods(self):#打印所有商品
        for s in self.goods_list:
            print(s)

    def run(self):
        print("欢迎使用购物车系统")
        while True:
            print()
            print("###################################################################")
            print("#1.添加商品  2.修改商品  3.删除商品  4.查询指定商品  5.查询所有商品 6.退出系统#")
            print("###################################################################")
            print()
            choice=input("请输入要执行的操作,1-6:")
            try:
                match choice:
                    case "1":
                        self.add_goods()
                    case "2":
                        self.mou_goods()
                    case "3":
                        self.delete_goods()
                    case "4":
                        self.query_goods()
                    case "5":
                        self.all_goods()
                    case "6":
                        print("bye~")
                        break
                    case _:
                        print("输入错误")
            except ValueError:
                print("输入数据有问题,请重新输入!")
                continue
            except Exception:
                print("程序运行出错了,请重新输入!")
                continue


if __name__=="__main__":
    goods_management=Shopping_cart()
    goods_management.run()
    # edu_management=EduManagement()
    # edu_management.run()