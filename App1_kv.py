import kivy 
from kivy.app import App

class MainApp(App):
    pass

if __name__=="__main__":
    M = MainApp()
    M.load_kv('App1_kv.kv')
    M.run()
