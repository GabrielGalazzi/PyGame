import sprites
import config
import pygame as py
from random import randint

class combate(py.sprite.sprite):
    def sergio(x):
        x = 0
        return x
    def __init__(self):
        turno = 'personagem'
        config.PLAYER_SPEED = 0
        pstats = personagem.habilidades
        pmstats = personagem.magia
        istats = inimigo1.stats
        vida_p = pstats['vidamax']
        vida_i = istats['vidamax']
        if turno == 'personagem':
            if event.type == py.KSCAN_Q:
                chance = randint(0,100)
                if chance<=5:
                    vida_i = vida_i
                    config.TURNO = 'inimigo'
                else:
                    vidainimigo -= pstats['forca']
                    config.TURNO = 'inimigo'
            if event.type == py.KSCAN_E:
                chance = randint(0,100)
                if chance<=5:
                    vida_i = vida_i
                    config.TURNO = 'inimigo'
                else:
                    vida_i -= pmstats['dano']
                    config.TURNO = 'inimigo'
            if event.type == py.KSCAN_F:
                cura = pstats['vidamax'] * pmstats['cura']
                config.TURNO = 'inimigo'
            elif config.TURNO == 'inimigo':
                chance = randint(0,100)
                if chance <= 5:
                    vida_p = vida_p
                else: 
                    vida_p -= istats['forca']
        if vida_i<=0:
            config.INIMIGO_MORTO +=1
            config.TURNO = 'personagem'



    while vidainimigo>0 and vidapersonagem>0:
        ataque = str(input(''))   
        if ataque == 'q':
            chance = randint(0,100)
            if chance<=5:
                vidainimigo = vidainimigo
            vidainimigo -= int(personagem.habilidades['forca'])
        if ataque == 'e':
            vidainimigo -= int(personagem.magia['dano'])
        if ataque == 'f':
            if vidapersonagem + personagem.habilidades['vidamax']*talentos.magia['cura']>personagem.habilidades['vidamax']:
                vidapersonagem = personagem.habilidades['vidamax']
            else:
                vidapersonagem += personagem.habilidades['vidamax']*talentos.magia['cura']
        chance2 = randint(0,100)
        if chance2<=5:
            vidapersonagem = vidapersonagem
        else:
            vidapersonagem -= inimigo['forca']
    if vidainimigo<= 0:
        #mostra msg de vitoria
        vidapersonagem = 
    config.PLAYER_SPEED = 8        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    config.PLAYER_SPEED = 0
    # q = ataque com espada; e = dano magia; f = magia cura
    f = 0 
    inimigo = inimigos.inimigos[f]
    vidainimigo = int(inimigo['vida'])
    vidapersonagem = int(personagem.habilidades['vidamax'])
    while vidainimigo>0 and vidapersonagem>0:
        ataque = str(input(''))   
        if ataque == 'q':
            chance = randint(0,100)
            if chance<=5:
                vidainimigo = vidainimigo
            vidainimigo -= int(personagem.habilidades['forca'])
        if ataque == 'e':
            vidainimigo -= int(personagem.magia['dano'])
        if ataque == 'f':
            if vidapersonagem + personagem.habilidades['vidamax']*talentos.magia['cura']>personagem.habilidades['vidamax']:
                vidapersonagem = personagem.habilidades['vidamax']
            else:
                vidapersonagem += personagem.habilidades['vidamax']*talentos.magia['cura']
        chance2 = randint(0,100)
        if chance2<=5:
            vidapersonagem = vidapersonagem
        else:
            vidapersonagem -= inimigo['forca']
    if vidainimigo<= 0:
        #mostra msg de vitoria
        vidapersonagem = 
    config.PLAYER_SPEED = 8