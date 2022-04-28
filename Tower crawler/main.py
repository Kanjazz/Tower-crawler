#подгрузка стандартных модулей
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import animations as anim
import menu
import game
import credits
import dev
#import mini
import shop

#СБОРКА  
#‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
class App(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(dev.Dev(name='dev'))
		sm.add_widget(menu.Menu(name='menu'))
		sm.add_widget(game.Game(name='game'))	
		sm.add_widget(credits.Credits(name='credits'))	
		#sm.add_widget(mini.Mini(name='mini'))	
		sm.add_widget(shop.Shop(name='shop'))	
		
		return sm

#‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡	

			
if __name__ == '__main__':
    App().run()
    