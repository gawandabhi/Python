from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self): pass
    
class Check(ABC):
    @abstractmethod
    def check(self): pass    

class WindowButton(Button):
    def click(self):
        print("Click window Button")
        
class WindowCheck(Check):
    def check(self):
        print("Check window checkbox")
                   
class MacButton(Button):
    def click(self):
        print("Click window Button")
        
class MacCheck(Check):
    def check(self):
        print("Check window checkbox")   
        

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:pass 
    @abstractmethod
    def create_check(self) -> Check:pass                      
    
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowButton()
    def create_check(self):
        return WindowCheck()
           
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_check(self):
        return MacCheck()  
    
def render_ui(factory:GUIFactory):
    button = factory.create_button()
    Check = factory.create_check()
    button.click()
    Check.check()
    
windows_factory = WindowsFactory()
render_ui(windows_factory)

mac_factory = MacFactory()
render_ui(mac_factory)             
           
           