from pygame import *
from random import choice



class personagem(sprite.sprite): 
    habilidades = {'vida' : 100,'vidamax':100, 'forca': 10, 'defesa': 5, 'agilidade': 5,'danolivro':0, 'curalivro': 0.0}
    magia = {'dano' : 0, 'cura':0}

class items(sprite.sprite):
    espadas = {'basica': 15, 'media': 30, 'forte': 45, 'rara': 100}
    livros = {'basico':{'dano': 40, 'cura': 0.20}, 'avancado':{'dano' : 60, 'cura': 0.40}}
    armaduras = {'basica':{'defesa': 15 , 'vidaad': 50}, 'media': {'defesa': 30, 'vidaad': 100}, 'avancada':{'defesa': 45, 'vidaad': 150}}
    pocao = {'cura': 50, 'dano': 10}

class inimigos(sprite.sprite):
    sergio = {'vida' : 120,'vidamax':120, 'forca':10, 'defesa': 5, 'agilidade': 5}
    andre = {'vida' : 180,'vidamax':180, 'forca':12, 'defesa': 7, 'agilidade': 5}
    maciel = {'vida' : 250,'vidamax':250, 'forca':25, 'defesa': 12, 'agilidade': 5}
    caue = {'vida' : 275,'vidamax':275, 'forca':27, 'defesa': 15, 'agilidade': 5}
    pelicano = {'vida' : 300,'vidamax': 300, 'forca':30, 'defesa': 17, 'agilidade': 5}
    marcos = {'vida' : 500,'vidamax':500, 'forca':50, 'defesa': 25, 'agilidade': 5}

class baus(sprite.sprite):
    bau_sergio = {'mapa' : 'tem mapa', 'livros': items.livros['basico'], 'armadura': items.armaduras['basica']}
    bau_andre = {'pedra' : 'tem pedra', 'espada': items.espadas['basica']}
    bau_maciel = {'remo' : 'tem remo', 'armadura': items.armaduras['basica']}
    bau_caue = {'passaporte' : 'tem passaporte', 'espada': items.espadas['media'], 'livros': items.livros['avancado']}
    bau_pelicano = 'tem chave'