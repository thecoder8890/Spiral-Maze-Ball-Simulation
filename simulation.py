# Ball Collision in Spiral Maze using Pymunk
import pygame
import pymunk
import pymunk.pygame_util
import math
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spiral Maze Simulation")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 200, 255)
BLACK = (0, 0, 0)

# Pymunk Space
space = pymunk.Space()
space.gravity = (0.0, 0.0)

# Draw Options
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Spiral Parameters
CENTER = WIDTH // 2, HEIGHT // 2
SPIRAL_TURNS = 4
SPIRAL_WIDTH = 10
SPIRAL_SPACING = 20

def create_spiral_walls():
    theta = 0
    segments = []
    prev_point = None
    while theta < SPIRAL_TURNS * 2 * math.pi:
        r = SPIRAL_SPACING * theta + 50
        x = CENTER[0] + r * math.cos(theta)
        y = CENTER[1] + r * math.sin(theta)
        if prev_point:
            seg = pymunk.Segment(space.static_body, prev_point, (x, y), SPIRAL_WIDTH // 2)
            seg.elasticity = 0.9
            seg.friction = 0.5
            space.add(seg)
            segments.append(seg)
        prev_point = (x, y)
        theta += 0.1
    return segments

def create_ball(x, y):
    mass = 1
    radius = 10
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = x, y
    body.velocity = random.uniform(-100, 100), random.uniform(-100, 100)
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    shape.friction = 0.5
    space.add(body, shape)
    return shape

# Create spiral and balls
spiral_walls = create_spiral_walls()
balls = [create_ball(CENTER[0], CENTER[1]) for _ in range(5)]

# Main loop
# Encapsulate the main loop in a function to make it reusable and testable
def main_loop():
    running = True
    for _frame in range(200): # Run for a limited number of frames for testing, adjust as needed
        if not running:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        space.step(1/60.0)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main_loop()
