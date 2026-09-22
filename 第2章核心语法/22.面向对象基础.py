# # 定义类,方法一:一般不用
# class Car:
#     pass
# c1 = Car()
# print(c1)
# c1.color = '绿色'
# c1.brand = 8000
# c1.name = 'X7'
# print(c1.__dict__)
# # 常用方法
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print('初始化,对象属性添加完毕')
# c1=Car("红","BWM","X7",80000)
# print(c1.__dict__)
# c2=Car('黑','奔驰','e300',300000)
# print(c2.__dict__)

# 定义调用实例方法
class Car:
    wheel=4
    tax_rate=0.15
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
    def running(self):
        print(f"{self.color} {self.name}正在行驶")
    def total_cost(self,dis,rt):
        return self.price*dis + self.price*rt
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price
    def __lt__(self, other):
        return self.price < other.price
c1=Car('红','法拉利','法911',3000000)
c1.running()
print(f"提车落地价:",c1.total_cost(0.9,0.1))
#调用魔法方法字符串__str__,等于__eq__,大于,大于等于__lt,le__
c2=Car('红','法拉利','法911',3000000)
print(c1)
print(c1<c2)
print(c1==c2)
# 添加并调用类属性
# 通过对象访问实列属性,没有就会在类里面找类属性
print("实列属性里面没有就会在类属性里面找wheel:",Car.wheel)
print(Car.tax_rate)

