import objins
import labins 
import random
import animations as anim
#стоячий противник
class Stay(objins.Entity):
	def __init__(self, pos, size, lvl,inv): 
		super().__init__()
		self.pos = pos
		self.texture = (anim.sprites['enemy'])['stay']
		self._type = 'stay'
		self._lvl = lvl
		self._invert = inv
		self.size = size
		
#перемещающийся противник
class Move(objins.Entity):
	def __init__(self,pos,size,lvl,inv): 
		super().__init__()
		self.pos = pos
		self.size = size
		self.texture = self.texture = (anim.sprites['enemy'])['move']
		self._type = 'move'
		self._lvl = lvl
		self._invert = inv
		self._atype = 1
		

#игрок
class Player(objins.Entity):
	def  __init__(self, pos,size,inv):  
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.texture = (anim.sprites['player'])['player']
		self._type = 'player'
		self._invert = inv
		
#показатель уровня
class Label(objins.Entity):
	def  __init__(self, pos,lvl,type):  
		super().__init__()
		self.pos = pos
		self.text = lvl
		self._type = type

#предметы
class Loot(objins.Entity):
	def __init__(self, pos,lvl): 
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		rand = random.randint(0,9) 
		self._atype = 0
		
		if rand == 0:
			self.texture = self.texture = (anim.sprites['misc'])['gold']
			self._type = 'gold'
			self._lvl = 0
		
		if rand >=1 and rand < 4:
			self.texture = self.texture = (anim.sprites['misc'])['sword']
			self._type = 'sword'
			self._lvl = lvl
			
		elif rand >=4 and rand < 6: 
			self.texture = self.texture = (anim.sprites['misc'])['potion']
			self._type = 'potion'
			self._lvl = 0
			
		elif rand >= 6 and rand <= 9: 
			self.texture =self.texture = (anim.sprites['misc'])['armor']
			self._type = 'armor'
			self._lvl = 0

#исчезающий противник
class Fade(objins.Entity):
	def __init__(self, pos,size,lvl,inv): 
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.texture = self.texture = (anim.sprites['enemy'])['mage']
		self._type = 'fade'
		self._lvl = lvl

#шипы
class Thorns(objins.Entity):
	def __init__(self, pos,inv): 
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.source = self.texture = (anim.sprites['misc'])['thorns']
		self._type = 'thorns'
		self._lvl = 0
		self._invert = inv
		self._atype = -1

#платформа
class Pad(objins.Entity):
	def __init__(self, pos,inv): 
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.texture =self.texture = (anim.sprites['misc'])['pad']
		self._type = 'pad'
		self._lvl = 0
		self._invert = inv
		self._atype = -1

#мертвый объект
class Dead(objins.Entity):
	def __init__(self, pos,texture): 
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.texture = texture
		self._type = 'dead_ent'
		self._lvl = 0
		self._atype = -1

#портал
class Portal(objins.Entity):
	def  __init__(self, pos,size):  
		super().__init__()
		self.pos = pos
		self.size = (100,100)
		self.texture = (anim.sprites['enemy'])['portal']
		self._type = 'portal'