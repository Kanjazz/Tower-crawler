from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

import spawn as sp

class Shop(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	#	sp.spawn_player(self)