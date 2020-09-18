#from playsound import playsound

import pygame
import time
import os

def main():
    pygame.init()
    pygame.mixer.music.load('skank.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
main()


'''def main():
    pygame.mixer.init()
    pygame.mixer.music.load('MC_ANÔNIMO_PAGOU_DE_SUPERADA.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(360)



main()
'''
'''def musica():
    playsound('MC_ANÔNIMO_PAGOU_DE_SUPERADA.mp3.mp3')

musica()
'''


