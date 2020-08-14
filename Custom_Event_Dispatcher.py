from kivy.app import App
from kivy.uix.button import Button
from kivy.event import EventDispatcher

class MyEventDispacther(EventDispatcher):

    def __init__(self, **kwargs):
        # register the name of the event
        self.register_event_type('callback')
        super(MyEventDispacther,self).__init__(**kwargs)

    def some_trigger(self, value):
        # calling this methos will trigger the event
        # with the given value
        self.dispatch('callback', value)

    def callback(self, *args):
        print("The event was dispatched ",args)
