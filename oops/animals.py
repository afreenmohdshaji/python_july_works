class Animals:
    def __init__(self,name):
        self.name=name
    def sounds(self):
        pass

class Dog(Animals):
    def sounds(self):
        print(f"{self.name} barks")
    def __str__(self):
        return self.name
    
class Frog(Animals):
    def sounds(self):
        print(f"{self.name} croaks")
    def __str__(self):
        return self.name
    
dbj=Dog("Dog")
dbj.sounds()
fbj=Frog("Frog")
fbj.sounds()
print(fbj)