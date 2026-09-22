class Car:
    def __init__(self,brand='品牌',model='型号',color='颜色',owner='所有者',charge='充能方式'):
        self.brand=brand
        self.model=model
        self.color=color
        self.__owner=owner

    def start(self):
        print(f"{self.brand}{self.model}正在启动...")

    def run(self):
        print(f"{self.brand}{self.model}正在行驶...")

    def stop(self):
        print(f"{self.brand}{self.model}停止...")

    def __control_fuel(self):
        print(f"{self.brand}{self.model}正在控制油门...")

    def get_owner(self):
        return self.__owner

    def charge(self):
        print(f"{self.brand}{self.model}正在充能...")

class ElectricCar():
    def __init__(self, brand='品牌', model='型号', color='颜色', owner='所有者', charge='充能方式'):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner
    def charge(self):
        print(f"{self.brand}{self.model}正在充电...")

class FuelCar():
    def __init__(self, brand='品牌', model='型号', color='颜色', owner='所有者', charge='充能方式'):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner
    def charge(self):
        print(f"{self.brand}{self.model}正在加油...")

def handle_charge(car):
    car.charge()
if __name__=='__main__':
    car=FuelCar('Audi','A6','黑色','王桑')
    #
    handle_charge(car)
    car = ElectricCar('Audi', 'A6', '黑色', '王桑')
    handle_charge(car)

