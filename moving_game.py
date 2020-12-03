from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.graphics import Rectangle
from kivy.graphics import Color 

class move(Widget):
    def __init__(self,**kwargs):
        super(move,self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,1,0.2,mode='rgba')
            self.rect =Rectangle(pos=(500,500),size=(50,50))

    def on_touch_down(self,touch):
        self.rect.pos=touch.pos

    def on_touch_move(self,touch):
        self.rect.pos=touch.pos

class mover(App):
    def build(self):
        return move()

if __name__=="__main__":
    mover().run()