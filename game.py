import pygame

fps = 60

# run the game
def play():
    # setup game
    pygame.init()
    screen = pygame.display.set_mode((720, 480))
    clock = pygame.time.Clock()
    running = True

    # game loop
    while running:
        # poll events
        for event in pygame.event.get():
            # if quit requested
            if event.type == pygame.QUIT:
                running = False
        
        # clear frame buffer
        screen.fill((0, 0, 255))

        # update screen
        pygame.display.flip()

        # ensure framerate does not excede maximum
        clock.tick(60)

    return
