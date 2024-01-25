'''
ESC204 2024S
PSA version 10 implementing function
Notes:
works! :)
    * perhaps change red resistor to increase lumination
'''
# Import libraries needed for blinking the LED
import board
import digitalio
import time

# Configure the GPIO pin connected to the LED as a digital output
ledred = digitalio.DigitalInOut(board.GP16)
ledred.direction = digitalio.Direction.OUTPUT

ledgreen = digitalio.DigitalInOut(board.GP17)
ledgreen.direction = digitalio.Direction.OUTPUT

ledblue = digitalio.DigitalInOut(board.GP14)
ledblue.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor


#implementing button modes
mode = 0


# Print a message on the serial console
print('Hello! My LED is controlled by the button.')

#testing
'''
button pressed = false
led on = true

mode 1: blue and red
mode 2:: all lights
'''

# Loop so the code runs continuously
while True:
    if button.value != True and mode == 0:
        mode = 1
        ledred.value = True #light up red light
        ledgreen.value = False #turn off green light
        ledblue.value = True #turn off blue light
        time.sleep(0.3)
    elif button.value != True and mode == 1:
        mode = 2
        ledgreen.value = True #light up green light
        ledred.value = True #turn off red light
        ledblue.value = True #turn off blue light
        time.sleep(0.3)
    elif button.value != True and mode == 2:
        mode = 0
        ledblue.value = False #light up blue light
        ledgreen.value = False #turn off green light
        ledred.value = False #turn off red light
        time.sleep(0.3)
# Write your code here :-)
# Write your code here :-)
