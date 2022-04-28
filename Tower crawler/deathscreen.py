from kivy.graphics import Rectangle
from kivy.uix.label import Label

def screen(self):
			with self.canvas.after:				
				self._movelesslabels.append(Rectangle(pos=(250,500), size = (500,600)))
						
				self._movelesslabels.append(Label(pos=(450,600),text='Restart',color=(0,0,0,1)))
							
				self._movelesslabels.append(Label(pos=(450,700),text='Height reached: ' +str(round(self.count)),color=(0,0,0,1)))
							
				self._movelesslabels.append(Label(pos=(450,800),text = 'Money collected: ' +str(self.money_count),color=(0,0,0,1)))