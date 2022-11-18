import math, random
import pygame
import TC_v0
import os

# Images path
script_dir = os.path.dirname(__file__)
steve_path = script_dir + "/imgs/" + "steve.jpg"
robot_path = script_dir + "/imgs/" + "robot.jpg"

# Initialization
pygame.init()
width, height, margin = 400, 640, 50
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Reinforcement learning environment ')

# Pedestrian bounding box
img_pedestrian = pygame.image.load(steve_path)
img_pedestrian = pygame.transform.scale(img_pedestrian, (50,50))
img_pedestrian.convert()
rect_pedestrian = img_pedestrian.get_rect()
rect_pedestrian.center = width//2, 2*margin

# Vehicle bounding box
img_vehicle = pygame.image.load(robot_path)
img_vehicle = pygame.transform.scale(img_vehicle, (100,100))
img_vehicle.convert()
rect_vehicle = img_vehicle.get_rect()
rect_vehicle.center = width//2, height-55
obstacles = [rect_vehicle]

# Ellipse bounding box
#rect_ellipse = pygame.Rect(rect_pedestrian.left, rect_pedestrian.top, 40, 80)

# Screen boundaries
left_pad = pygame.Rect(-5, -5, 10, height)
right_pad = pygame.Rect(width-5, -5, 10, height)
top_pad = pygame.Rect(-5, -5, width, 10)
bottom_bad = pygame.Rect(0, height-5, width, 10)
pads = [top_pad, bottom_bad, left_pad, right_pad]

# Initial conditions
speedX_ped, speedY_ped = 0.1, 0.1
speedX_car, speedY_car = 0, 0.04
theta = random.uniform(0, 2*math.pi)
run = True

env = TC_v0.TC_environment()
env.reset()
experience_buffer = []
observation_set = []
counter = 0

while run:
    screen.fill((0, 0, 0))
    dt = clock.tick(30)
    counter += 1

    observation_set.append([rect_pedestrian.center, (speedX_ped, speedY_ped)])

    if counter % 4 == 0:
        experience_buffer.append(observation_set)
        observation_set = []

    rect_pedestrian.move_ip(math.cos(theta)*speedX_ped*float(dt), math.sin(theta)*speedY_ped*float(dt))
    rect_vehicle.move_ip(speedX_car*float(dt), -speedY_car*float(dt))

    if rect_pedestrian.collidelist(pads) != -1:
        speedY_ped = -speedY_ped
        speedX_ped = -speedX_ped
        theta = random.uniform(0, 2*math.pi)

    if rect_vehicle.collidelist(pads) != -1:
        speedY_car = -speedY_car
        speedX_car = -speedX_car
        theta = random.uniform(0, 2*math.pi)

    if rect_pedestrian.colliderect(rect_vehicle) == True:
        speedY_ped = -speedY_ped
        speedX_ped = -speedX_ped
        theta = random.uniform(0, 2*math.pi)

    screen.blit(img_pedestrian, rect_pedestrian)
    screen.blit(img_vehicle, rect_vehicle)
    pygame.draw.rect(screen, (0, 0, 0), rect_pedestrian, 1)
    pygame.draw.rect(screen, (0, 0, 0), rect_vehicle, 1)

    for pad in pads:
        pygame.draw.rect(screen, (255,255,153), pad)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

for i in experience_buffer:
    print(i)
    
quit()
