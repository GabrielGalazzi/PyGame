import pygame as py
from config import *
from sprites import *
import sys



class Jogo:
    def _init_(self):
        py.init()
        self.screen = py.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = py.time.Clock()
    #    self.font = py.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = spritesheet('Personagem/fafa _sprite.png')
        self.arvore_spritesheet = spritesheet("Terreno/arvore.png")

    def createTilemap (self):
        for i, row in enumerate(tilemap):
            for k, column in enumerate(row):
                if column == 'B':
                    block(self, k, i)
                if column == 'P':
                    personagem(self, k, i)


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
        pass

    def intro_screen (self): 
        pass

j = Jogo()
j.intro_screen()
j.new()
while j.running:
    j.main()
    j.game_over()

py.quit()
sys.exit()


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
