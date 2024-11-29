import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()

# Screen setup
size = (1250, 700)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Centered Text Example')
clock = pygame.time.Clock()

# Load background
bg = pygame.image.load('Assets/bg.png')

# Font setup
font = pygame.font.Font('Assets/Font/Disket-Mono-Bold.ttf', 36)

# Text surface
text_surface = font.render('Hello, World!', True, (255, 255, 255))  # White text
text_rect = text_surface.get_rect()
text_rect.center = (size[0] // 2, size[1] // 2)  # Center the text

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Clear screen and draw background
    window.blit(bg, (0, 0))

    # Draw the text
    window.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
