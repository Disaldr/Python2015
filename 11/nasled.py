class car:
    """Базовый класс автомобиля"""
    def __init__(self, marka, speed, litrazh):
        self.marka = marka
        self.speed = speed
        self.litrazh = litrazh
        self.odometr = 0

    def ride(self):
        return self.marka+" едет со скоростью " + str(self.speed)

    def read_odometr(self):
        print("Пробег: " + str(self.odometr))



class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def show_capacity(self):
        print("Аккумулятор заряжен на " + str(self.capacity))

    @staticmethod
    def info():
        print("Класс, отвечающий за батарею электромобиля")



class ElectricCar(car):
    """
        Класс автомобиля с электродвигателем
    """
    def __init__(self, marka, speed, capacity):
        """Инициализация атрибутов класса-родителя"""
        super().__init__(marka, speed, None)
        self.capacity = capacity
        self.battery = Battery(self.capacity)


Battery.show_capacity()


a = set()