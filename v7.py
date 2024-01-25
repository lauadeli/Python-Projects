# Write your code here :-)
'''
ESC204 2024S
PSA version 7 testing mode usage
Notes:
does not work -> one press lights all lights at once and does not turn back off
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
    if button.value != True:
        if mode == 0:
            mode = 1
            ledred.value = True #light up red light
            #time.sleep(0.3)
        elif mode == 1:
            mode = 2
            ledgreen.value = True #light up green light
            #time.sleep(0.3)
        elif mode == 2:
            mode = 0
            ledblue.value = True #light up blue light
            #time.sleep(0.3)

