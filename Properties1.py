from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button

class CustomButton(Button):
    txt = StringProperty('Up')

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text="Ready"

    #trigger if button is pressed, change the property
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.txt = "Down"
            return True
        return super(CustomButton, self).on_touch_down(touch) #repropagate
        
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.txt = "Up"
            return True
        return super(CustomButton, self).on_touch_up(touch) #repropagate

    def on_txt(self, instance, pos):
        self.text=self.txt
        

class MainApp(App):
    def build(self):
        return CustomButton()

if __name__=="__main__":
    MainApp().run()
