from pathlib import Path
import subprocess
import sys
import pygame

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Psud Game Launcher")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

bg_image = pygame.image.load(str(ASSETS / "menu_bg.png"))
btn_default = pygame.image.load(str(ASSETS / "button_default.png"))
btn_hover = pygame.image.load(str(ASSETS / "button_hover.png"))

class Button:
    def __init__(self, text, y, game):
        self.text = text
        self.rect = pygame.Rect(250, y, 300, 60)
        self.game = game

    def draw(self, mouse_pos):
        image = btn_hover if self.rect.collidepoint(mouse_pos) else btn_default
        screen.blit(image, self.rect.topleft)
        screen.blit(font.render(self.text, True, WHITE), (self.rect.x + 20, self.rect.y + 10))

    def launch(self):
        target = ROOT / "play_games" / self.game / "main.py"
        subprocess.Popen([sys.executable, str(target)], cwd=str(ROOT))

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

buttons = [
    Button("Play Bedroom", 180, "bedroom"),
    Button("Play Visit", 270, "visit"),
    Button("Play Ferris", 360, "ferris"),
]

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(bg_image, (0, 0))
    for button in buttons:
        button.draw(mouse_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.clicked(event.pos):
                    button.launch()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
