# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
#
# модуль turtle для рисования
# Tkinter
# PyQt5
import turtle
from time import sleep
from random import randint
from itertools import cycle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def draw_light(self, color):
        s = turtle.getscreen()
        t = turtle.Turtle()
        t.pen(pencolor=color, fillcolor=color, pensize=1, speed=0)
        t.begin_fill()
        t.circle(90)
        t.end_fill()

    def change_light(self):
        count = 0
        while count < 100:
            for light in cycle(self.__color):
                if light == 'red':
                    self.draw_light(light)
                    sleep(7)
                elif light == 'yellow':
                    self.draw_light(light)
                    sleep(2)
                elif light == 'green':
                    self.draw_light(light)
                    sleep(randint(1, 3))
        count += 1


tl = TrafficLight()
tl.change_light()
