class Car:
    def __init__(self,brand='品牌',model='型号',color='颜色',owner='所有者'):
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

class ElectricCar(Car):
    pass

class FuelCar(Car):
    pass

if __name__=='__main__':
    car=FuelCar('Audi','A6','黑色','王桑')

    print(car.brand)

    print(car._Car__owner)  # 强制访问，实际开发中不推荐使用
    car._Car__control_fuel()

    car.start()
    car.run()
    car.stop()
    print(car.get_owner())