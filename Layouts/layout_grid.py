from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics','height',600)
Config.set('graphics','width',600)

Builder.load_file('layout_grid.kv')

class Layout(GridLayout):
    pass

class MainApp(App):
    def build(self):
        return Layout()

if __name__=='__main__':
    MainApp().run()
