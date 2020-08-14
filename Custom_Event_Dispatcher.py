from kivy.event import EventDispatcher

class MyEventDispacther(EventDispatcher):

    def __init__(self, **kwargs):
        # register the name of the event
        # the name must begin with on_ 
        self.register_event_type('on_callback')
        super(MyEventDispacther,self).__init__(**kwargs)

    def some_trigger(self, value):
        # calling this methos will trigger the event
        # with the given value
        self.dispatch('on_callback', value)

    def on_callback(self, *args):
        print("The event was dispatched ",args)

# Driver code

def my_callback(valuse, *arge):
    print("This is the sample callback driver")

evd = MyEventDispacther()
evd.bind(on_callback=my_callback)
evd.some_trigger('Test value')
