###########################################
# Titre: Derby                            #
# Auteur: Guy Paquin                      #
# Courriel: gpaquin@educnda.com           #
# Date: 25 juillet 2018                   #
# Note:                                   #
###########################################

#importation des modules utiles

import pygame
import sys
from pygame.locals import *
from random import *
import time

###### CLASSES, FONCTIONS ET VARIABLES ######

#Variable
premier_tours=True
position =[0,0,0,0,0]

# CLASSE
class LICORNE:

    def __init__(self,position_x,position_y,fond,ligne,corne1,corne2,peau,criniere,meche,pupille):
        self.y = position_y-1
        self.x = position_x-1
        self.couleur_de_fond = fond
        self.couleur_de_ligne = ligne
        self.couleur_de_corne1 = corne1
        self.couleur_de_corne2 = corne2
        self.couleur_de_peau = peau
        self.couleur_de_criniere = criniere
        self.couleur_de_meche = meche
        self.couleur_de_pupille = pupille
        self.licorne=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,3,3,1,7,7,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,1,0,0,1,4,4,1,3,3,1,2,2,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,1,1,1,1,1,3,3,1,7,7,7,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,1,3,3,3,3,3,1,2,2,2,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,4,4,1,1,1,1,1,1,1,7,7,7,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,4,4,1,1,4,4,4,4,4,4,4,1,2,2,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,1,1,1,4,4,4,4,4,4,4,4,4,4,1,1,1,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,1,4,4,4,4,4,4,4,1,1,1,1,4,4,4,4,4,4,4,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,3,3,3,1,4,4,4,4,4,4,1,1,5,1,1,1,4,4,4,4,4,4,4,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,6,1,3,3,1,4,4,4,4,4,4,1,1,1,1,1,1,4,4,4,4,4,4,4,4,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,6,1,3,3,3,1,4,4,4,4,4,4,1,1,1,1,1,1,4,4,4,4,4,4,4,4,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,1,6,1,3,3,1,1,4,4,4,4,4,4,4,1,1,1,1,4,4,4,4,4,4,4,4,4,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,1,1,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,1,6,6,6,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,1,0,0,0,0,0,1,1,4,4,4,4,4,4,1,3,3,3,3,3,3,3,3,1,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,3,1,0,0,1,1,4,4,4,4,4,4,4,4,4,1,3,3,3,3,3,1,1,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,3,3,3,1,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,1,3,3,3,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,1,3,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,1,6,6,6,1,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,6,6,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,1,6,6,6,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,1,6,6,6,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,6,6,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,6,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,1,3,3,3,1,6,6,6,1,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,1,3,3,3,1,6,6,6,1,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,3,1,1,1,3,3,3,1,6,6,6,6,1,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,1,3,3,3,3,3,3,1,6,6,6,1,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,6,1,3,3,3,3,1,6,6,6,6,1,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,6,6,1,1,1,1,6,6,6,6,1,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,6,6,6,6,6,6,6,6,6,1,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,6,6,6,6,6,6,6,1,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,6,6,6,6,6,1,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,1,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,1,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,1,1,0,1,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,1,0,1,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,1,0,0,1,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,1,0,0,0,1,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    def afficher(self):
        xcoord= self.x
        ycoord=self.y
        for y in range(0,50):
            ycoord=ycoord+1
            xcoord= self.x

            for x in range(0,70):
                xcoord=xcoord+1
                if self.licorne[y][x] == 0:
                    pygame.draw.rect(surface,self.couleur_de_fond,(xcoord,ycoord,1,1))
                elif self.licorne[y][x] == 1:
                    pygame.draw.rect(surface,self.couleur_de_ligne,(xcoord,ycoord,1,1))
                elif self.licorne[y][x] == 2:
                    pygame.draw.rect(surface,self.couleur_de_corne1,(xcoord,ycoord,1,1))
                elif self.licorne[y][x] == 3:
                    pygame.draw.rect(surface,self.couleur_de_criniere,(xcoord,ycoord,1,1))
                elif self.licorne[y][x] == 4:
                    pygame.draw.rect(surface,self.couleur_de_peau,((xcoord),ycoord,1,1))
                elif self.licorne[y][x] == 5:
                    pygame.draw.rect(surface,self.couleur_de_pupille,((xcoord),ycoord,1,1))
                elif self.licorne[y][x] == 6:
                    pygame.draw.rect(surface,self.couleur_de_meche,((xcoord),ycoord,1,1))
                elif self.licorne[y][x] == 7:
                    pygame.draw.rect(surface,self.couleur_de_corne2,((xcoord),ycoord,1,1))
        pygame.display.update()
                
    def mouvement_horizontal(self,delta):
        print("avance",self.x,self.y)
        pygame.draw.rect(surface,self.couleur_de_fond,(self.x,self.y,75,55))
        pygame.display.update()
        self.x=self.x+delta
        self.afficher()
        return self.x

    def mouvement_vertical(self,delta):
        print("monter",self.x,self.y)
        pygame.draw.rect(surface,self.couleur_de_fond,(self.x,self.y,75,55))
        pygame.display.update()
        self.y=self.y+delta
        if self.y < 0 or self.y >569:
            self.y = self.y-delta
        self.afficher()

    def mouvement_aleatoire(self):
        a=randrange(0,4)
        if a == 0:
            self.mouvement_horizontal(20)
        elif a == 1:
            self.mouvement_horizontal(-20)
        elif a == 2:
            self.mouvement_vertical(-20)
        elif a == 3:
            self.mouvement_vertical(20)
        elif a == 4:
            pygame.draw.rect(surface,self.couleur_de_fond,(self.x,self.y,75,55))
            pygame.display.update()
            self.afficher()
        
# FONCTIONS
def delta():
    global premier_tours
    if premier_tours == True:
        delta=randrange(100,200)
        return delta
    else:
        delta=randrange(0,100)
        return delta
        
            
    
# définition des couleurs (https://www.toutes-les-couleurs.com/code-couleur-rvb.php)

NOIR = (0,0,0)
BLEU = (0,0,255)
PERSAN=(102,0,255)
INDIGO=(121,28,248)
LAVANDE=(150,131,236)
VIOLET=(102,0,153)
ROUGE = (255,0,0)
ROSE = (253,108,158)
CARDINAL = (184,32,16)
CARMIN = (150,0,24)
MARS = (247,35,12)
BISQUE = (255,228,196)
CERISE = (222,49,99)
OEUF = (253,233,224)
NYMPHE = (254,231,240)
FRAMBOISE = (199,44,72)
FUSHIA = (253,63,146)
MAGENTA = (255,0,255)
PECHE = (253,191,183)
JAUNE = (255,255,0)
AMBRE = (240,195,0)
OR = (255,215,0)
TOPAZE = (250,234,115)
VERT = (0,255,0)
BLANC = (255,255,255)
GRIS = (128,128,128)
ARGILE =(239,239,239)
ETAIN = (237,237,237)
PERLE = (206,206,206)
MAUVE = (75, 0, 130)
BRUN = (136, 66, 29)
GAZON = (58, 137, 35)

# définition des sons

#sonbleu = pygame.mixer.Sound("Simeonbleu.wav")


###### CONFIGURATION DE LA FENÊTRE DE JEU ######

# initialisation du module pygame
pygame.init()

#initialisation de la fenêtre de jeux
surface = pygame.display.set_mode((1200,600),0,32) # création de la surface de jeux
pygame.display.set_caption("Derby - Licorne d'amour") # Entête de la fenêtre pygame
surface.fill(GAZON) # Couleur de fond de l'écran

def lignes():
    global GAZON
    surface.fill(GAZON)
    # Ligne de départ
    pygame.draw.line(surface,BLANC,(100,10),(100,560),10)



    # Ligne d'arrivée
    lignedarrivee=[[1,2],[2,1]]
    for boucle in range(0,560,20):
        posy=boucle
        for y in range(0,2):
            posy=posy+10
            posx=1100
            for x in range(0,2):
                posx=posx+10
                if lignedarrivee[y][x] == 1:
                    pygame.draw.rect(surface,NOIR,(posx,posy,10,10))
                elif lignedarrivee[y][x] == 2:
                    pygame.draw.rect(surface,BLANC,(posx,posy,10,10))
            
            
    pygame.display.update()

#définition des licornes (def __init__(self,position_x,position_y,fond,ligne,corne1,corne2,peau,criniere,meche,pupille):)

Julie = LICORNE(10,50,GAZON,NOIR,MAUVE,BLEU,BLANC,JAUNE,ROUGE,BLANC)
Martine = LICORNE(10,150,GAZON,NOIR,JAUNE,ROUGE,PERLE,MAUVE,BLEU,BLANC)
Lucille = LICORNE(10,250,GAZON,NOIR,VIOLET,OR,AMBRE,FRAMBOISE,OEUF,BLANC)
Lana = LICORNE(10,350,GAZON,NOIR,ROSE,INDIGO,ETAIN,CARDINAL,CARMIN,BLANC)
Lucinda = LICORNE(10,450,GAZON,NOIR,FRAMBOISE,NYMPHE,PERSAN,TOPAZE,BLANC,BLANC)


###### DÉFINITION DES ÉCRANS #####

# Introduction

def intro():
    surface.fill(GAZON)
    surface.blit(pygame.image.load("licorneintro.png"),(600,300))
    pygame.display.update()
    boucle = True
    while boucle == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                boucle = False
            




###### BOUCLE PRINCIPALE ######
intro()


lignes()
Julie.afficher()
Martine.afficher()
Lucille.afficher()
Lana.afficher()
Lucinda.afficher()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            boucle = True
            while boucle ==True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    else:
                        position[0]=Julie.mouvement_horizontal(delta())
                        position[1]=Martine.mouvement_horizontal(delta())
                        position[2]=Lucille.mouvement_horizontal(delta())
                        position[3]=Lana.mouvement_horizontal(delta())
                        position[4]=Lucinda.mouvement_horizontal(delta())
                        premier_tours=False
                        time.sleep(0.5)
        

    pygame.display.update()
                                  
        
                                

