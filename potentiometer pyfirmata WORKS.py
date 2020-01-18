"""potentiometre pyfirmata"""

import pyfirmata
from tkinter import *

board=pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()
board.analog[0].enable_reporting()

root = Tk()

def arret():
    global running
    root.destroy()
    running = False

bouton = Button(root, text = 'stop', cursor='hand2', command=arret)
bouton.pack()

running = True
while running == True:
    try: texte.destroy()
    except: pass

    analogval = (board.analog[0].read())
    texte = Label(root, text = 'valeur : {}'.format(analogval), fg='black')
    texte.pack()

    root.update()
