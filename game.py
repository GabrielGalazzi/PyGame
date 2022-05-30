import pygame as py
from sys import *
from math import *
from random import choice



## Config
WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
camada_jogador = 1
VERMELHO = (255, 0 , 0)



##  Sprites
class items(py.sprite.sprite):
    pocao = {'cura': 50, 'dano': 10}

class talentos(py.sprite.sprite):
    taxadano = 1
    dano = 15*taxadano
    taxadefesa = 15
    defesa = 15 * taxadefesa
    taxamagia = [1, 1.75]
    magia = [(dano*1.5)*taxamagia[1],0.3]
    vidaadicional = 75 * "inimigos derrotados"


class inimigos(py.sprite.sprite):
    sergio = {'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0}
    andre = {'vida' : 180,'vidamax':180, 'forca':10, 'defesa': 5, 'agilidade': 0}
    maciel = {'vida' : 250,'vidamax':250, 'forca':25, 'defesa': 12, 'agilidade': 5}
    caue = {'vida' : 275,'vidamax':275, 'forca':27, 'defesa': 15, 'agilidade': 5}
    pelicano = {'vida' : 300,'vidamax': 300, 'forca':30, 'defesa': 17, 'agilidade': 5}
    marcos = {'vida' : 500,'vidamax':500, 'forca':50, 'defesa': 25, 'agilidade': 5}

class personagem(py.sprite.sprite): 
    habilidades = {'vida' : (100 + talentos.vidaadicional),'vidamax':100, 'forca': 0, 'defesa': 0, 'agilidade': 0}
    magia = {'dano' : talentos.magia[0], 'cura':talentos.magia[1]}
#
    def __init__(self, game, x, y):
        self.game = game
        self.camada = camada_jogador
        self.grupos = self.game.all_sprites
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.imagem = py.surface([self.width, self.height])
        self.image.fill(VERMELHO)

class Jogo:
    def _init_(self):
        py.init()
        self.screen = py.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = py.time.Clock()
        self.font = py.font.Font('Arial', 32)
        self.running = True

    def new(self):



py.init()

# ----- Gera tela principal
window = py.display.set_mode((500, 400))
py.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in py.event.get():
        # ----- Verifica consequências
        if event.type == py.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    cor = (255, 0, 0)
    vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]
    py.draw.polygon(window, cor, vertices)

    # ----- Atualiza estado do jogo
    py.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
py.quit()
