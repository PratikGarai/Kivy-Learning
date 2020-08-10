import time
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text="Hello World")

    def on_start(self):
        print("Starting...")
        time.sleep(3)
        print("Started!")

    def on_stop(self):
        print("Closing...")
        time.sleep(3)
        print("Bye!")

if __name__=='__main__':
    MainApp().run()
