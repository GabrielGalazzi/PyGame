class combate(py.sprite.sprite):
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
    config.PLAYER_SPEED = 3