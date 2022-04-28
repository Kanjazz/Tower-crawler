import entityins
from kivy.uix.label import Label
import random
import menu

#[стоячий противник]
#=============================== 
def spawn_stay(self):
	inv = random.randrange (-1,2,2)
	size = (100*inv,100)
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,60)
	add_entity(self,entityins.Stay((posx,posy),size,round(self.enemylevel/1.3),inv))	
#===============================
   
#[движущийся противник]
#===============================
def spawn_move(self):
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,100)
	inv = random.randrange (-1,2,2)
	size = (100*inv,100)	
	add_entity(self,entityins.Move((posx, posy),(100,100),round(self.enemylevel/1.4),1))
#===============================

#[игрок]
#===============================
def spawn_player(self):
	add_entity(self,entityins.Player((450,700),(100,100),1))
	self.player = self._entity[0]			
	add_label(self,self.player)
	self.player._lvl = 1
	
	if self.name ==  'game':
		with self.canvas.after:
			self._movelesslabels.insert(0,Label(pos=(100,1800), font_name ='resources/fonts/dogica.ttf' ,font_size = '15sp'))
			self.height_count = self._movelesslabels[0]					
			self._movelesslabels.insert(1,Label(pos=(0,0), font_name ='resources/fonts/dogica.ttf',font_size = '20sp' ))
			self.invul_cooldown = self._movelesslabels[1]
			
			self._movelesslabels.insert(2,Label(pos=(400,1800), font_name ='resources/fonts/dogica.ttf',font_size = '15sp' ))
			self.ability_cooldown = self._movelesslabels[2]
			
			self._movelesslabels.insert(3,Label(pos=(700,1800), font_name ='resources/fonts/dogica.ttf',font_size = '15sp' ))
			self.money = self._movelesslabels[3]
			
			self._movelesslabels.insert(4,Label(text= self.version, pos=(200,0), font_name ='resources/fonts/dogica.ttf',font_size = '10sp' ))
#===============================

#[предметы]
#===============================
def spawn_loot(self):
	rand = random.randint(0,3) 
	if rand == 0:
		level = 0
	elif rand == 1:
		level=1
	elif rand == 2:
		level=2
	else:
		level=3
			
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,100)
	add_entity(self,entityins.Loot((posx, posy),level))
#===============================	

#[исчезающий противник]
#===============================
def spawn_fade(self):
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,100)
	inv = random.randrange (-1,1,2)
	size = (100*inv,100)
	add_entity(self,entityins.Fade((posx, posy),size,round(self.enemylevel/1.2),inv))
#===============================

def spawn_dead(self,pos,texture):
	add_entity(self,entityins.Dead(pos,texture))

#[платформа]
#===============================
def spawn_pad(self):
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,100)
	if random.randint(1,2) == 1:
		add_entity(self,entityins.Pad((posx, posy),1))
	else:
		add_entity(self,entityins.Thorns((posx, posy),1))
#===============================	

#[портал]
#===============================
def spawn_portal(self):
	posx = random.randrange (100,800,70)
	posy = random.randrange (1900,2500,100)
	size = (100,100)	
	add_entity(self,entityins.Portal((posx, posy),size))
#===============================

#[начальный экран]
#===============================
def spawn_begin(self):
	pad = entityins.Pad((450, 300),1)
	add_entity(self,pad)
	add_label(self,pad)

	for i in range(8):
		posx = random.randrange (100,800,70)
		posy = random.randrange (500,2500,60)
		inv = random.randrange (-1,2,2)
		size = (100*inv,100)
		stay =entityins.Stay((posx, posy),size,1,inv)
		add_entity(self,stay)
		add_label(self,stay)
#===============================	

#[начальный экран портала]
#===============================
def spawn_souls(self):
	for i in range(4):
		posx = random.randrange (100,800,70)
		posy = random.randrange (1900,2500,100)
		move = entityins.Move((posx, posy),(100,100),0,1)
		add_entity(self,move)
#===============================	


#[добавление объектов в множество]
#===============================
def add_entity(self, entity):
		
	self._entity.append(entity)
	self.canvas.add(entity._instruction)
#===============================	

#[добавление счетчика уровня]
#===============================
def add_label(self,entity):
	with self.canvas:	
		label = Label(pos=(entity.pos[0],entity.pos[1]-70),text=str(entity._lvl),font_name ='resources/fonts/dogica.ttf' )
		self._labels.append(label)	
#===============================     
 
#[удаление объектов]
#===============================
def remove_entity(self, entity):
	if entity in self._entity and not entity.type == 'player':
		self._entity.remove(entity)
		self.canvas.remove(entity._instruction)
#===============================
   