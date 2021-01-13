# Will Butler, wgb6dwp
# Alex Taing alt6yzw

# main character sprite from http://opengameart.org/content/detective by artist jordyadan-- licensed in public domain
# background is a photo taken of UVa grounds by Alex Taing
# supply art created in PowerPoint by Alex Taing

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
start_screen1 = gamebox.from_text(400, 250, "Journey of the Student", 30, "blue", italic=True)
start_screen2 = gamebox.from_text(400, 285, "Alex Taing (alt6yzw) and Will Butler (wgb6dwp)", 30, "blue", italic=True)
start_screen3 = gamebox.from_text(400, 320, "Jump on top of the bad grades to defeat them,", 30, "blue", italic=True)
start_screen4 = gamebox.from_text(400, 355, "defeat them all, collect the supplies, and reach the end to win!", 30, "blue", italic=True)
start_screen5 = gamebox.from_text(400, 390, "Press space to start", 30, "blue", italic=True)
background = gamebox.from_image(4000, 50, "background.jpg")

supplies_image = gamebox.load_sprite_sheet('supplies.png', 2, 3)

spacing = 0
supplies = []
got_suppliesx = [50, 100, 150, 200, 250, 300]
for image in supplies_image:
    supplies.append(gamebox.from_image(random.randrange(400 + spacing, 800 + spacing), -100, image))
    spacing += 600
for each in supplies:
    each.scale_by(.20)


def draw_supplies():
    '''
    this function draws school supplies, denotes their location, and allows player to collect supplies (collectibles)
    :return: None
    '''
    global word_supplies
    word_supplies = gamebox.from_text(camera.topleft[0] + 60, 30, "SUPPLIES", 30, "white", False, False)
    global got_supplies
    for tool in supplies:
        camera.draw(tool)
        for image in walker[1:8]:
            for obstacle in noninteractives:
                if tool.x - image.x <= 500 and tool.speedy == 0 and not (tool.touches(obstacle) or tool.touches(floor))\
                        and not (tool.x - image.x < 0 and tool.y < 200):
                    tool.speedy = .1
                    tool.move_speed()
                else: tool.speedy = 0
                tool.move_to_stop_overlapping(obstacle)
            if image.touches(tool):
                tool.center = (camera.topleft[0] + (got_suppliesx[supplies.index(tool)]),
                               70)
                tool.speedy = 0
                tool.move_speed()
            if tool.x - image.x < 0 and tool.y < 200:
                tool.center = (camera.topleft[0] + (got_suppliesx[supplies.index(tool)]),
                               70)




game_on = False
game_off = False
floor = gamebox.from_color(400, 550, "dark green", 20000, 100)
noninteractives = [floor, gamebox.from_color(700, 500, "dark green", 100, 100),
                   gamebox.from_color(800, 500, "dark green", 100, 200),
                   gamebox.from_color(900, 500, "dark green", 100, 100),
                   gamebox.from_color(1000, 500, "dark green", 100, 100),
                   gamebox.from_color(1300, 500, "dark green", 100, 200),
                   gamebox.from_color(1500, 500, "dark green", 100, 200),
                   gamebox.from_color(2000, 500, "dark green", 200, 50),
                   gamebox.from_color(2200, 500, "dark green", 200, 100),
                   gamebox.from_color(2400, 500, "dark green", 200, 150),
                   gamebox.from_color(2600, 500, "dark green", 200, 200),
                   gamebox.from_color(2800, 500, "dark green", 300, 400),
                   gamebox.from_color(3200, 500, "dark green", 200, 200),
                   gamebox.from_color(3600, 500, "dark green", 200, 200),
                   gamebox.from_color(3800, 500, "dark green", 200, 300),
                   gamebox.from_color(4200, 500, "dark green", 400, 150),
                   gamebox.from_color(4450, 500, "dark green", 100, 200),
                   gamebox.from_color(4550, 500, "dark green", 100, 250),
                   gamebox.from_color(4650, 500, "dark green", 100, 300),
                   gamebox.from_color(4750, 500, "dark green", 100, 350),
                   gamebox.from_color(4850, 500, "dark green", 100, 400),
                   gamebox.from_color(5220, 250, "dark green", 510, 50),
                   gamebox.from_color(4950, 500, "dark green", 100, 200),
                   gamebox.from_color(5580, 500, "dark green", 100, 600),
                   gamebox.from_color(5680, 500, "dark green", 100, 200),
                   gamebox.from_color(6400, 500, "dark green", 400, 100)]



def draw_noninteractives():
    """
    this function draws all of the terrain in the game.
    :return: None
    """
    for item in noninteractives:
        camera.draw(item)

gravity = []
walker_ = []
walker = []
part = 0

def make_student():
    """
    this function divides a sprite sheet of the character into parts that are added into a list to create a walking,
    standing, and jumping animation.
    :return: This list of sprite sheet parts.
    """
    global part
    spritesheet = "charzera.png"
    images = gamebox.load_sprite_sheet(spritesheet, 3, 14)
    for image in images:
        walker_.append(gamebox.from_image(0, 470, image))
    for frame in walker_:
        frame.scale_by(1.5)
    for image in walker_[:7]:
        walker.append(image)
    walker.append(walker_[13])
    walker.append(walker_[38])
    print(walker)
    return walker


def move_student(keys):
    """
    this function takes user input and applies it to character animation and movement. this function applies gravity to
    the character.
    :param keys: it takes in user input (up, down, left, right)
    :return: None
    """
    global part
    global gravity
    if pygame.K_RIGHT in keys:
        if pygame.K_UP in keys:
            camera.draw(walker[8])
            for image in walker:
                image.x += 10
                for obstacle in noninteractives:
                    if image.bottom_touches(obstacle) and obstacle.top_touches(image):
                        image.speedy = -17
                        gravity = []

                image.move_speed()
        else:
            camera.draw(walker[int(part) % 7])
            part += 1
            for image in walker:
                image.x += 10
        for image in walker:
            camera.center = [image.center[0], 300]
    elif pygame.K_LEFT in keys:
        if pygame.K_UP in keys:
            camera.draw(walker[8])
            for image in walker:
                image.x -= 10
                for each in noninteractives:
                    if image.bottom_touches(each):
                        image.speedy = -17
                        gravity = []
                        break
                image.move_speed()
        else:
            camera.draw(walker[int(part) % 7])
            part -= 1
            for image in walker:
                image.x -= 10
        for image in walker:
            camera.center = [image.center[0], 300]
    elif pygame.K_UP in keys:
        camera.draw(walker[8])
        for image in walker:
            for each in noninteractives:
                if image.bottom_touches(each):
                    image.speedy = -17
                    image.move_speed()
    elif pygame.K_UP not in keys and (pygame.K_LEFT not in keys) and pygame.K_RIGHT not in keys:
        camera.draw(walker[7])
    for image in walker:  # Gravity
        for each in noninteractives:
            if image.bottom_touches(each):
                gravity.append(True)
            else:
                gravity.append(False)
        if True not in gravity:
            image.speedy += 3
            image.move_speed()
        gravity = []

    for frame in walker:
        for item in noninteractives:
            frame.move_to_stop_overlapping(item)
    # Background movement
    for images in walker:
            background.x = (images.x*0.9) + 500


enemies = [gamebox.from_text(1150, 475, "C-", 60, "red", True),
           gamebox.from_text(2700, 275, "D+", 60, "red", True),
           gamebox.from_text(3000, 475, "D", 60, "red", True),
           gamebox.from_text(4400, 425, "D-", 60, "red", True),
           gamebox.from_text(5700, 475, "F-", 200, "red", True)]


enemy_speed = -6


def enemy_start():  # Initializes enemy movement and then breaks in a separate function, else it resets movement at -10 every time the function runs.
    global enemy_speed
    for enemy in enemies:
        for image in walker:
            if (enemy.x - image.x > 500):
                    enemy.speedx = 0
    for enemy in enemies:
        for image in walker:
            if (enemy.x - image.x <= 500) and enemy.speedx == 0:
                enemy.speedx = enemy_speed
                break


gravity1 = []


def enemy_move():
    """
    this function automates enemy movement, starting when the character comes within a certain distance, and switching
    directions when enemies hit a wall. this function also applies gravity to enemies.
    :return: None
    """
    global gravity1
    global enemy_speed
    for enemy in enemies:
        # enemy.move_speed()
        already_touched = False
        for obstacle in noninteractives:
            if (enemy.left_touches(obstacle) or enemy.right_touches(obstacle)) and already_touched == False:
                already_touched = True
                # if not enemy.bottom_touches(obstacle): #Originally changed enemy direction if it touched obstacle at all. I changed this so that it only switches direction if it touches the side of an obstacle
                enemy.speedx *= -1
        enemy.move_speed()

    for enemy in enemies:
        camera.draw(enemy)
    for enemy in enemies:
        for image in walker:
            if image.bottom_touches(enemy):
                if enemy.top_touches(image):
                    enemies.remove(enemy)
                    break
    for enemy in enemies:  # Gravity
        for obstacle in noninteractives:
            enemy.move_to_stop_overlapping(obstacle)
            if enemy.bottom_touches(obstacle):
                gravity1.append(True)
            else:
                gravity1.append(False)
        if True not in gravity1:
            enemy.speedy += 3
            enemy.move_speed()
        gravity1 = []


# Lives
life_count = [1, 2, 3]


def lives_box():
    """
    this function keeps track of character lives, and updates the interface in the top right corner of the screen
    :return: a list that consists of the lives the character has left
    """
    global current_lives
    global life_count
    global word_lives
    word_lives = gamebox.from_text(camera.topright[0] - 60, 30, "LIVES", 30, "white", False, False)
    current_lives = [gamebox.from_circle(int(camera.topright[0]) - 80, 60, "red", 10),
                     gamebox.from_circle(int(camera.topright[0]) - 50, 60, "red", 10),
                     gamebox.from_circle(int(camera.topright[0]) - 20, 60, "red", 10)]
    if game_on:
        for life in current_lives:
            if 3 in life_count:
                camera.draw(life)  # 3 lives = draw all lives
            elif 2 in life_count:
                camera.draw(current_lives[0])  # 2 lives = draw 2 lives
                camera.draw(current_lives[1])
            else:
                camera.draw(current_lives[0])

    return current_lives


count = 1500


def lose_life():
    """
    this function removes a life from the top right corner of the screen if the character either touches an enemy for
    its first time or after a certain period of time after that.
    :return: a list that consists of the lives the character has left
    """
    global game_off
    global count
    global current_lives
    for image in walker:  # When student touches the side of an enemy, they lose a life.
        for enemy in enemies:
            if image.touches(enemy):
                if not image.bottom_touches(
                        enemy):  # Player bottom has to touch enemy to not get hurt (need to make way for player bottom to have to touch enemy TOP)
                    if count == 1500:  # If recovery is recharged
                        if len(life_count) == 3:
                            life_count.remove(3)
                            count = 0  # Restart recovery
                        elif len(life_count) == 2:
                            life_count.remove(2)
                            count = 0  # Restart recovery
                        else:  # If player is on their last life
                            game_off = True

    return current_lives


def recovery():  # Gives player a recovery of about 2 seconds
    """
    this function give the character an invincibility period after the bottom of the character touches the top of an
    enemy
    :return: the invincibility timer
    """
    global count
    for image in walker:
        for enemy in enemies:
            if image.touches(enemy):
                if image.bottom_touches(enemy) and enemy.top_touches(image):
                    if count == 1500:
                        break
                    else:
                        count += 1
            elif count != 1500:
                count += 1
    return count


dub = gamebox.from_text(6400, 160, "CONGRATULATIONS!!!", 40, "blue", True)
dub1 = gamebox.from_text(6400, 210, "YOU\'VE DEFEATED THE BAD GRADES!!!", 40, "blue", True)

As = [gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True),
      gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+", random.randint(40, 80), "red", True)]

supply_count = 0
def victory():
    """
    this function draws a victory/loss screen at the end of the level
    :return: None
    """
    global supply_count
    supply_count = 0
    for tools in supplies:
        if tools.y < 200:
            supply_count += 1
    supply_score = gamebox.from_text(6400, 260, "You've collected" + str(supply_count) + " out of 6 supplies", 40,
                                         "blue")
    for image in walker:
        if image.x >= 6200:
            if len(enemies) == 0:
                for A in As:
                    camera.draw(A)
                    A.speedy = .1
                    A.move_speed()
                    if A.y > 600:
                        As.remove(A)
                        As.append(gamebox.from_text(random.randint(6000, 6800), random.randint(50, 400), "A+",
                                                    random.randint(40, 80), "red", True))
                camera.draw(dub)
                camera.draw(dub1)
                camera.draw(supply_score)
            else:
                camera.draw(
                    gamebox.from_text(6400, 160, "Sorry, you must have let some bad grades slip!", 30, "blue", True))
                camera.draw(supply_score)






make_student()


def tick(keys):
    """
    this function cycles through necessary code 30 times a second to create the game
    :param keys: this takes key strokes from user to manipulate aspects of the game
    :return: None
    """
    global game_on
    global count
    global student
    if game_on is False:
        camera.clear('red')
        camera.draw(start_screen1)
        camera.draw(start_screen2)
        camera.draw(start_screen3)
        camera.draw(start_screen4)
        camera.draw(start_screen5)

    else:
        camera.clear('blue')

    if pygame.K_SPACE in keys:
        game_on = True

    if game_on:
        camera.draw(background)
        draw_noninteractives()
        move_student(keys)
        for image in walker:
            camera.center = [image.center[0], 300]
        enemy_start()
        enemy_move()
        lives_box()
        recovery()
        lose_life()
        victory()
        draw_supplies()
        camera.draw(word_supplies)
        camera.draw(word_lives)


    if game_off == True:
        camera.draw(gamebox.from_color(image.x, 300, 'red', 800, 600))
        camera.draw(gamebox.from_text(image.x, 300, "Class Canceled", 40, "blue", italic=True))
    camera.display()

gamebox.timer_loop(30, tick)
