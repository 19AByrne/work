import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

g = 9.8
start_pos = pygame.Vector2((50, 400))
initial_vel = pygame.Vector2((20, 20))

start_time = 0
time_of_flight = 2 * initial_vel.y / g
simulating = False
pos = start_pos
path = []

def calculate_pos(g: float, time: float, initial_vel: pygame.Vector2, start_pos: pygame.Vector2): 
    x = start_pos.x + initial_vel.x * time
    y = start_pos.y - (initial_vel.y * time - (0.5 * g * (time ** 2)) ) 
    return pygame.Vector2(x, y)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_time = pygame.time.get_ticks() / 1000
            simulating = True

    screen.fill("purple")

    if simulating:
        current_time = pygame.time.get_ticks() / 1000
        if current_time - start_time > time_of_flight:
            simulating = False
        pos = calculate_pos(g, current_time - start_time, initial_vel, start_pos)
        path.append(pos)

    pygame.draw.circle(screen, "red", pos, 5, 1)

    for point in path:
        pygame.draw.circle(screen, "white", point, 1)

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()