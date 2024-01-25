'''
ESC204 2024S
PSA version 8 testing modes part2
Notes:
modes work now but needs wait time as pressing down button too long
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
'''

# Loop so the code runs continuously
while True:
    if button.value != True and mode == 0:
        mode = 1
        ledred.value = True #light up red light
        ledgreen.value = False #turn off green light
        ledblue.value = False #turn off blue light
        #time.sleep(0.3)
    elif button.value != True and mode == 1:
        mode = 2
        ledgreen.value = True #light up green light
        ledred.value = False #turn off red light
        ledblue.value = False #turn off blue light
        #time.sleep(0.3)
    elif button.value != True and mode == 2:
        mode = 0
        ledblue.value = True #light up blue light
        ledgreen.value = False #turn off green light
        ledred.value = False #turn off red light
        #time.sleep(0.3)
# Write your code here :-)
