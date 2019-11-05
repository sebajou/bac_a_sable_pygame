#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640,480), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)


#Rafraîchissement de l'écran
pygame.display.flip()

#Prend en compte le maintient appuyer de la touche
pygame.key.set_repeat(400, 30)

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,30)
			if event.key == K_UP:	#Si "flèche haut"
				#On monte le perso
				position_perso = position_perso.move(0,-30)
			if event.key == K_RIGHT:	#Si "flèche droite"
				#On va vers la droite le perso
				position_perso = position_perso.move(30,0)
			if event.key == K_LEFT:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(-30,0)

#        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1]100:
#            print("En voyage !")

	
	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()

