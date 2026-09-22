class Car:
    def __init__(self, brand='品牌', model='型号', color='颜色', owner='所有者'):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner

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


class HuaweiAiDriving:
    def __init__(self,version='V1.0'):
       self.version = version

    def run(self):
        print(f"{self.version}系统正在自动驾驶...")


class WenJieCar(Car,HuaweiAiDriving):
    def __init__(self, brand='品牌', model='型号', color='颜色', owner='所有者', version='V1.0'):
        super().__init__(brand, model, color, owner)
        HuaweiAiDriving.__init__(self,version)

    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)


if __name__ == '__main__':
    car = WenJieCar('Audi', 'A6', '黑色', '王桑')
    car.run()

    print(WenJieCar.mro())