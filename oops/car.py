from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def start(self):
        print("starts car ")
    def accelerate(self):
        print("acclerate the car")
    def stop(self):
        print("car stops")

obj=Swift()
obj.start()
