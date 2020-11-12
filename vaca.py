from playsound import playsound
import pyglet
import threading


def gifs():
    ag_file = "vaca.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    pyglet.app.run()


def sound():
    while True:
        playsound('vaca.mp3')


gifs = threading.Thread(target=gifs, name='gifs')
sound = threading.Thread(target=sound, name='sound')

gifs.start()
sound.start()
