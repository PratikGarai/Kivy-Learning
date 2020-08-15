from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ListProperty

class CustomLabel(Label):
    n = ListProperty([-1,-1])

    def __init__(self, **kwargs):
        self.text = str(self.n)
        super(CustomLabel, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.n = list((int(touch.pos[0]), int(touch.pos[1])))
            return True
        return super(CustomLabel, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.n = [-1,-1]
            return True
        return super(CustomLabel, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.n = list((int(touch.pos[0]), int(touch.pos[1])))
            return True
        return super(CustomLabel, self).on_touch_move(touch)

    def on_n(self, instance, pos):
        self.text = str(self.n)

class MainApp(App):
    def build(self):
        a = CustomLabel()
        a.bind(n=self.my_n_handler)
        return a

    def my_n_handler(self, instance, pos):
        # print("Instance : ", instance, "\tPos : ", str(pos))
        instance.text = instance.text+" External Handler present too"

if __name__=='__main__':
    MainApp().run()
