#!usr/bin/env python

#ok here we started to work with pyglet. this file will be main game file and
#will replaced with game.py.
import pyglet

window = pyglet.window.Window(640*480, caption='APyGM')
creator = pyglet.resource.image('images/pyglet.png')
batch = pyglet.graphics.Batch()

label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
labels = [
            pyglet.text.Label('Name', x=10, y=100, anchor_y='bottom',
                              color=(0, 0, 0, 255), batch),
            pyglet.text.Label('Species', x=10, y=60, anchor_y='bottom',
                              color=(0, 0, 0, 255), batch),
            pyglet.text.Label('Special abilities', x=10, y=20, 
                              anchor_y='bottom', color=(0, 0, 0, 255), 
                              batch)
        ]
self.widgets = [
            TextWidget('', 200, 100, self.width - 210, self.batch),
            TextWidget('', 200, 60, self.width - 210, self.batch),
            TextWidget('', 200, 20, self.width - 210, self.batch)
        ]


@window.event
def on_key_press(symbol, modifiers):
    print 'A key was pressed'

@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()
    creator.blit(100,100)
    
pyglet.app.run()    
