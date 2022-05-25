from pygame import *
class personagem(sprite.sprite): 
    habilidades = {'vida' : 100,'vidamax':100, 'forca': 0, 'defesa': 0, 'agilidade': 0}
    magia = {'dano' : 0, 'cura':0}

class items(sprite.sprite):
    espadas = {'basica': 15, 'media': 30, 'forte': 45}
    varinhas = {'basica':{'dano': 40, 'cura': 0.20}, 'avancada':{'dano' : 60, 'cura': 0.40}}
    armaduras = {'basica':{'defesa': 15 , 'vidaad': 50}, 'media': {'defesa': 30, 'vidaad': 100}, 'avancada':{'defesa': 45, 'vidaad': 150}}
    pocao = {'cura': 50, 'dano': 10}
class inimigos(sprite.sprite):
    sergio = {'vida' : 150,'vidamax':150, 'forca':10, 'defesa': 5, 'agilidade': 0}
    andre = {'vida' : 180,'vidamax':180, 'forca':10, 'defesa': 5, 'agilidade': 0}
