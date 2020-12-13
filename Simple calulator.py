from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *


def getvals(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error - Wait for 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready..')
            screen.update()

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')



def term_of_use():
    tmsg.showinfo('Terms of Use ','IF YOU LIVE IN (OR IF YOUR PRINCIPAL PLACE OF BUSINESS IS IN) THE UNITED STATES, PLEASE READ THE BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER IN SECTION 11. IT AFFECTS HOW DISPUTES ARE RESOLVED.')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','Please Rate us on PlayStore')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')

root=Tk()
canvas_width=750
canvas_height=650
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('CalCulator ')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='calculator.png'))

root.mainloop()
