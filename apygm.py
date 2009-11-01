#!usr/bin/env python

#ok here we started to work with pyglet. this file will be main game file and
#will replaced with game.py.
from pyglet import window
from pyglet import clock
from pyglet import font


class APyGM(window.Window):
		
		def __init__(self, *argm, **kwargs):
				
				window.Window.__init__(self, *argm, **kwargs)
		
		def mainLoop(self):
				
				ft = font.load('Arial', 28)
				fps_text = font.Text(ft, y=10)
				
				while not self.has_exit:
						self.dispatch_events()
						self.clear
						
						clock.tick()
						
						fps_text = ("fps: %d") % (clock.get_fps())
						fps_text.draw()
						
						self.flip()
if __name__ == "__main__":
		apygm = APyGM()
		apygm.mainLoop()