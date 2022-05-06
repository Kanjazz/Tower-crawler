from kivy.graphics import Rectangle

class Entity(object):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._pos = (0, 0)	
		self._size = (100, 100)
		self._texture = None
		self._invert = 1
		self._lvl = 0
		self._atime = 0
		self._atype = 0
		self._type = 'none'
		self._rotate = 0
		self._instruction = Rectangle( 
		pos=self._pos,
		size=self._size, 
		texture=self._texture,
		invert = self._invert,
		lvl = self._lvl,
		type = self._type,
		atype = self._atype,
		atime = self._atime)

	@property
	def pos(self):
		return self._pos

	@pos.setter
	def pos(self, value):
		self._pos = value
		self._instruction.pos = self._pos
        
	@property
	def invert(self):
		return self._invert

	@invert.setter
	def invert(self, value):
		self._invert = value
		self._instruction.invert = self._invert

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		self._size = value
		self._instruction.size = self._size

	@property
	def texture(self):
		return self._texture

	@texture.setter
	def texture(self, value):
		self._texture = value
		self._instruction.texture = self._texture
		
	@property
	def lvl(self):
		return self._lvl

	@lvl.setter
	def lvl(self, value):
		self._lvl = value
		self._instruction.lvl = self._lvl
		
	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, value):
		self._type = value
		self._instruction.type = self._type

	@property
	def atime(self):
		return self._atime

	@atime.setter
	def atime(self, value):
		self._atime = value
		self._instruction.atime = self._atime
	
	@property
	def atype(self):
		return self._atype

	@atime.setter
	def atype(self, value):
		self._atype = value
		self._instruction.atype = self._atype