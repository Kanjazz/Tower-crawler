from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Rotate
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import  NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock

import spawn as sp
import animations as anim
import colliding as col

class Mini(Screen):
	version = 'v. indev 081121'
	vx=NumericProperty(0)
	vy=NumericProperty(0)
	velocity = ReferenceListProperty (vx,vy)
	player = ObjectProperty()
	s=(0,0)
	px=0
	py=0
	pos_p = 0
	enemylevel = 0
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._entity = []
		self._labels = []
		self._bkg = []
		self._movelesslabels = []
		sp.spawn_player(self)
		sp.spawn_souls(self)
		self.player.pos = (450,900)
		
		Clock.schedule_interval(self.update, 1/60)
		
	def update(self, dt):
		self.s = self.size
		if self.manager.current == 'mini':
			self.p_move(self)
			self.col_pl(self)
			self.enemy_move(self)
		
#[анимирование спрайтов противников]			
#===============================			
	def animation(self):
		for e in self._entity:
			if e._type == 'move':
				self.anim_name = 'move'
						
				
#[движение игрока] 
#===============================
	def p_move(self, dt):
		if self.player.pos[1]>-100:
			self.player.pos = Vector(*(self.vx,0))+self.player.pos
#===============================

 #[движение противников]
#==============================
	def enemy_move(self,dt):
		for e in self._entity:
			if not e == self.player:
				e.pos = Vector(*(0,-30))+e.pos
				if e.pos[1]< -50:
					sp.remove_entity(self,e)
					if len(self._entity) <= 5:
						sp.spawn_move(self)
#==============================

#[взаимодействие с игроком]
#==============================
	def col_pl(self, entity):
		for e in self._entity:
			if col.col(col,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),(abs(e.size[0]),e.size[1]), (self.player.pos[0]+self.player.size[0]/2-self.player.size[0]/2*self.player._invert,self.player.pos[1]),(abs(self.player.size[0]),self.player.size[1])):
				pass
			#	self.manager.transition = NoTransition()
				#self.manager.current =  'game'
#==============================

#[действия при касании экрана]
#===============================
	def on_touch_down(self, touch):
		self.pos_p = self.player.pos[0]-touch.x
		self.px = touch.x
		self.py = touch.y
#===============================
	
#[действия при передвижении пальца]
#===============================
	def on_touch_move(self, touch):
		if not self.player._type == 'dead':
#если игрок двигается влево
			if touch.x+5< touch.px:
				self.player.size = (-100,100)
				self.player._invert = -1
				
				if self.player.pos[0] > 100:
					self.player.pos = (self.pos_p+touch.x-self.player.size[0]/2,self.player.pos[1])
				else:
					self.player.pos = (100,self.player.pos[1])
					
#если игрок двигается вправо
			elif touch.x-5> touch.px:
				self.player.size = (100,100)
				self.player._invert = 1
				
				if self.player.pos[0]+self.player.size[0] < self.s[0]:
					self.player.pos = (self.pos_p+touch.x-self.player.size[0]/2,self.player.pos[1])
					
				else:
					self.player.pos=(self.s[0]-self.player.size[0],self.player.pos[1])
#===============================
#‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡