from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def accelarator():
        print("Car speeds up")

    def brakes():
        print("Car Slows down")

    def gear(change):
        print(f"Gear {change}")

class TataNano(Car):
    def accelarator(self):
        print("Tata Nano tries to Speed up")
    def brakes(self):
        print("Tata Nano Crashed, it has no brakes")
    def gear(self,change):
        print("Gear",change)
class MarutiSuzuki(Car):
    def accelarator(self):
        print("MS Speed up")
    def brakes(self):
        print("MS stops")
    def gear(self,change):
        print("Gear",change)

nano=TataNano()
nano.accelarator()
nano.brakes()
nano.gear('up')
nano.gear('down')
MS=MarutiSuzuki()
MS.accelarator()
MS.brakes()
MS.gear('up')
MS.gear('down')