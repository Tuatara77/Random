import pygame
import random

CHANGERATE = 3
MINBRIGHTNESS = 0
MAXBRIGHTNESS = 255
assert 0 <= MINBRIGHTNESS <= MAXBRIGHTNESS <= 255

STARTCOLOURS = [
	(random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MINBRIGHTNESS,                                 MAXBRIGHTNESS                ),
	(random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MAXBRIGHTNESS,                                 MINBRIGHTNESS                ),
	(               MINBRIGHTNESS,                  random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MAXBRIGHTNESS                ),
	(               MAXBRIGHTNESS,                  random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS),                 MINBRIGHTNESS                ),
	(               MINBRIGHTNESS,                                  MAXBRIGHTNESS,                 random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS)),
	(               MAXBRIGHTNESS,                                  MINBRIGHTNESS,                 random.randrange(MINBRIGHTNESS,MAXBRIGHTNESS))
    ]

def rainbow(rgb: tuple):
    assert len(rgb) == 3 and rgb[0] == int(rgb[0]) and rgb[1] == int(rgb[1]) and rgb[2] == int(rgb[2]), "Tuple must be 3 integers"
    assert rgb[0] == MAXBRIGHTNESS or rgb[1] == MAXBRIGHTNESS or rgb[2] == MAXBRIGHTNESS and \
           rgb[0] == MINBRIGHTNESS or rgb[1] == MINBRIGHTNESS or rgb[2] == MINBRIGHTNESS, "There must be a value which is 0 and a value which is max-MAXBRIGHTNESS"
    r, g, b = rgb

    if                   r <  MAXBRIGHTNESS and                 g == MINBRIGHTNESS and                 b == MAXBRIGHTNESS: r += CHANGERATE
    elif MINBRIGHTNESS < r <= MAXBRIGHTNESS and                 g == MAXBRIGHTNESS and                 b == MINBRIGHTNESS: r -= CHANGERATE
    elif                 r == MAXBRIGHTNESS and                 g <  MAXBRIGHTNESS and                 b == MINBRIGHTNESS: g += CHANGERATE
    elif                 r == MINBRIGHTNESS and MINBRIGHTNESS < g <= MAXBRIGHTNESS and                 b == MAXBRIGHTNESS: g -= CHANGERATE
    elif                 r == MINBRIGHTNESS and                 g == MAXBRIGHTNESS and                 b <  MAXBRIGHTNESS: b += CHANGERATE
    elif                 r == MAXBRIGHTNESS and                 g == MINBRIGHTNESS and MINBRIGHTNESS < b <= MAXBRIGHTNESS: b -= CHANGERATE

    if r <= MINBRIGHTNESS: r = MINBRIGHTNESS
    if r >= MAXBRIGHTNESS: r = MAXBRIGHTNESS
    if g <= MINBRIGHTNESS: g = MINBRIGHTNESS
    if g >= MAXBRIGHTNESS: g = MAXBRIGHTNESS
    if b <= MINBRIGHTNESS: b = MINBRIGHTNESS
    if b >= MAXBRIGHTNESS: b = MAXBRIGHTNESS

    return (r,g,b)


def main():
    counter = 0
    FULLSCREEN = False
    pygame.init()
    info = pygame.display.Info()
    pygame.mouse.set_visible(False)

    if FULLSCREEN: SCREENWIDTH, SCREENHEIGHT = info.current_w, info.current_h; del info
    else: SCREENWIDTH, SCREENHEIGHT = 500,500; del info
    
    if FULLSCREEN: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT], pygame.FULLSCREEN)
    else: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

    clock = pygame.time.Clock()
    colour = random.choice(STARTCOLOURS)

    done = False
    while not done:
    # while counter < 1001:
        clock.tick_busy_loop(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # done = 1000000
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    # done = 10000000
        
        colour = rainbow(colour)
        screen.fill(colour)
        print(colour)
        # counter += 1
        # print(counter)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
   main()

def a():
    colour = (255,0,0)
    for f in range(1000000):
        colour = rainbow(colour)

# import cProfile
# cProfile.run("main()")
# cProfile.run("a()")
