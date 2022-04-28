from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import  NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
import random
import math

import animations as anim
import colliding as col
import spawn as sp
import deathscreen as ds

import menu

#НАЧИНКА УРОВНЯ
#‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
class Game(Screen):
	version = 'v. indev 081121'
	vx=NumericProperty(0)
	vy=NumericProperty(0)
	velocity = ReferenceListProperty (vx,vy)
	score = ''
	pre_type = ''
	pre_source = None
	count = 0
	money_count = 0
	invul_time = 0
	player = ObjectProperty()
	reset = ObjectProperty()
	height_count = ObjectProperty()
	invul_cooldown = ObjectProperty()
	ability_cooldown = ObjectProperty()
	money = ObjectProperty()
	enemylevel = 0
	px=0
	py=0
	pos_p = 0
	at = 0#количество кадров до перезапуска умения
	menu = False
	s=(0,0)
	anim_name = ''
		
#[инициация основных параметров]
#===============================
	def __init__(self, **kwargs):
		anim.uploading_sprites()
		self.pre_type = 'player'
		self.pre_source = (anim.sprites['player'])['player']
		super().__init__(**kwargs)
		self._entity = []
		self._labels = []
		self._bkg = []
		self._movelesslabels = []
		sp.spawn_player(self)
		sp.spawn_begin(self)
		Clock.schedule_interval(self.update, 1/60)   
#===============================
	
#[функция обновления событий]
#===============================
	def update(self, dt):
		if self.manager.current ==  'game':
			self.s = self.size
			self.vy -=0.5
			self.p_move(self)
			self.col_pl(self)
			self.scr_move(self)
			self.side_move(self)
			self.money_counter()
			self.height_counter(self)			
			self.invul_timer(self, self.player._type)
			self.enemylevel = math.floor(pow(self.count/10+1,1.1))
			self.dead_fall(self)
			self.skin_change(self, self.player._type, self.player.texture)
			self.underfall(self.player.pos[1])
			self.ability_timer()
			self.animation()
			self.player_animation()
#===============================			

#[анимирование спрайтов противников]			
#===============================			
	def animation(self):
		for e in self._entity:
			if e._atype == 0:
				if random.randint(0,100) < 1:
					e._atype = 1
					if e._type == 'fade':
						if random.randint(0,3)<2:
							e._atype = 2
						else:
							e._atype = 1
			
			if e._atype > 0 and not e == self.player and not e._type == 'pad' and not e._type == 'thorns':
						
						e._atime += 1
						if e._atype == 1:
							if e._type == 'stay':
								self.anim_name = 'stay blink'
									
							elif e._type == 'move':
								self.anim_name = 'move'
									
							elif e._type == 'fade':
								self.anim_name = 'mage blink'
								
							elif e._type == 'sword':
								self.anim_name = 'sword blink'
									
							elif e._type == 'potion':
								self.anim_name = 'potion blink'
								
							elif e._type == 'armor':
								self.anim_name = 'armor blink'
								
							elif e._type == 'gold':
								self.anim_name = 'gold blink'
								
						elif e._atype == 2:
							self.anim_name = 'fade'
							
						elif e._atype == -1:
							if (math.floor(e._atime/10))%2 ==0:
								e.size = (0,0)
							else:
								e.size =(100,100)
							
						try:
							e.texture = anim.animate(self.anim_name,math.floor(e._atime/10))
						except IndexError:
							e._atime = 0
							if not e._type =='move':
								e._atype = 0		
#===============================		

#[анимирование персонажа]
#===============================		
	def player_animation(self):
		if not self.player.type == 'ability':
			if self.player.type == 'player':
				if self.vy < 0:
					self.player.texture = (anim.sprites['player'])['player jump']
				else:
					self.player.texture = (anim.sprites['player'])['player']
					
			elif self.player.type == 'invul':
				if self.vy < 0:
					self.player.texture = (anim.sprites['player'])['invul jump']
				else:
					self.player.texture = (anim.sprites['player'])['invul']
					
			elif self.player.type == 'armored':
				if self.vy < 0:
					self.player.texture = (anim.sprites['player'])['armored jump']
				else:
					self.player.texture = (anim.sprites['player'])['armored']	
#===============================		
	
#[проверка падения игрока за пределы экрана]
#===============================
	def underfall(self, position):
			if position<=-100:
				self.player._type='dead'
#===============================
	
#[изменение спрайта персонажа]
#===============================
	def skin_change(self, dt, type, texture):
		if type == 'dead':
			self.player.texture  = (anim.sprites['player'])['dead']
			try:
				if not self._movelesslabels[5] == None:
					pass
			except IndexError:
				ds.screen(self)
				self.menu = True

		elif type == 'ability':
			if self.vy <0:
				self.player._type = self.pre_type
				self.player.texture = self.pre_source
			else:
				self.player.texture = (anim.sprites['player'])['ability']	
#===============================

#[счётчик высоты]
#==============================
	def height_counter(self,dt):
		if not self.player._type == 'dead':
			if self.vy > 0:
				self.count += .5
			else:
				self.count -= .25
				
		if self.count > 0:
			self.height_count.text = str(math.floor(self.count))
		else:
			self.count = 0
#===============================

#[таймер отката неуязвимости]
#===============================
	def invul_timer(self, dt, type):
		if self.invul_time > 0:
			self.invul_time -= 1
			
		elif self.invul_time == 0:
			self.invul_time = -1
			self.player._type = self.pre_type
			self.player.texture = self.pre_source
		
		if self.invul_time > 0:
			self.invul_cooldown.text = str(math.floor(self.invul_time/60))
			self.invul_cooldown.pos =(self.player.pos[0]+self.player.size[0]/2-self.player.size[0]/2*self.player._invert,self.player.pos[1]+110)
		else:
			self.invul_cooldown.text = ''
#==============================

#[таймер отката способности]
#===============================
	def ability_timer(self):
		if self.at > 0:
			self.at -= 1	
			self.ability_cooldown.text = str(math.floor(self.at/60))
			
		elif self.at == 0:
			self.at = -1
			
		else:
			self.ability_cooldown.text = 'Ready!'
#==============================

#[счетчик денег]
#===============================
	def money_counter(self):
		self.money.text = str(self.money_count)
#===============================

#[перемещение движущихся противников]
#==============================
	def side_move(self,dt):
		for e in self._entity:
			if e._type == 'move' and e._atype == 1:
				if (e.pos[0] <100 and e._invert == -1) or (e.pos[0]>1000 and e._invert == 1):
					e._invert = -e._invert
					e.size = (-e.size[0],e.size[1])
				e.pos = e._invert*Vector(*(10,0)) + e.pos		
#==============================

#[падение мертвых противников]
#==============================
	def dead_fall(self,dt):
		for e in self._entity:
			if e._type == 'dead_ent':
				e.pos = Vector(*(0,-10))+e.pos
				if e.pos[1] < 0:
					sp.remove_entity(self,e)
#==============================

#[движение игрока] 
#===============================
	def p_move(self, dt):
		if self.player.pos[1]>-100:
			self.player.pos = Vector(*(self.vx,0))+self.player.pos
				
		if self.player.pos[1] <= 1200 or self.vy <0:
				self.player.pos = Vector(*(0,self.vy))+self.player.pos
#===============================
  
#[движение экрана]
#===============================
	def scr_move(self,dt):		
		if self.vy >0:
#			for b in self._bkg:
#				b.pos =  -Vector(*self.velocity)*3+b.pos
#				if b.pos[1] <= -2500:
#					b.pos=(0,4998)
			for e in self._entity:
				if not e == self.player:
					e.pos =  -Vector(*self.velocity)*3+e.pos
	
					if e.pos[1]< -50:
						sp.remove_entity(self,e)
						if len(self._entity) <= 10:
							if random.randint(0,100) < 50:
								sp.spawn_stay(self)
							elif random.randint(0,100) < 60:
								sp.spawn_move(self)
							elif random.randint(0,100) < 60:
								sp.spawn_fade(self)
							elif random.randint(0,100) < 60:
								sp.spawn_pad(self)
							elif random.randint(0,100)<1:
								sp.spawn_loot(self)
							else:
								sp.spawn_portal(self)
								
				else: pass
		try:
			i=0
			while i < 10:
				position = self._entity[i].pos
				size = self._entity[i].size[0]		
				inv = self._entity[i]._invert
				self._labels[i].pos = (position[0]+size/2-size/2*inv,position[1]-70)
				if self._entity[i].lvl == 0:
					self._labels[i].text = ''
				else:
					self._labels[i].text = str(self._entity[i].lvl)
				i+=1
		except IndexError:
			pass
#===============================

#[событие столкновений с игроком]
#===============================
	def col_pl(self, entity):
		for e in self._entity:
			if not e._type == self.player._type and not self.player._type == 'dead':		
				for i in self._entity:
					if not i == e and col.col(col,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),(abs(e.size[0]),e.size[1]), (i.pos[0]+i.size[0]/2-i.size[0]/2*i._invert,i.pos[1]),(abs(i.size[0]),i.size[1])) and not e._type == 'dead_ent' and not i._type == 'dead_ent' and  not i._type == self.player._type and not e._type == 'move' and not i._type == 'move':
						e.pos = (-100,-100)
				
				if col.col(col,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),(abs(e.size[0]),e.size[1]), (self.player.pos[0]+self.player.size[0]/2-self.player.size[0]/2*self.player._invert,self.player.pos[1]),(abs(self.player.size[0]),self.player.size[1])) and (self.vy<0 or self.player._type == 'ability') and not e.texture == (anim.sprites['misc'])['null']:
				
					if not self.player._type == 'ability':
						self.vy = 15						
						
					if e._type == 'sword':
						self.player._lvl += e._lvl		
						e._lvl = 0
						e._type = 'pad'
						e.texture = (anim.sprites['misc'])['pad']
						
					elif e._type == 'armor' :
						if self.player._type == 'invul':
							self.pre_type = 'armored'
							self.player._type = 'invul'
							self.player.texture = (anim.sprites['player'])['invul armored']
						else:
							self.pre_type = self.player._type
							self.player._type = 'armored'
							self.pre_source = self.player.texture
							self.player.texture =  (anim.sprites['player'])['armored']
						e._lvl = 0
						e._type = 'pad'
						e.texture =  (anim.sprites['misc'])['pad']
				
					elif e._type == 'potion' :
						self.pre_source = self.player.texture
						if self.player._type == 'armored':
							self.player.texture =  (anim.sprites['player'])['invul armored']
						else:
							self.player.texture = (anim.sprites['player'])['invul']
						self.pre_type = self.player._type
						self.player._type = 'invul'
						self.invul_time = 300
						e._lvl = 0
						e._type = 'pad'
						e.texture =  (anim.sprites['misc'])['pad']
						
					elif e._type == 'gold':
						self.money_count +=10
						e._type = 'pad'
						e.texture =  (anim.sprites['misc'])['pad']
						
					elif e._type == 'portal':
						self.manager.transition = NoTransition()
						self.manager.current =  'mini'
						
					elif e._type == 'pad':
						sp.spawn_dead(self,e.pos,  (anim.sprites['misc'])['broken'])
						e.size = (0,0)
						e.pos= (0,0)

					elif e._type == 'thorns':
						if self.player._type == 'player':						
							self.player._type = 'dead'
						elif self.player._type == 'armored':
							self.player._type = 'player'
							self.player.texture =  (anim.sprites['player'])['player']
							sp.spawn_dead(self,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),(anim.sprites['player'])['broken'])
						
					if self.player._lvl >= e._lvl or self.player._type == 'invul' or self.player._type == 'ability':
						if e._type == 'stay':
							sp.spawn_dead(self,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),  (anim.sprites['enemy'])['stay dead'])
							self.player._lvl += 1
							self.money_count +=1
							e._lvl = 0
							e.texture =  (anim.sprites['misc'])['pad']
							e._type = 'pad'
					 
						elif e._type == 'fade':
							sp.spawn_dead(self,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),  (anim.sprites['enemy'])['mage dead'])
							self.player._lvl += 1
							self.money_count +=2
							e._lvl = 0
							e.texture =  (anim.sprites['misc'])['pad']
							e._type = 'pad'
						
						elif e._type == 'move':
							sp.spawn_dead(self,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]), (anim.sprites['enemy'])['move dead'])
							self.player._lvl += 1
							self.money_count +=1
							e.size = (0,0)
							e._lvl = 0
					
					elif self.player._type == 'armored' and self.player._lvl < e._lvl:
							self.player._type = 'player'
							self.player.texture =  (anim.sprites['player'])['player']
							sp.spawn_dead(self,(e.pos[0]+e.size[0]/2-e.size[0]/2*e._invert,e.pos[1]),((anim.sprites['player'])['broken']))
					
					else:
						self.player._type = 'dead'
#===============================
			
#[действия при касании экрана]
#===============================
	def on_touch_down(self, touch):

		if (self.menu and col.col(col,(450,600),(500,500),(touch.x,touch.y),(0,0))):
			self.canvas.clear()
			self.canvas.after.clear()
			self._entity.clear()
			self._labels.clear()
			self._movelesslabels.clear()
			sp.spawn_player(self)
			sp.spawn_begin(self)
			self.player.pos = (450,500)
			self.count = 0
			self.money_count = 0	
			self.at = 0
			self.menu=False
		
		if self.manager.current == 'game' and not self.menu:
			self.pos_p = self.player.pos[0]-touch.x
			self.px = touch.x
			self.py = touch.y
			
			if touch.is_double_tap and self.at == -1 and not self.player._type == 'dead':
				if self.player._type == 'armored':
					self.player.texture =  (anim.sprites['player'])['ability armored']
				else:
					self.player.texture =  (anim.sprites['player'])['ability']
				self.pre_type = self.player._type
				self.player._type = 'ability'
				
				self.vy = 30
				self.at = 960
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