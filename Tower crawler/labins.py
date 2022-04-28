from kivy.uix.label import Label

class Entity(object):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._pos = (0, 0)	
		self._size = (100, 100)
		self._text = str(0)
		
		self._instruction = Label( 
		pos=self._pos,
		size=self._size,
		text = self._text)

	@property
	def pos(self):
		return self._pos

	@pos.setter
	def pos(self, value):
		self._pos = value
		self._instruction.pos = self._pos
        
	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		self._size = value
		self._instruction.size = self._size

	@property
	def text(self):
		return self._text

	@text.setter
	def text(self, value):
		self._text = value
		self._instruction.text = self._text		
	