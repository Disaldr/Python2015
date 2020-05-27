class car:
    def __init__(self, marka, speed):
        self.marka = marka
        self.speed = speed
        self.odometr = 0

    def ride(self):
        return self.marka+" едет со скоростью " + str(self.speed)

    def read_odometr(self):
        print("Пробег: " + str(self.odometr))


if __name__=='__main__':
    mashina = car('lada', 100)
    mashina.odometr = 100
    mashina.read_odometr()