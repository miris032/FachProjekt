import pygame





if __name__ == '__main__':
    pygame.init()

    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Moving rectangle")
    x = 200
    y = 200

    # dimensions of the object
    width = 20
    height = 20
    # velocity / speed of movement
    vel = 10

    # Indicates pygame is running
    run = True

    # infinite loop
    while run:
        # creates time delay of 10ms
        pygame.time.delay(10)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        # stores keys pressed
        keys = pygame.key.get_pressed()

        # if left arrow key is pressed
        if keys[pygame.K_LEFT] and x > 0:
            # decrement in x co-ordinate
            x -= vel

        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and x < 500 - width:
            # increment in x co-ordinate
            x += vel

        # if left arrow key is pressed
        if keys[pygame.K_UP] and y > 0:
            # decrement in y co-ordinate
            y -= vel

        # if left arrow key is pressed
        if keys[pygame.K_DOWN] and y < 500 - height:
            # increment in y co-ordinate
            y += vel

        # completely fill the surface object
        # fill the background colour
        win.fill((219, 208, 167))

        # drawing object on screen which is rectangle here
        pygame.draw.rect(win, (18, 53, 85), (x, y, width, height))

        # it refreshes the window
        pygame.display.update()

    # closes the pygame window
    pygame.quit()
