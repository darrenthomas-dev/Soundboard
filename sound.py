import pygame
import random
import RPi.GPIO as GPIO
from os import listdir

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

path = 'python/soundboard/clips/'
 
while True:
	input_state = GPIO.input(18)
	if input_state == False:

		files = listdir(path)

		soundclip = random.choice(files)
		print(soundclip)

		pygame.mixer.init()
		sound = pygame.mixer.Sound(path + soundclip)
		sound.play()
		while pygame.mixer.get_busy() == True:
    	continue
