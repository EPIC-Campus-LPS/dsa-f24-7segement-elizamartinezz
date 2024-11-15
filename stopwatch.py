# Importing modules and classes
import tm1637
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buttonpin = 4 #define button pin as 4
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                                                                                                                                      
GPIO.setup(12, GPIO.OUT) #light pin
GPIO.setup(12, GPIO.LOW) #turns off the pin


display = tm1637.TM1637(clk=18, dio=17)  # Using 17 and 18 form my display 

display.write([0, 0, 0, 0])  # Defining values used to clear the display
display.brightness(7)
time.sleep(1)


CLK = 18
DIO = 17


			
def start():
	count = 0000
	GPIO.output(12, GPIO.LOW)
	while GPIO.input(buttonpin) == GPIO.HIGH:
		GPIO.output(12, GPIO.HIGH) #this turns on the light 
		count += 1
		display.show(str(count))
		time.sleep(1)
	

GPIO.output(12, GPIO.LOW)
while True:
	if GPIO.input(buttonpin) == GPIO.LOW:
		time.sleep(1)
		display.write([0, 0, 0, 0])
		count = 0000

		#GPIO.output(12, GPIO.LOW)
		while True:
			GPIO.output(12, GPIO.HIGH) #this turns on the light 
			count += 1
			display.show(str(count))
			time.sleep(1)
			if GPIO.input(buttonpin) == GPIO.LOW:
				GPIO.output(12, GPIO.LOW)
				time.sleep(0.5)
				break
				

