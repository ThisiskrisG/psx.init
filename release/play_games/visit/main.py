
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Visit Game")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((70, 30, 30))
    text = font.render("Visit Game Placeholder", True, (255, 255, 255))
    screen.blit(text, (100, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
