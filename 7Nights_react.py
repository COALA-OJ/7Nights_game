import pygame as pg
from settings import *
import os
class UserState:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.selecting = True
        self.clear = False
        self.start = True
        self.usermap = []

        with open('map_file', 'r') as file:
            for line in file:
                self.usermap.append(line.strip('\n').split(' '))
        # self.st_x = 44
        # self.st_y = 38
        self.st_x = 20
        self.st_y = 15

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.explo = pg.sprite.Group()
        self.road = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.enemys = pg.sprite.Group()
        self.player = Player(self.st_y, self.st_x, self)  # self.player, Player객체 생성

        #self.player= pg.sprite.Group()
        #self.players.add(self.player)

        self.items = pg.sprite.Group()
        self.start_tick = pg.time.get_ticks()
        self.road_dic = {}
        self.wall_dic = {}
        self.enemys_dic = {}
        self.run()

    def run(self):
        self.playing = True
        self.clock.tick(FPS)
        self.start_screen()
        while self.playing:
            self.result()
            self.legal_moves()


    def is_evnet(self):
        """
        event 발생 여부
        1. 몬스터 만났을 때
        2. 아이템을 얻었을 때
        """

    def legal_moves(self):
        """
        이동키를 입력 받았을 때 이동 가능한 곳 인지 확인
        'up' 'down' 'left' 'right'
        벽이라면 이동 불가능, 이벤트 발생 여부 체크?
        게임을 끝내고 싶을 때
        :return: True/False
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                self.start = False

            if event.type == pg.KEYDOWN:
                key_event = pg.key.get_pressed()
                if key_event[pg.K_LEFT]: self.player.left()
                elif key_event[pg.K_RIGHT]: self.player.right()
                elif key_event[pg.K_UP]: self.player.up()
                elif key_event[pg.K_DOWN]: self.player.down()


    def start_screen(self):
        self.screen.fill(WHITE)
        for col in range(len(self.usermap)):
            for row in range(len(self.usermap)):
                if self.usermap[col][row] == "0":
                    road = Road(col, row)
                    self.road_dic[(col,row)] = road

                elif self.usermap[col][row] == "1":
                    enemy = Enemy(col,row,self)
                    self.enemys_dic[(col, row)] = enemy

                elif self.usermap[col][row] == "2":
                    wall = Wall(col, row)
                    self.wall_dic[(col, row)] = wall

        pg.display.update()

    def result(self):
        """
        이동 전, 후 맵 출력
        ex) 전체 맵 중에 현재 위치 기준으로 주변 10x10 출력
        만약 가장 위쪽이여서 더이상 출력할 결과가 없다면? 유저가 이동?
        :return:
        """
        self.p_lx = max(self.st_x - 5, 0)
        self.p_rx = min(self.st_x + 5, len(self.usermap))
        self.p_ly = max(self.st_y - 5, 0)
        self.p_ry = min(self.st_y + 5, len(self.usermap))

        self.road.empty()
        self.wall.empty()
        self.enemys.empty()
        for col in range(50):
            for row in range(50):
                if (col,row) in self.road_dic.keys():
                    self.road.add(self.road_dic[(col,row)])
                elif (col,row) in self.wall_dic.keys():
                    self.wall.add(self.wall_dic[(col, row)])
                elif (col, row) in self.enemys_dic.keys():
                    self.enemys.add(self.enemys_dic[(col, row)])

        self.road.draw(self.screen)
        self.wall.draw(self.screen)
        self.enemys.draw(self.screen)
        self.explo.draw(self.screen)
        pg.display.update()

class Enemy(pg.sprite.Sprite):
    def __init__(self, col, row, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class Road(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/wood.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
        #self.rect.center = (self.rect.x, self.rect.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/fire.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
        #self.rect.center = (self.rect.x, self.rect.y)


class Player(pg.sprite.Sprite):

    def __init__(self,col,row, game):
        self.groups = game.explo
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.image.load(os.path.join('Image/player.png')).convert_alpha()
        self.image = pg.image.load('Image/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

    def enemy_collide(self):
        collide_enemy = pg.sprite.spritecollide(self, self.game.enemys, False)
        collide_wall = pg.sprite.spritecollide(self, self.game.wall, False)

        if collide_enemy:
            print('colidge')
        elif collide_wall:
            print('wall')

    def update(self):
        self.enemy_collide()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def down(self):
        self.pos_y+=40
        self.update()
    def right(self):
        self.pos_x+=40
        self.update()
    def left(self):
        self.pos_x-=40
        self.update()
    def up(self):
        self.pos_y-=40
        self.update()

g = UserState()
while g.start:
    g.new()



