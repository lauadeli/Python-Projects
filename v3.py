'''
ESC204 2024S
PSA version 3 testing green
'''
# Import libraries needed for blinking the LED
import board
import digitalio

'''
# Configure the GPIO pin connected to the LED as a digital output
ledred = digitalio.DigitalInOut(board.GP16)
ledred.direction = digitalio.Direction.OUTPUT
'''

ledgreen = digitalio.DigitalInOut(board.GP17)
ledgreen.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor

'''
#implementing button modes
mode = 0
'''

# Print a message on the serial console
print('Hello! My LED is controlled by the button.')

#testing
'''
button pressed = false
led on = true
'''

# Loop so the code runs continuously
while True:
	#ledred.value = not button.value #light up if button is pressed
    ledgreen.value = not button.value #light up if button is pressed



# Write your code here :-)
