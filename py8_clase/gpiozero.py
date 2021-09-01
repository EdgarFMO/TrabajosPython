from gpiozero import Button
from signal import pause
button = Button(2) #hold_time 
button2 = Button(3)

def imprimebtn(a):
  print('se oprimió el botón', a)
try:
  button.when_pressed = lambda:  imprimebtn(1) # _represed (dejó de presionar)
  button2.when_pressed = lambda: imprimebtn(2) #hold (mientras se presiona el botón)
  pause()
 
finally:
  pass



#if button.is_pressed:
#  print('oprimió el botón')
#eslse:
#   print('no oprimió el botón')

  