from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import  ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from kivy.graphics import Rectangle
s = (0,0)
class Dev (Screen):

	rect1 = ObjectProperty()
	rect2 = ObjectProperty()
	rect3 = ObjectProperty()
	rect4 = ObjectProperty()
	label = ObjectProperty()
	t = 0

	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		with self.canvas:
			self.label = Label(font_name ='resources/fonts/dogica.ttf')
			self.rect1= Rectangle(size=(0,0),source='resources/icons/py3.png' )
			self.rect2= Rectangle(size=(0,0),source='resources/icons/kivy.png' )
			self.rect3= Rectangle(size=(0,0),source='resources/icons/pixitracker.png' )
			self.rect4= Rectangle(size=(0,0),source='resources/icons/pixelstudio.png' )
		Clock.schedule_interval(self.update, 1/30)   
		
	def update(self,dt):
		s = self.size
		
		if self.manager.current=='dev' and s[0]>100:
			self.label.text = 'created with'
			self.rect1.size = (300,300)
			self.rect2.size = (300,300)
			self.rect3.size = (300,300)
			self.rect4.size = (300,300)
			self.label.size = (400,400)
			
			self.rect1.pos=(s[0]/3-self.rect1.size[0]/2,s[1]/2)
			self.rect2.pos=(s[0]*2/3-self.rect2.size[0]/2,s[1]/2)
			self.rect3.pos=(self.rect1.pos[0],self.rect1.pos[1]-500)
			self.rect4.pos=(self.rect2.pos[0],self.rect2.pos[1]-500)
			self.label.pos=(s[0]/2-self.label.size[0]/2,s[1]/2+250)
			self.t+=1
	
			if self.t > 60*4 and not self.rect1.source == 'resources/icons/logo.png':
				self.label.text= 'developed by'
				self.rect1.source = 'resources/icons/logo.png'
				self.rect1.size=(600,600)
				self.rect1.pos=(s[0]/2-300,s[1]/2-200)
				self.rect2.size=(0,0)
				self.rect3.size=(0,0)
				self.rect4.size=(0,0)
			if self.t > 60*6:
				self.manager.transition = FadeTransition()
				self.manager.current =  'menu'
			
	def on_touch_down(self, touch):
		self.manager.transition = FadeTransition()
		self.manager.current =  'menu'