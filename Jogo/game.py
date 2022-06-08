import pygame as py
from config import *
from sprites import *
import sys


py.init()
class Jogo:
    def _init_(self):
        py.init()
        py.font.init()
        self.screen = py.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = py.time.Clock()
        self.running = True
        self.font = py.font.SysFont('Arial', 32)

        #self.character_spritesheet = spritesheet('Personagem/fafa _sprite.png')
        #self.terreno = py.image.load("./Terreno/terreno.png")
        self.intro_bg = py.image.load('./BGs/introbackground.png')
        self.go_bg = py.image.load('./BGs/gameover.png')

    def createTilemap (self):
        for i, row in enumerate(tilemap):
            for k, column in enumerate(row):
                if column == '.':
                    chao(self, k, i)
                if column == 'B':
                    block(self, k, i)
                if column == 'P':
                    personagem(self, k, i)
                if column == 'S':
                    inimigo1(self, k, i)
                if column == 'A':
                    inimigo2(self, k, i)
                if column == 'M':
                    inimigo3(self, k, i)
                if column == 'C':
                    inimigo4(self, k, i)
                if column == 'P':
                    inimigo5(self, k, i)
                if column == 'L':
                    inimigo6(self, k, i)
                if column == 'b': #Ponte
                    if INIMIGO_MORTO <= 1:
                        py.image.load('./Terreno/ponte_queb_p.png')
                    else:
                        py.image.load('./Terreno/ponte_int_p.png')
                if column == 'c': #Barco
                    py.image.load('./Terreno/boat_p.png')
                if column == 'd': #Alfandega
                    py.image.load('./Terreno/alfandega_p.png')
                if column == 'b': #Porta
                    if INIMIGO_MORTO <= 5: 
                        py.image.load('./Terreno/porta_f_p.png')
                    else:
                        py.image.load('./Terreno/porta_a_p.png')
                
    def new(self):
        # Define um novo jogo
        self.playing = True

        self.all_sprites = py.sprite.LayeredUpdates()
        self.blocks = py.sprite.LayeredUpdates()
        self.inimigos = py.sprite.LayeredUpdates()
        self.ataques = py.sprite.LayeredUpdates()

        self.createTilemap()


    def eventos (self):
        # Evento do jogo em loop
        for evento in py.eventos.get():
            if evento.type == py.QUIT:
                self.playing = False
                self.running = False

    def update (self):
        # Updates do jogo em loop
        self.all_sprites.update()

    def draw (self):
        # Desenho do game em loop
        self.screen.fill(PRETO)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        py.display.update()

    def main (self):
        # Loop do jogo
        while self.playing:
            self.eventos()
            self.update()
            self.draw()
        self.running = False


    def game_over (self):
        text = self.font.render('Game Over', True, BRANCO)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = botao(10, WIN_HEIGHT-60, 120, 50, BRANCO, PRETO, 'Jogar de novo', 32)

        for sprite in self.all_sprites:
            sprite.kill()
        
        while self.running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

        mouse_pos = py.mouse.get_pos()
        mouse_press = py.mouse.get_pressed()

        if restart_button.is_pressed(mouse_pos, mouse_press):
            self.new()
            self.main()

        self.screen.blit(self.go_bg, (0,0))
        self.screen.blit(text, text_rect)
        self.screen.blit(restart_button.image, restart_button.rect)
        py.display.update()

    def intro_screen (self): 
        intro = True
        py.font.init()
        self.font = py.font.SysFont('Arial', 32) ## 14

        title = self.font.render('Jogo Projeto PYGAME', True, PRETO) #09
        title_rect = title.get_rect(x=10, y=10) 

        play_button = botao(10, 50, 100, 50, BRANCO, PRETO, 'Play', 32)

        while intro:
            for event in py.event.get():
                if event.type == py.QUIT:
                    intro = False
                    self.running = False

        mouse_pos = py.mouse.get_pos()
        mouse_press = py.mouse.get_pressed

        if play_button.is_pressed(mouse_pos, mouse_press):
            intro = False

        self.screen.blit(self.intro_bg, (0,0))
        self.screen.blit(title, title_rect)
        self.screen.blit(play_button.image, play_button.rect)
        self.clock.tick(FPS)
        py.display.update()

j = Jogo()
j.intro_screen()
j.new()
while j.running:
    j.main()
    j.game_over()

py.quit()
sys.exit()