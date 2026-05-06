import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# character variable
head_x, head_y = 50, 450
chest_x, chest_y = 46, 460
left_leg_x, left_leg_y = 49, 480
right_leg_x, right_leg_y = 57, 480
left_right = 5
copy_of_right_leg_x = 260

# gravity
velocity = 0
space = 0
gravity = 3
jump_power = -30
onground = True

# reuduce
new_block = False
replace = True
first_maze = 50
reduce_2 = 50
reduce_speed = -40
# right_leg = None

# game variable
plot = 250
decrement_plot = 550

# Text
font=pygame.font.SysFont("None",48)

clock = pygame.time.Clock()
run = True

def gravityy():
    global jump_power, velocity, space,copy_of_right_leg_x
    global chest_y, head_y, left_leg_y, right_leg_y, onground, plot,run

    space += gravity
    velocity = space
    head_y += velocity
    chest_y += velocity
    left_leg_y += velocity
    right_leg_y += velocity 
    for out in [(200<right_leg_x and right_leg_x<250),(plot>copy_of_right_leg_x),(650<right_leg_x and right_leg_x<700)]:
        if out is True:
            if right_leg_y>520:
                run=False
    ground()
def character():
    pygame.draw.rect(screen, black, (head_x, head_y, 10, 10))
    pygame.draw.rect(screen, black, (chest_x, chest_y, 18, 20))
    pygame.draw.rect(screen, black, (left_leg_x, left_leg_y, 3, 20))
    pygame.draw.rect(screen, black, (right_leg_x, right_leg_y, 3, 20))
    pygame.draw.circle(screen, black, (right_leg_x + 1, right_leg_y + 17), 5)
    pygame.draw.circle(screen, black, (left_leg_x + 1, left_leg_y + 17), 5)


def reduce_block():
    global first_maze
    first_maze += reduce_speed


def plot_increment():
    global plot, decrement_plot
    if plot < 610:
        plot += 6.5
        decrement_plot -= 10


def reduce_block_2():
    global reduce_2
    reduce_2 += (reduce_speed + 30)


def fall():
    global plot, onground, right_leg_x, run
    if plot > copy_of_right_leg_x:
        run = False


def ground():
    global head_y, chest_y, left_leg_y, right_leg_y, onground
    if left_leg_y >= 480:
        head_y = 450
        chest_y = 460
        left_leg_y = 480
        right_leg_y = 480
        onground = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if onground:
                if event.key == pygame.K_UP:
                    space = jump_power
                    onground = False
                if event.key == pygame.K_q:
                    run = False

    screen.fill(white)

    character()
    gravityy()

    press = pygame.key.get_pressed()

    if press[pygame.K_RIGHT]:
        head_x += left_right
        chest_x += left_right
        left_leg_x += left_right
        right_leg_x += left_right
        if copy_of_right_leg_x < right_leg_x:
            copy_of_right_leg_x += left_right

    if press[pygame.K_LEFT]:
        head_x -= left_right
        chest_x -= left_right
        right_leg_x -= left_right
        left_leg_x -= left_right
        if copy_of_right_leg_x>270:
            copy_of_right_leg_x-= left_right

    if right_leg_x > 200:
        new_block = True
        reduce_block()

    if right_leg_x > 350:
        plot_increment()

    if new_block:
        pygame.draw.rect(screen, red, (plot, 503, decrement_plot, 100), 200)
        pygame.draw.rect(screen, red, (600, 503, 50, 100))
        replace = False

    if replace:
        pygame.draw.rect(screen, red, (250, 503, 550, 100), 200)

    if right_leg_x > 450:
        pygame.draw.rect(screen, red, (650, 503, reduce_2, 100), 200)

    if right_leg_x > 610:
        reduce_block_2()
    
    if right_leg_x>740:
        text=font.render("You Win!!!",True,black)
        screen.blit(text,(300,400))

    if right_leg_x>780:
        run=False

    pygame.draw.rect(screen, red, (700, 503, 100, 100), 200)

    # first block
    pygame.draw.rect(screen, red, (0, 503, 200, 100), 200)
    pygame.draw.rect(screen, red, (200, 503, first_maze, 100), 200)

    fall()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
