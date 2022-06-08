import pygame as py
from config import *
from math import *
from random import randint

from sqlalchemy import false


class combate(py.sprite.Sprite):
    if combate1 == True:
        if import1 == False:
            pstats = personagem.habilidades
            pmstats = personagem.magia
            istats = inimigo1.stats
            vida_p = pstats['vidamax']
            vida_i = istats['vidamax']
            import1 == True
        def __init__(self):
            PLAYER_SPEED = 0
            if TURNO == 'personagem':
                if py.event.type == py.KSCAN_Q:
                    chance = randint(0,100)
                    if chance<=5:
                        vida_i = vida_i
                        TURNO = 'inimigo'
                    else:
                        vidasinimigo -= pstats['forca']
                        TURNO = 'inimigo'
                if py.event.type == py.KSCAN_E:
                    chance = randint(0,100)
                    if chance<=5:
                        vida_i = vida_i
                        TURNO = 'inimigo'
                    else:
                        vida_i -= pmstats['dano']
                        TURNO = 'inimigo'
                if py.event.type == py.KSCAN_F:
                    cura = pstats['vidamax'] * pmstats['cura']
                    TURNO = 'inimigo'
            elif TURNO == 'inimigo':
                chance = randint(0,100)
                if chance <= 5:
                    vida_p = vida_p
                else: 
                    vida_p -= istats['forca']
            elif vida_i<=0:
                INIMIGO_MORTO +=1
                TURNO = 'personagem'
            elif vida_p<=0:
                self.game.playing = False # mandar pra tela de game over dps

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


class inimigo1(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0}

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/sergio.png')
    
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        
class inimigo2(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 180,'vidamax':180, 'forca':10, 'defesa': 5, 'agilidade': 0}
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/andre.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class inimigo3(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0}
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/maciel.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class inimigo4(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 275,'vidamax':275, 'forca':27, 'defesa': 15, 'agilidade': 5}
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/caue.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class inimigo5(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 300,'vidamax': 300, 'forca':30, 'defesa': 17, 'agilidade': 5}
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.inimigos
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/pelicano.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class inimigo6(py.sprite.Sprite):
    def __init__(self, game, x, y):

        stats = {'vida' : 500,'vidamax':500, 'forca':50, 'defesa': 25, 'agilidade': 5}
    # ordem lista = sergio; andre; maciel; caue; pelicano; marcos

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        py.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = py.image.load('./Inimigos/marcos.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


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
        
        self.image = py.image.load('Personagem/fafa pronto 8 bits2.png')

        #self.image = self.game.character_spritesheet.get_sprite(game , 0, 0 , self.width, self.height+90)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update (self):
        self.movimento()
        self.colisao_inimigo()
        self.combate
        self.rect.x += self.x_change
        self.colisao('x')
        self.rect.y += self.y_change
        self.colisao('y')
        
        self.x_change = 0
        self.y_change = 0

    def movimento (self):
        chaves = py.key.get_pressed()
        if chaves[py.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if chaves[py.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if chaves[py.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if chaves[py.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def colisao_inimigo1 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo1, False)
        if hits:
            combate1 = True
    
    def colisao_inimigo2 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo2, False)
        if hits:
            pass
    
    def colisao_inimigo3 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo3, False)
        if hits:
            pass
    
    def colisao_inimigo4 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo4, False)
        if hits:
            pass

    def colisao_inimigo5 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo5, False)
        if hits:
            pass

    def colisao_inimigo6 (self):
        hits = py.sprite.spritecollide(self, self.game.inimigo6, False)
        if hits:
            pass

    def colisao (self, direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED


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
        
        #self.arvore = py.image.load('Jogo/arvore_pronta.png')
        self.image = py.image.load('Terreno/arvore_pronta.png')
        
        #self.image = self.game.arvore.load.image(64,64 ,self.width, self.height) #Arvore BLOCK

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

        #self.image = self.game.terreno.load.image(64, 64, self.width, self.ght) #GRAMA CHAO
        self.image = py.image.load("Terreno/terreno.png")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class botao:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        py.font.init()
        self.font = py.font.SysFont('Arial', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = py.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
