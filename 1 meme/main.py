import pygame, sys
from pygame import *
from time import sleep
from gtts import gTTS
from playsound import playsound
import os


def audio(message, voice):
        NOMBRE_ARCHIVO = "text.mp3"

        tts = gTTS(message, lang='es', tld=voice)
        tts.save(NOMBRE_ARCHIVO)

        playsound(NOMBRE_ARCHIVO)
        os.system(f'DEL /F /A {NOMBRE_ARCHIVO}')


pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)



text = ['when vas shaco support', 'que tal un truco de magia','mi equipo', 'oh mi lente de contacto',
        'el otro equipo automaticamente', 'garen soporte', 'lemacia', 'xd dedededede']

images = ['part1.png', 'shaco.png','part2.png', 'part2.png','part3.png','part4.png','garen.png','part5.png']

voice = ['com','fr','com','fr','com','fr','fr','com']

for i,img in enumerate(images):
        window.fill((0,0,0))
        image = pygame.image.load(img)
        window.blit(image, (0,0))
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()
        
        audio(text[i], voice[i])
        sleep(1)

sleep(2)

pygame.quit()
sys.exit()
