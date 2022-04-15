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

def rainbow(rgb: tuple, minbrightness: int=0, maxbrightness: int=255, changerate: int=3):
    assert len(rgb) == 3 and rgb[0] == int(rgb[0]) and rgb[1] == int(rgb[1]) and rgb[2] == int(rgb[2]), "Tuple must be 3 integers"
    assert rgb[0] == maxbrightness or rgb[1] == maxbrightness or rgb[2] == maxbrightness and \
           rgb[0] == minbrightness or rgb[1] == minbrightness or rgb[2] == minbrightness, "There must be values which are equal to the min and max brightness"
    r, g, b = rgb

    if                   r <  maxbrightness and                 g == minbrightness and                 b == maxbrightness: r += changerate
    elif minbrightness < r <= maxbrightness and                 g == maxbrightness and                 b == minbrightness: r -= changerate
    elif                 r == maxbrightness and                 g <  maxbrightness and                 b == minbrightness: g += changerate
    elif                 r == minbrightness and minbrightness < g <= maxbrightness and                 b == maxbrightness: g -= changerate
    elif                 r == minbrightness and                 g == maxbrightness and                 b <  maxbrightness: b += changerate
    elif                 r == maxbrightness and                 g == minbrightness and minbrightness < b <= maxbrightness: b -= changerate

    if r <= minbrightness: r = minbrightness
    if r >= maxbrightness: r = maxbrightness
    if g <= minbrightness: g = minbrightness
    if g >= maxbrightness: g = maxbrightness
    if b <= minbrightness: b = minbrightness
    if b >= maxbrightness: b = maxbrightness

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
        
        colour = rainbow(colour, MINBRIGHTNESS, MAXBRIGHTNESS, CHANGERATE)
        screen.fill(colour)
        # print(colour)
        # counter += 1
        # print(counter)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
   main()

def a():
    colour = (255,0,0)
    for f in range(1000000):
        colour = rainbow(colour, MINBRIGHTNESS, MAXBRIGHTNESS, CHANGERATE)

# import cProfile
# cProfile.run("main()")
# cProfile.run("a()")
