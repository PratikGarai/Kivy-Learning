from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics','height',600)
Config.set('graphics','width',600)

class Layout(FloatLayout):
    pass

class MainApp(App):
    def build(self):
        return Layout()

if __name__=='__main__':
    MainApp().run()
