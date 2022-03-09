import pygame
import math

TILESIZE = 20
DIMENSIONX, DIMENSIONY = 64,64
SCREENWIDTH, SCREENHEIGHT = TILESIZE*DIMENSIONX, TILESIZE*DIMENSIONY

def raycast(screen, map, player):
    precision = 64
    incrementangle = player.fov/SCREENWIDTH

    wallheights = []
    rayangle = player.angle - player.fov/2
    for f in range(SCREENWIDTH):
        rayx = player.rect.x
        rayy = player.rect.y
        
        raycos = math.cos(math.radians(rayangle))/precision
        raysin = math.sin(math.radians(rayangle))/precision

        wall = 0
        while wall == 0:
            rayx += raycos
            rayy += raysin
            wall = map[math.floor(rayy)]