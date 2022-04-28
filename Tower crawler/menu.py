from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.screenmanager import NoTransition

import colliding as col

s = (0,0)

class Menu (Screen):

	def __init__(self, **kwargs):
		super(Menu,self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1/60)
		self._menu = []
		self._res = [
		'resources/gui/buttons/start.png',
		'resources/gui/buttons/credits.png',
		'resources/gui/buttons/right_arr.png',
		'resources/gui/buttons/left_arr.png',
		'resources/gui/menu/bkg.png']

			
	def update(self,dt):
		s = self.size
		if len(self._menu)==0 and s[0]>100:
			with self.canvas.before:
				self._menu.append(Rectangle(size=s,source=self._res[4]))
					
			with self.canvas:
				self._menu.append(Rectangle(size= (s[0]/2,s[0]/7), pos=(s[0]/2-s[0]/4,s[1]/4), source=self._res[0]))
					
				self._menu.append(Rectangle(size= (s[0]/2,s[0]/7), pos=(s[0]/2-s[0]/4,s[1]/6), source=self._res[1]))
					
	def on_touch_down(self, touch):
		if col.col(self,self._menu[1].pos, self._menu[1].size, (touch.x,touch.y),(1,1)):		
			if self.manager.current == 'menu':
				self.manager.transition = NoTransition()
				self.manager.current =  'game'
		elif col.col(self,self._menu[2].pos, self._menu[2].size, (touch.x,touch.y),(1,1)):
				self.manager.transition = NoTransition()
				self.manager.current = 'credits'
