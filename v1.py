# Write your code here :-)
'''
ESC204 2024S
PSA Version 1 (differentiating leds)
'''
# Import libraries needed for blinking the LED
import board
import digitalio

# Configure the GPIO pin connected to the LED as a digital output
ledred = digitalio.DigitalInOut(board.GP16)
ledred.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor

# Print a message on the serial console
print('Hello! My LED is controlled by the button.')
#testing
print('why')
print(button.value)
print(ledred.value)


# Loop so the code runs continuously
while True:
	ledred.value = not button.value #light up if button is pressed


