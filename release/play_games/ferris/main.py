import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ferris Wheel")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 34)
angle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((22, 38, 68))
    center = (400, 285)
    pygame.draw.line(screen, (190, 200, 215), (400, 285), (350, 470), 12)
    pygame.draw.line(screen, (190, 200, 215), (400, 285), (450, 470), 12)
    pygame.draw.circle(screen, (235, 215, 130), center, 155, 5)
    for i in range(8):
        a = angle + i * 3.14159 / 4
        x = center[0] + int(155 * pygame.math.Vector2(1, 0).rotate_rad(a).x)
        y = center[1] + int(155 * pygame.math.Vector2(1, 0).rotate_rad(a).y)
        pygame.draw.line(screen, (190, 200, 215), center, (x, y), 3)
        pygame.draw.circle(screen, (80 + i * 12, 160, 220), (x, y), 18)
    screen.blit(font.render("Ferris Wheel Ride - Close the window to exit", True, (255, 255, 255)), (115, 540))
    angle += 0.01
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
