class Editor:
    def __init__(self,name):
        self.name=name
    def spec(self):
        pass

class VsCode(Editor):
    def spec(self):
        print(f"{self.name} has debug , run , support and create")
    
    def __str__(self):
        return self.name
    
class Pycharm(Editor):
    def spec(self):
        print(f"{self.name} has debug , run , support.")
    
    def __str__(self):
        return self.name



vbj=VsCode("Vscode")
vbj.spec()
print(vbj)
pbj=Pycharm("Pycharm")
pbj.spec()
