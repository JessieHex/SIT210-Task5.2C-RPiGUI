from tkinter import *
import tkinter.font
from gpiozero import LED # calls cleanup automatically
import RPi.GPIO # clean up

RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led_r = LED(14)
led_y = LED(15)
led_g = LED(18)
leds = [led_r, led_y, led_g]

## GUI DEFINITIONS ##
gui = Tk()
gui.title("LED GUI")

### Event Functions ###
def sel():
   selected = var.get()
   for i, led in enumerate(leds):
       if i != selected and led.is_lit:
           led.off()
       if i == selected and not led.is_lit:
            led.on()

## WIDGETS ##
var = IntVar() # select a radio button will store an int value to var
r1 = Radiobutton(gui, text="RED", bg="red", variable=var, value=0, command=sel,
                height=1, width=24)
r1.pack( anchor = W )

r2 = Radiobutton(gui, text="YELLOW", bg="yellow", variable=var, value=1,
                 command=sel, height=1, width=24)
r2.pack( anchor = W )

r3 = Radiobutton(gui, text="GREEN", bg="green", variable=var, value=2, command=sel,
                 height=1, width=24)
r3.pack( anchor = W)

exitButton = Button(gui, text='EXIT', command=lambda: gui.destroy(),
                    bg='gray', height=1, width=24)
exitButton.pack(anchor = SE)


gui.mainloop() # Loops forever

