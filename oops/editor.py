from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def Run(self):
        pass
    @abstractmethod
    def Debug(self):
        pass
    @abstractmethod
    def Edit(self):
        pass
    @abstractmethod
    def Save(self):
        pass

class Vscode(Editor):

    def Run(self):
        print("code run")

    def Debug(self):
        print("its debug")

    def Edit(self):
        print("its edit")
   
    def Save(self):
        print("its save")

obj=Vscode()
obj.Run()