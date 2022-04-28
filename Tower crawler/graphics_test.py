from kivy.app import App
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Color,Line
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import  NumericProperty,ObjectProperty
from kivy.vector import Vector
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.atlas import Atlas
class Game(FloatLayout):
	before = ObjectProperty()
	after = ObjectProperty()
	line = ObjectProperty()
	at = Atlas('storage/emulated/0/kivy/Hello World/at.atlas')
	print(atlas.textures.keys())
	def __init__(self, **kwargs):
		super(Game,self).__init__(**kwargs)
	#	Clock.schedule_interval(self.update, 1/60)      
	#	texture = Image('test.png').texture  
		with self.canvas.before:
		#	self.before=Rectangle(source = at['player'],pos= (450,400),size = (100,100))
			self.before.pos = (450 -abs(self.before.size[0]/2),400)
			Color(1,0,1,1)

		
class App(App):
	def build (self):
		return Game()

if __name__ == '__main__':
    App().run()