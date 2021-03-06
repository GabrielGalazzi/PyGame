import pygame as py
from config import *
from sprites import *
import sys



class Jogo:
    def __init__(self):
        py.init()
        py.font.init()
        self.screen = py.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = py.time.Clock()
        self.running = True
        self.font = py.font.SysFont('Arial', 32)
        self.intro_bg = py.image.load('./BGs/introbackground.png')
        self.go_bg = py.image.load('./BGs/gameover.png')
        self.musicp = py.mixer.music.load('./Musica/8-Bit-Mayhem.wav')
        self.musicp_v = py.mixer.music.set_volume(0.4)

    def createTilemap (self):
        for i, row in enumerate(tilemap):
            for k, column in enumerate(row):
                if column == '.':
                    chao(self, k, i)
                if column == 'B':
                    block(self, k, i)
                if column == 'F':
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

          
    def new(self):
        # Define um novo jogo
        self.playing = True
        self.combate1 = False
        self.combate2 = False
        self.combate3 = False
        self.combate4 = False
        self.combate5 = False
        self.combate6 = False

        if self.combate1 == True:
            numero = inimigo1
        if self.combate2 == True:
            numero = inimigo2
        if self.combate3 == True:
            numero = inimigo3
        if self.combate4 == True:
            numero = inimigo4
        if self.combate5 == True:
            numero = inimigo5
        if self.combate6 == True:
            numero = inimigo6

        self.all_sprites = py.sprite.LayeredUpdates()
        self.blocks = py.sprite.LayeredUpdates()
        self.inimigo1 = py.sprite.LayeredUpdates()
        self.inimigo2 = py.sprite.LayeredUpdates()
        self.inimigo3 = py.sprite.LayeredUpdates()
        self.inimigo4 = py.sprite.LayeredUpdates()
        self.inimigo5 = py.sprite.LayeredUpdates()
        self.inimigo6 = py.sprite.LayeredUpdates()
        self.music_play = py.mixer.music.play()

        self.createTilemap()

    def event (self):
        # Evento do jogo em loop
        for evento in py.event.get():
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
            self.event()
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

        title = self.font.render('As Fantasticas Aventuras de Fabricio', True, PRETO)
        title_rect = title.get_rect(x=10, y=10) 

        play_button = botao(10, 50, 100, 50, BRANCO, PRETO, 'Play', 32)

        while intro:
            for event in py.event.get():
                if event.type == py.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = py.mouse.get_pos()
            mouse_press = py.mouse.get_pressed()

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