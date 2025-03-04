from gtts import gTTS
import pygame
import os

myText = "Welcome to geeksforgeeks!"
language = "en"

myObj = gTTS(text=myText , lang=language , slow=False)

myObj.save("welcome_to_py.mp3")

pygame.mixer.init()
pygame.mixer.music.load("welcome_to_py.mp3")
# pygame.mixer.music.play()

os.system("start welcome_to_py.mp3")