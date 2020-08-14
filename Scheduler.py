from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import time

class MainApp(App):

    def build(self):

        def schedule_interval_event(qw):
            print("This is the schedule interval ",qw)

        def schedule_interval_once_event(qw):
            print("This is the once scheduled event ",qw)
        def trig_callback(qw):
            print("This is the trigger callback",qw)

        trigger = Clock.create_trigger(trig_callback)
        trigger()

        Clock.schedule_interval(schedule_interval_event, 1)
        Clock.schedule_once(schedule_interval_once_event, 3)
        return Label(text="Events")

if __name__=='__main__':
    MainApp().run()
