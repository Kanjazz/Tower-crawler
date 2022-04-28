from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.screenmanager import NoTransition

class Credits (Screen):
	def __init__(self, **kwargs):
		super(Credits,self).__init__(**kwargs)
		with self.canvas:
			Label(pos=(450,800),text='Code : Kanjazz \n Visual : Kanjazz \n Music : Kanjazz',font_name ='resources/fonts/dogica.ttf' )
			
	def on_touch_down(self, touch):
		self.manager.transition = NoTransition()
		self.manager.current =  'menu'