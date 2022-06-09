import pygame as py
from config import *
from math import *
from random import randint




class valores(py.sprite.Sprite):
    inimigos_derrotados = 0
    if inimigos_derrotados>0:
        taxadano = 1 * 0.5 *inimigos_derrotados
    else: 
        taxadano = 1
    dano = 15*taxadano


    taxamagia = [1, 1.75]
    magia = [(dano*1.5)*taxamagia[1],0.3]
    vidaadicional = 100 * inimigos_derrotados

    habilidades = {'vida' : 100 ,'vidamax':100 + vidaadicional, 'forca': dano, 'agilidade': 0}

    magia = {'dano' : magia[0], 'cura': magia[1]}
    dano_p = float(habilidades['forca'])
    mdano_p = float(magia['dano'])
    mcura_p = float(magia['cura'])

    Auxilio1 = False
    Auxilio2 = False
    Auxilio3 = False
    Auxilio4 = False
    Auxilio5 = False
    Auxilio6 = False
    irresetavel = False

    vida_i = 0
    vida_p = 0
    TURNO = 'personagem'
    vidamax_i = 0
    interrupt = False
    vivo = True

class auxilio(py.sprite.Sprite):
    if valores.inimigos_derrotados == 0:
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 10
        if valores.irresetavel == False:
            valores.vida_p = 100
            valores.vida_i = 150
            valores.vidamax_i = 150
            valores.TURNO = 'personagem'
            valores.irresetavel = True
    if valores.inimigos_derrotados == 1:
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 10
        if valores.irresetavel == False:
            valores.vida_p = 200
            valores.vida_i = 180
            valores.vidamax_i = 180
            valores.TURNO = 'personagem'
            valores.irresetavel = True
    if valores.inimigos_derrotados == 2:
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 15
        if valores.irresetavel == False:
            valores.vida_p = 300
            valores.vida_i = 220
            valores.vidamax_i = 220
            valores.TURNO = 'personagem'
            valores.irresetavel = True
    if valores.inimigos_derrotados == 4:
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 20
        if valores.irresetavel == False:
            valores.vida_p = 275
            valores.vida_i = 275
            valores.vidamax_i = 400
            valores.TURNO = 'personagem'
            valores.irresetavel = True
    if valores.inimigos_derrotados == 5:
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 35
        if valores.irresetavel == False:
            valores.vida_p = 500
            valores.vida_i = 300
            valores.vidamax_i = 150
            valores.TURNO = 'personagem'
            valores.irresetavel = True
    if valores.inimigos_derrotados > 5 :
        dano_p = int(valores.habilidades['forca'])
        mdano_p = int(valores.magia['dano'])
        mcura_p = int(valores.magia['cura'])
        vidamax_p = int(valores.habilidades['vidamax'])
        dano_i = 50
        if valores.irresetavel == False:
            valores.vida_p = 600
            valores.vida_i = 500
            valores.vidamax_i = 500
            valores.TURNO = 'personagem'
            valores.irresetavel = True
       
            
    def update(self):
        self.game.auxilio()


class combate(py.sprite.Sprite):
    print('yes')
    print('opa')

    def __init__(self,game):#, game, z, vivo, dano_p, mdano_p, mcura_p, dano_i, vidamax_p, vida_p, vida_i, vidamax_i):
        self.game = game

        
        if valores.TURNO == 'personagem' and valores.vivo == True:
            event = py.key.get_pressed()
            #nao reconhece evento
            #não consegue editar variaveis
            if event[py.K_d]:
                chance = randint(0,100)
                if chance<=5:
                    valores.vida_i = valores.vida_i
                else:
                    valores.vida_i -=  auxilio.dano_p
                    valores.TURNO = 'inimigo'
            if event[py.K_w]:
                chance = randint(0,100)
                if chance<=5:
                    valores.vida_i = valores.vida_i
                    valores.TURNO = 'inimigo'
                else:
                    valores.vida_i -= auxilio.mdano_p
                    valores.TURNO = 'inimigo'
            if event[py.K_a]:
                cura = auxilio.vidamax_p * auxilio.mcura_p
                if cura + auxilio.vidamax_p >= auxilio.vidamax_p:
                   valores.vida_p = auxilio.vidamax_p
                   valores.TURNO = 'inimigo'
                else:
                    valores.vida_p += cura
                    valores.TURNO = 'inimigo'
            
            print(valores.vida_i)      
        elif valores.TURNO == 'inimigo':
            print('da')
            chance = randint(0,100)
            if chance <= 5:
                valores.vida_p = valores.vida_p
                valores.TURNO = 'personagem'
            else: 
                valores.vida_p -= auxilio.dano_i
                valores.TURNO = 'personagem'
        if valores.vida_i<=0:
            print('j')
            valores.inimigos_derrotados +=1
            valores.vida_i = valores.vidamax_i
            valores.vida_p = auxilio.vidamax_p
            valores.TURNO = 'personagem'
            valores.vivo =  False
            valores.irresetavel = False
            if valores.inimigos_derrotados == 0:
                valores.Auxilio1 = True 
            if valores.inimigos_derrotados == 1:
                valores.Auxilio2 = True 
            if valores.inimigos_derrotados == 2:
                valores.Auxilio3 = True 
            if valores.inimigos_derrotados == 3:
                valores.Auxilio4 = True 
            if valores.inimigos_derrotados == 4:
                valores.Auxilio5 = True
            if valores.inimigos_derrotados == 5:
                valores.Auxilio6 = True 
             
        print(valores.vida_p)
        if valores.vida_p<=0:
            self.game.playing = False # mandar pra tela de game over dps
        print (valores.TURNO)
    def update(self):
        self.game.combate()
        


class inimigo1(py.sprite.Sprite):
    stats = {'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0}
    def __init__(self, game, x, y):



        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.inimigo1
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
        self.groups = self.game.all_sprites, self.game.inimigo2
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
        self.groups = self.game.all_sprites, self.game.inimigo3
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
        self.groups = self.game.all_sprites, self.game.inimigo4
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
        self.groups = self.game.all_sprites, self.game.inimigo5
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
        self.groups = self.game.all_sprites, self.game.inimigo6
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

    def get_sprite (self, x, y, width, height):
        sprite = py.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(PRETO)
        return sprite



class personagem (py.sprite.Sprite): 


    def __init__ (self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.grupos = self.game.all_sprites
        py.sprite.Sprite.__init__(self, self.grupos)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        imagem = py.image.load('Personagem/fafa pronto 8 bits.png')
        self.image = py.Surface([self.width+20, self.height])
        self.image.set_colorkey(PRETO)
        self.image.blit(imagem, (0,0))
       # self.image = self.game.character_spritesheet.get_sprite(x, y , self.width, self.height+32)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
  

    def movimento (self):
        chaves = py.key.get_pressed()
        if chaves[py.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            #self.facing = 'left'
        if chaves[py.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            #self.facing = 'right'
        if chaves[py.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            #self.facing = 'up'
        if chaves[py.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            #self.facing = 'down'

    def colisao_inimigo1 (self, direcao):
        #hits = py.sprite.spritecollide(self, self.game.inimigo1, False)
        #if hits:
        #    self.game.combate1 = True
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo1, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate1 = True
                if valores.Auxilio1 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)#,TURNO, vivo, dano_p, mdano_p, mcura_p, dano_i[0], vidamax_p, vida_p, vida_i[0], vidamax_i[0])
      
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo1, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate1 = True
                if valores.Auxilio1 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)#,TURNO, vivo, dano_p, mdano_p, mcura_p, dano_i[0], vidamax_p, vida_p, vida_i[0], vidamax_i[0])

    def colisao_inimigo2 (self,direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo2, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate2 = True
                if valores.Auxilio2 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo2, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate2 = True
                if valores.Auxilio2 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
    
    def colisao_inimigo3 (self,direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo3, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate3 = True
                if valores.Auxilio3 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo3, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate3 = True
                if valores.Auxilio3 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
    
    def colisao_inimigo4 (self,direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo4, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate4 = True
                if valores.Auxilio4 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo4, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate4 = True
                if valores.Auxilio4 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)

    def colisao_inimigo5 (self,direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo5, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate5 = True
                if valores.Auxilio5 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo5, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate = True
                if valores.Auxilio5== False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)

    def colisao_inimigo6 (self,direcao):
        if direcao == 'x':
            hits = py.sprite.spritecollide(self, self.game.inimigo6, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                self.game.combate6 = True
                if valores.Auxilio6 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)
                            
        if direcao == 'y':
            hits = py.sprite.spritecollide(self, self.game.inimigo6, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= PLAYER_SPEED
                self.game.combate6 = True
                if valores.Auxilio6 == False:
                    auxilio()
                    valores.vivo = True
                    combate(self.game)

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
                       sprite.rect.y -= PLAYER_SPEED

    def update (self):
        self.movimento()
        self.rect.x += self.x_change
        self.colisao('x')
        self.colisao_inimigo1('x')
        self.colisao_inimigo2('x')
        self.colisao_inimigo3('x')
        self.colisao_inimigo4('x')
        self.colisao_inimigo5('x')
        self.colisao_inimigo6('x')
        self.rect.y += self.y_change
        self.colisao('y')
        self.colisao_inimigo1('y')
        self.colisao_inimigo2('y')
        self.colisao_inimigo3('y')
        self.colisao_inimigo4('y')
        self.colisao_inimigo5('y')
        self.colisao_inimigo6('y')
        
        self.x_change = 0
        self.y_change = 0


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

        #self.image = self.game.arvore(0, 0, self.width, self.height) #Arvore BLOCK

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
        self.image = py.image.load("Terreno/terreno2.png")

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