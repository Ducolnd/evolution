import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
done = False
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (100, 100, 50,50))

    clock.tick(60)
    pygame.display.flip()
pygame.quit()