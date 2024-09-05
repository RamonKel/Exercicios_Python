import pygame
pygame.init() #Inicia a biblioteca
pygame.mixer.music.load('Music/giornos-theme-but-only-the-best-part-is-in_vwd15lya_lyb0-online-audio-converter.mp3') #Carrega a musica
pygame.mixer.music.play() #
pygame.event.wait()
input()
pygame.event.wait()

#Realiza a reprodução de um audio em MP3 utilizando a biblioteca PyGame