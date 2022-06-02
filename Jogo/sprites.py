import pygame as py
from config import *
from math import *
from random import randint




class items(py.sprite.Sprite):
    pocao = {'cura': 50, 'dano': 10}

class talentos(py.sprite.Sprite):
    inimigos_derrotados = 0
    taxadano = 1
    dano = 15*taxadano
    taxadefesa = 15
    defesa = 15 * taxadefesa
    taxamagia = [1, 1.75]
    magia = [(dano*1.5)*taxamagia[1],0.3]
    vidaadicional = 100 * inimigos_derrotados


class inimigos(py.sprite.Sprite):
    inimigos = [{'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0},
    {'vida' : 180,'vidamax':180, 'forca':10, 'defesa': 5, 'agilidade': 0},
    {'vida' : 250,'vidamax':250, 'forca':25, 'defesa': 12, 'agilidade': 5},
    {'vida' : 275,'vidamax':275, 'forca':27, 'defesa': 15, 'agilidade': 5},
    {'vida' : 300,'vidamax': 300, 'forca':30, 'defesa': 17, 'agilidade': 5},
    {'vida' : 500,'vidamax':500, 'forca':50, 'defesa': 25, 'agilidade': 5}]
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

class spritesheet:
    def  __init__ (self, file):
        self.sheet = py.image.load(file).convert()

    def get_sprite (self, game, x, y, width, height):
        sprite = py.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(PRETO)
        return sprite

class personagem (py.sprite.Sprite): 
    habilidades = {'vida' : (100 + talentos.vidaadicional),'vidamax':100, 'forca': talentos.dano, 'defesa': talentos.defesa, 'agilidade': 0}
    magia = {'dano' : talentos.magia[0], 'cura':talentos.magia[1]}

    def __init__ (self, game, x, y):
        self.game = game
        self._camada = PLAYER_LAYER
        self.grupos = self.game.all_sprites
        py.sprite.Sprite.__init__(self, self.grupos)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = self.jogo.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update (self):
        self.movimento()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movimento (self):
        chaves = py.key.get_pressed()
        if chaves[py.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if chaves[py.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if chaves[py.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if chaves[py.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

class block (py.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.arvore_spritesheet.get_sprite(0, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class chao (py.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

    #    self.image = self.game.