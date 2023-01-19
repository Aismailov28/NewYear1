from pygame import *
import pygame
from random import *
import math
from os import path
import time
from queue import PriorityQueue
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
pygame.init()
win_width = 1920
win_height = 1050
Fullcreen = (win_width, win_height)
flags = FULLSCREEN | DOUBLEBUF
window = display.set_mode((win_width, win_height), flags)
window.set_alpha(None)
window.fill(BLACK)
display.set_caption('Лабиринт')

angle = 180
UP = Vector2(0, -1)
DOWN = Vector2(-1, 0)
exhaust_images = []
exhaust_animation = pygame.time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
    # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y)).convert_alpha() 
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.pos = (player_x, player_y)
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.x = player_x
        self.rect.y = player_y
        self.offset = Vector2(1, 2)

class Player1(GameSprite):
    def __init__(self, picture, x, y, w, h, x_speed, y_speed, health):
        super().__init__(picture, x, y, w, h)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.direction = Vector2(self.offset)
        angle = 0
        self.pos = Vector2(x,y)
        self.health = health
        self.MANEUVERABILITY = 4
        self.direction = Vector2(UP)
        self.direction2 = Vector2(DOWN)
        self.ACCELERATION = 0.15
        self.velocity = Vector2(0, 0)
        self.ACCELERATION2 = 0.15
        self.direction_UP = (-1)
        self.direction_DOWN = (+1)
        self.Repulsion = False
        self.pos += self.velocity
        angle = self.direction.angle_to(UP)
        for i in range(1, 13):
            smoke = transform.scale(image.load(path.join(img_dir, f"smoke_{i}.png")), (35, 80))
            exhaust_images.append(smoke)



    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
        print(self.velocity[0])
        #print(self.pos)

    def deceleration(self):
        if self.velocity[0] > 0:
            self.velocity[0] += self.direction_UP * self.ACCELERATION2
        elif self.velocity[0] < 0:
            self.velocity[0] += self.direction_DOWN * self.ACCELERATION2

        if self.velocity[1] > 0:
            self.velocity[1] += self.direction_UP * self.ACCELERATION2
        elif self.velocity[1] < 0:
            self.velocity[1] += self.direction_DOWN * self.ACCELERATION2
    def repulsion(self):
        if self.rect.x >= 1770:
            if self.velocity[0] > 25:
                if self.rect.x >= 1620 and self.Repulsion == False:
                    self.velocity[0] = (-12)
                    self.Repulsion = True
                elif self.rect.x <= 1620:
                    self.velocity[0] = 0
                self.Repulsion = False
            elif self.velocity[0] > 15 and self.velocity[0] < 25:
                if self.rect.x >= 1660 and self.Repulsion == False:
                    self.velocity[0] = (-8)
                    self.Repulsion = True
                elif self.rect.x <= 1660:
                    self.velocity[0] = 0
                self.Repulsion = False
            elif self.velocity[0] < 15:
                if self.rect.x >= 1700 and self.Repulsion == False:
                    self.velocity[0] = (-3)
                    self.Repulsion = True
                elif self.rect.x <= 1700:
                    self.velocity[0] = 0
                self.Repulsion = False

        if self.rect.x <= 0:
            if self.velocity[0] < (-25):
                if self.rect.x <= 130 and self.Repulsion == False:
                    self.velocity[0] = (+12)
                    self.Repulsion = True
                elif self.rect.x >= 130:
                    self.velocity[0] = 0
                self.Repulsion = False
            elif self.velocity[0] < (-15) and self.velocity[0] > (-25):
                if self.rect.x <= 170 and self.Repulsion == False:
                    self.velocity[0] = (+8)
                    self.Repulsion = True
                elif self.rect.x >= 170:
                    self.velocity[0] = 0
                self.Repulsion = False
            elif self.velocity[0] > (-15):
                if self.rect.x <= 210 and self.Repulsion == False:
                    self.velocity[0] = (+3)
                    self.Repulsion= True
                elif self.rect.x >= 210:
                    self.velocity[0] = 0
                self.Repulsion = False

        if self.rect.y <= 0:
            if self.velocity[1] < (-25):
                if self.rect.y <= 150 and self.Repulsion == False:
                    self.velocity[1] = (+12)
                    self.Repulsion = True
                elif self.rect.y <= 150:
                    self.velocity[1] = 0
                self.Repulsion = False
            elif self.velocity[1] < (-15) and self.velocity[1] > (-25):
                if self.rect.y <= 190 and self.Repulsion == False:
                    self.velocity[1] = (+8)
                    self.Repulsion = True
                elif self.rect.y >= 190:
                    self.velocity[1] = 0
                self.Repulsion = False
            elif self.velocity[1] > (-15):
                if self.rect.y <= 230 and self.Repulsion == False:
                    self.velocity[1] = (+3)
                    self.Repulsion = True
                elif self.rect.y >= 230:
                    self.velocity[1] = 0
                self.Repulsion = False

        if self.rect.y >= 1030:
            if self.velocity[1] > (+25):
                if self.rect.y <= 880 and self.Repulsion == False:
                    self.velocity[1] = (-12)
                    self.Repulsion = True
                elif self.rect.y <= 880:
                    self.velocity[1] = 0
                self.Repulsion = False
            elif self.velocity[1] > (+15) and self.velocity[1] < (+25):
                if self.rect.y <= 840 and self.Repulsion == False:
                    self.velocity[1] = (-8)
                    self.Repulsion = True
                elif self.rect.y >= 840:
                    self.velocity[1] = 0
                self.Repulsion = False
            elif self.velocity[1] < (+15):
                if self.rect.y <= 800 and self.Repulsion == False:
                    self.velocity[1] = (-3)
                    self.Repulsion = True
                elif self.rect.y >= 800:
                    self.velocity[1] = 0
                self.Repulsion = False

    def collide_rect(self):
        dir = Vector2(player1.pos) - Vector2(player2.pos)
        repulsion_direction = Vector2(self.pos.x - player2.pos.x, self.pos.y - player2.pos.y)
        #repulsion_direction.normalize()
        force = 0.4
        player1.velocity += repulsion_direction * force
        player2.velocity -= repulsion_direction * force


    def handle_input(self):
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            if self.rect.x >= 0:
                self.accelerate()
            elif self.rect.x <= 0:
                self.repulsion()
            if self.rect.x >= 1770:
                self.repulsion()
            elif self.rect.x <= 1770:
                self.accelerate()
            if self.rect.y >= 0:
                self.accelerate()
            elif self.rect.y <= 0:
                self.repulsion()
            if self.rect.y <= 1030:
                self.deceleration
            elif self.rect.y >= 1030:
                self.repulsion()
            if self.rect.colliderect(bot.rect):
                self.repulsion()
            if self.rect.colliderect(player2.rect):
                self.repulsion()
            if self.rect.colliderect(player2):
                self.collide_rect()

        elif not is_key_pressed[pygame.K_UP]:
            if self.rect.x >= 0:
                self.deceleration()
            elif self.rect.x <= 0:
                self.repulsion()
            if self.rect.x <= 1770:
                self.deceleration()
            elif self.rect.x >= 1770:
                self.repulsion()
            if self.rect.y >= 0:
                self.deceleration()
            elif self.rect.y <= 0:
                self.repulsion()
            if self.rect.y >= 1030:
                self.deceleration
            elif self.rect.y <= 1030:
                self.repulsion()
            if self.rect.colliderect(bot.rect):
                self.repulsion()
            if self.rect.colliderect(player2.rect):
                self.repulsion()
            if self.rect.colliderect(player2):
                self.collide_rect()

    def update(self):
        self.pos += self.velocity
        angle = self.direction.angle_to(UP)
        self.rotated_surface = transform.rotozoom(self.image, angle, 1.0).convert_alpha() 
        rotated_surface_size = Vector2(self.rotated_surface.get_size())
        self.blit_position = self.pos - rotated_surface_size * 0.5
        #print(self.blit_position)
        self.rect = self.rotated_surface.get_rect(center=self.blit_position)
        window.blit(self.rotated_surface, self.blit_position)
        exhaust_animation.tick(60)
        current_frame = exhaust_animation.get_time() // 5 % len(exhaust_images)
        window.blit(exhaust_images[current_frame], self.pos)
        self.handle_input()

        return self.image
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
        rotated_velocity = self.velocity.rotate(angle)
        self.velocity = rotated_velocity

class Bot(Player1):
    def __init__(self, picture, x, y, w, h, x_speed, y_speed, health):
        Player1.__init__(self, picture, x, y, w, h, x_speed, y_speed, health)
        self.target = player1.pos  # Текущая цель для перемещения (точка на маршруте)
        self.w = w
        self.h = h
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.rect.center = (self.pos[0], self.pos[1])

    def update(self):
        # Update the bot's position based on the current speed
        self.pos += self.velocity
        players = [player1.pos, player2.pos] # List of all players
        print(self.pos)
        #self.find_target(players)

        # If a player is found, find a path to them
        if self.target is not None:
            start = (int(self.pos.x), int(self.pos.y))
            end = (int(self.target.x), int(self.target.y))

            # Find the path using the A* algorithm
            self.path = self.astar(start, end, self.neighbors, self.cost)
            if self.path:
                self.move = list(self.path).pop(0)
                self.rotate_towards(self.move)
                self.move_to(self.move)
            else:
                self.move = None

    def move_to(self, next):
        self.pos = Vector2(next[0], next[1])
        self.rect.center = (next[0], next[1])

    def cost(self, current, next):
        x1, y1 = current
        x2, y2 = next
        return abs(x1 - x2) + abs(y1 - y2)
    def heuristic(self, pos, goal):
        x, y = pos
        gx, gy = goal
        return abs(x - gx) + abs(y - gy)

    def rotate_towards(self, target_pos):
        # Calculate the angle between the current direction of the bot and the vector to the target point
        target_vector = Vector2(target_pos[0], target_pos[1]) - self.pos
        angle = self.direction.angle_to(target_vector)
        self.direction = self.direction.rotate(angle)
        self.image = transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def is_valid_pos(self, pos):
        x, y = pos
        if x < 0 or x >= win_width or y < 0 or y >= win_height:
            return False
        return True

    def find_target(self, players):
        # Finds the closest player to the bot
        closest_distance = None
        closest_player = None
        for player in players:
            distance = self.distance_to(player)
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_player = player
        self.target = closest_player
  
    def neighbors(self, pos):
        x, y = pos
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.is_valid_pos, results)
        return results
    
    def astar(self, start, goal, neighbors_func, cost_func):
        came_from = {}
        cost_so_far = {}
        priority_queue = PriorityQueue()
        priority_queue.put(start, 0)
        came_from[start] = None
        cost_so_far[start] = 0

        while not priority_queue.empty():
            current = priority_queue.get()

            if current[0] == goal[0] and current[1] == goal[1]:
                break

            for next in neighbors_func(current):
                new_cost = cost_so_far[current] + cost_func(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    priority_queue.put(next, priority)
                    came_from[next] = current
        return came_from, cost_so_far
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
class Vector_2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


class Player2(Player1):
    def __init__(self, picture, x, y, w, h, x_speed, y_speed, health):
        Player1.__init__(self, picture, x, y, w, h, x_speed, y_speed, health)
        
    def handle_input2(self):
        is_key_pressed = pygame.key.get_pressed()
    
        if is_key_pressed[pygame.K_d]:
            player2.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_a]:
            player2.rotate(clockwise=False)
        if is_key_pressed[pygame.K_w]:
            if self.rect.x >= 0:
                self.accelerate()
            elif self.rect.x <= 0:
                self.repulsion()
            if self.rect.x >= 1770:
                self.repulsion()
            elif self.rect.x <= 1770:
                self.accelerate()
            if self.rect.y >= 0:
                self.accelerate()
            elif self.rect.y <= 0:
                self.repulsion()
            if self.rect.y <= 1030:
                self.deceleration
            elif self.rect.y >= 1030:
                self.repulsion()
            if self.rect.colliderect(bot.rect):
                self.repulsion()
            if self.rect.colliderect(player1.rect):
                self.repulsion()
            if self.rect.colliderect(player1):
                self.collide_rect()

        elif not is_key_pressed[pygame.K_UP]:
            if self.rect.x >= 0:
                self.deceleration()
            elif self.rect.x <= 0:
                self.repulsion()
            if self.rect.x <= 1770:
                self.deceleration()
            elif self.rect.x >= 1770:
                self.repulsion()
            if self.rect.y >= 0:
                self.deceleration()
            elif self.rect.y <= 0:
                self.repulsion()
            if self.rect.y >= 1030:
                self.deceleration
            elif self.rect.y <= 1030:
                self.repulsion()
            if self.rect.colliderect(bot.rect):
                self.repulsion()
            if self.rect.colliderect(player1.rect):
                self.repulsion()
            if self.rect.colliderect(player1):
                self.collide_rect()
                
    def update(self):
        self.pos += self.velocity
        angle = self.direction.angle_to(UP)
        self.rotated_surface = transform.rotozoom(self.image, angle, 1.0)
        rotated_surface_size = Vector2(self.rotated_surface.get_size())
        self.blit_position = self.pos - rotated_surface_size * 0.5
        #print(self.blit_position)
        self.rect = self.rotated_surface.get_rect(center=self.blit_position)
        window.blit(self.rotated_surface, self.blit_position)
        self.handle_input2()
        self.rect.x += (player1.rect.x - self.rect.x) * 0.1 * dt
        self.rect.y += (player1.rect.y - self.rect.y) * 0.1 * dt

class Snowflake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.dy = uniform(3, 5)
snowflakes = []

def create_snowflake():
    x = randint(0, 1920)
    y = 0
    size = randint(1, 3)
    snowflakes.append(Snowflake(x, y, size))
def move_snowflakes():
    for snowflake in snowflakes:
        if snowflake.size == 1:
            snowflake.dy = 3
        elif snowflake.size == 2:
            snowflake.dy = 4
        elif snowflake.size == 3:
            snowflake.dy = 5
        snowflake.y += snowflake.dy
        if snowflake.y > 1080:
            snowflakes.remove(snowflake)

#start = Vector_2(0, 0)
#end = Vector_2(5, 5)
      
img_dir = r'C:\\Users\\Programmer\\Desktop\\NewYear\\Exhaust'


display.set_caption('Гонки')

barriers = sprite.Group()
healths = sprite.Group()

#создаём стены картинки
w1 = GameSprite('long.png', 0, 0, 0, 0)
w2 = GameSprite('short.png', 0, 0, 0, 0)
w3 = GameSprite('normal.png', 300, 300, 500, 100)
w4 = GameSprite('angle.png', 0, 0, 0, 0)
#добавляем стены в группу
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)

player1 = Player1('Sleigh.png', 400, 100, 52, 85, 0, 0, 5)
player2 = Player2('Sleigh.png', 100, 950, 52, 85, 0, 0, 5)
bot = Bot('Sleigh.png', 1800, 500, 52, 85, 0, 0, 5)

start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0

i = 0
finish = False

FPS = 60
clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(50)
    for e in event.get():
       if e.type == QUIT:
           run = False
 
    if not finish:
        counter+=1
        if (time.time() - start_time) > x :
            print("FPS: ", counter / (time.time() - start_time))
            counter = 0
            start_time = time.time()
        create_snowflake()
        # Перемещение снежинок
        move_snowflakes()

        window.fill(BLACK)
        dt = clock.tick(60)

        #включаем движение
        player1.update()
        player2.update()
        #bot.update()
        #pygame.display.flip()  # Обновляем экран

        for snowflake in snowflakes:
            pygame.draw.circle(window, (255, 255, 255), (snowflake.x, snowflake.y), snowflake.size)
    
        # Обновление экрана

    display.update()
    clock.tick(FPS)
