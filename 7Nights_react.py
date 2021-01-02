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
        #self.load_date()

        self.usermap = []
        with open('map_file', 'r') as file:
            for line in file:
                self.usermap.append(line.strip('\n').split(' '))
        # self.st_x = 44
        # self.st_y = 38
        self.st_x = 0
        self.st_y = 0

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.explo = pg.sprite.Group()
        self.road = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.enemys = pg.sprite.Group()  # 적 sprite 그룹 생성
        self.player = Player(self.st_y, self.st_x, self)  # self.player, Player객체 생성

        #self.player= pg.sprite.Group()
        #self.players.add(self.player)

        self.items = pg.sprite.Group()
        self.start_tick = pg.time.get_ticks()
        self.run()

    def run(self):
        self.playing = True
        self.clock.tick(FPS)
        while self.playing:
            self.start_screen()
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
        self.p_lx = max(self.st_x-10, 0)
        self.p_rx = min(self.st_x+10, len(self.usermap))
        self.p_ly = max(self.st_y-10, 0)
        self.p_ry = min(self.st_y+10, len(self.usermap))

        for col in range(self.p_ly,self.p_ry):
            for row in range(self.p_lx, self.p_rx):
                if self.usermap[col][row] == "0":
                    road = Road(col, row)
                    self.all_sprites.add(road)
                    self.road.add(road)
                elif self.usermap[col][row] == "1":
                    wall = Wall(col,row)
                    self.all_sprites.add(wall)
                    self.wall.add(wall)


        self.all_sprites.draw(self.screen)
        #self.players.draw(self.screen)
        pg.display.update()

    def result(self):
        """
        이동 전, 후 맵 출력
        ex) 전체 맵 중에 현재 위치 기준으로 주변 10x10 출력
        만약 가장 위쪽이여서 더이상 출력할 결과가 없다면? 유저가 이동?
        :return:
        """



class Road(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/wood.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
        self.rect.center = (self.rect.x, self.rect.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/water.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
        self.rect.center = (self.rect.x, self.rect.y)


class Player(pg.sprite.Sprite):

    def __init__(self,col,row, game):
        #self.groups = game.player
        pg.sprite.Sprite.__init__(self)
        self.game = game
        #self.image = pg.image.load(os.path.join('Image/player.png')).convert_alpha()
        self.image = pg.image.load('Image/player.png')
        self.rect = self.image.get_rect()
        self.pos_x = row * TILESIZE
        self.pos_y = col * TILESIZE
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.rect.center = (self.pos_x, self.pos_y)

    def down(self):
        self.pos_y+=10
        self.update()
    def right(self):
        self.pos_x+=10
        self.update()
    def left(self):
        self.pos_x-=10
        self.update()
    def up(self):
        self.pos_y-=10
        self.update()

g = UserState()
while g.start:
    g.new()



