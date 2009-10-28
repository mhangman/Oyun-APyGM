#!usr/bin/env python

#ok here we started to work with pyglet. this file will be main game file and
#will replaced with game.py
import pyglet

window = pyglet.window.Window(800*600, caption='APyGM')

label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    print 'A key was pressed'

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()    
