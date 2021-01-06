import pygame as pg
from settings import *
import os
from main import *

class UserState:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # self.background = pg.display.get_num_displays()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.selecting = True
        self.clear = False
        self.start = True
        #self.usermap = usermap
        self.usermap = []
        """
        초기 맵 상태, 초기 유저 위치 확인인
        """

        with open('map_file3', 'r', encoding='utf-8') as file:
            for line in file:
                self.usermap.append(line.strip('\n').split(' '))
        with open('user_pos', 'r', encoding='utf-8') as file:
            cnt = False
            for line in file:
                if not cnt:
                    self.st_x = int(line)
                    cnt = True
                else:
                   self.st_y = int(line)

        # self.player_pos = [5, 5]
        # self.game_state = {}
        # self.game_state['player_pos'] = self.player_pos

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.explo = pg.sprite.Group()
        self.road = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.enemys = pg.sprite.Group()
        self.player = Player(self.st_y, self.st_x, self)  # self.player, Player객체 생성

        self.items = pg.sprite.Group()
        self.start_tick = pg.time.get_ticks()
        self.item_dic = {}
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

    def is_event(self, event, pos_y, pos_x):
        """
        event 발생 여부
        1. 몬스터 만났을 때 -> 결과에 따라 아이템 드랍?
        2. 아이템을 얻었을 때
        """
        if event == 'monster':
            self.res = send_event(event, pos_y, pos_x)
            del(self.enemys_dic[(pos_y, pos_x)])
            item = Item(pos_y, pos_x, self)
            self.item_dic[(pos_y,pos_x)] = item
            #self.items.add(item)
            # if self.res['f_result'] == '1':
            #     item = Item(self.res['cury'], self.res['curx'])
            #     self.item_dic[self.res['cury'], self.res['curx']] = item
        elif event == 'item':
            self.res = send_event(event,pos_y, pos_x)
            if (pos_y,pos_x) in self.item_dic:
                del(self.item_dic[(pos_y, pos_x)])
            road = Road(pos_y, pos_x)
            self.road_dic[(pos_y, pos_x)] = road

    def legal_moves(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                self.start = False

            if event.type == pg.KEYDOWN:
                key_event = pg.key.get_pressed()
                if key_event[pg.K_LEFT]:
                    self.player.left()
                elif key_event[pg.K_RIGHT]:
                    self.player.right()
                elif key_event[pg.K_UP]:
                    self.player.up()
                elif key_event[pg.K_DOWN]:
                    self.player.down()

    def start_screen(self):
        self.screen.fill(WHITE)
        for col in range(len(self.usermap)):
            for row in range(len(self.usermap)):
                if self.usermap[col][row] == "0" or self.usermap[col][row] == "3":
                    road = Road(col, row)
                    self.road_dic[(col, row)] = road

                elif self.usermap[col][row] == "2":
                    enemy = Enemy(col, row, self)
                    self.enemys_dic[(col, row)] = enemy

                elif self.usermap[col][row] == "1":
                    wall = Wall(col, row)
                    self.wall_dic[(col, row)] = wall

        pg.display.update()

    def result(self):
        """
        이동 전, 후 맵 출력
        ex) 전체 맵 중에 현재 위치 기준으로 주변 10x10 출력
        만약 가장 위쪽이여서 더이상 출력할 결과가 없다면? 유저가 이동?
        :return:
        1.현재 캐릭터 좌표 확인
        2.캐릭터 좌표 기준(센터)+_5 화면 출력
        3.화면이 경계선을 넘어가면 캐릭터만 이동?
        """

        self.road.empty()
        self.wall.empty()
        self.enemys.empty()
        self.items.empty()
        self.screen.fill(WHITE)

        pos_y = self.player.rect.y
        pos_x = self.player.rect.x

        for col in range(pos_y // 40 - 5, pos_y // 40 + 6):
            for row in range(pos_x // 40 - 5, pos_x // 40 + 6):
                if (col, row) == (pos_y // 40, pos_x // 40):
                    self.player.rect.y, self.player.rect.x = 200, 200
                elif (col, row) in self.road_dic.keys():
                    self.road_dic[(col, row)].update(col - (pos_y // 40 - 5), row - (pos_x // 40 - 5))
                    self.road.add(self.road_dic[(col, row)])

                elif (col, row) in self.wall_dic.keys():
                    self.wall_dic[(col, row)].update(col - (pos_y // 40 - 5), row - (pos_x // 40 - 5))
                    self.wall.add(self.wall_dic[(col, row)])

                elif (col, row) in self.enemys_dic.keys():
                    self.enemys_dic[(col, row)].update(col - (pos_y // 40 - 5), row - (pos_x // 40 - 5))
                    self.enemys.add(self.enemys_dic[(col, row)])

                elif (col, row) in self.item_dic.keys():
                    self.item_dic[(col, row)].update(col - (pos_y // 40 - 5), row - (pos_x // 40 - 5))
                    self.items.add(self.item_dic[(col, row)])


        self.road.draw(self.screen)
        self.wall.draw(self.screen)
        self.enemys.draw(self.screen)
        self.items.draw(self.screen)
        self.explo.draw(self.screen)
        pg.display.update()
        self.player.rect.y = pos_y
        self.player.rect.x = pos_x

        for col in range(pos_y // 40 - 5, pos_y // 40 + 6):
            for row in range(pos_x // 40 - 5, pos_x // 40 + 6):
                if (col, row) in self.road_dic.keys():
                    self.road_dic[(col, row)].update(col, row)
                elif (col, row) in self.wall_dic.keys():
                    self.wall_dic[(col, row)].update(col, row)
                elif (col, row) in self.enemys_dic.keys():
                    self.enemys_dic[(col, row)].update(col, row)
                elif (col, row) in self.item_dic.keys():
                    self.item_dic[(col, row)].update(col, row)


class Item(pg.sprite.Sprite):
    def __init__(self, col, row, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/potion.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self, col, row):
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, col, row, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/monster2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self, col, row):
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE


class Road(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/grass.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self, col, row):
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pg.image.load('Image/fire.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self, col, row):
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE


class Player(pg.sprite.Sprite):
    def __init__(self, col, row, game):
        self.groups = game.explo
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('Image/char.png')
        self.rect = self.image.get_rect()
        self.rect.x = row * TILESIZE
        self.rect.y = col * TILESIZE
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

    def enemy_collide(self):
        collide_enemy = pg.sprite.spritecollide(self, self.game.enemys, False)
        collide_wall = pg.sprite.spritecollide(self, self.game.wall, False)
        collide_item = pg.sprite.spritecollide(self, self.game.items, False)

        if collide_enemy:
            return 'monster'
        elif collide_wall:
            return 'wall'
        elif collide_item:
            #print('item')
            return 'item'
        else:
            return 'road'

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.enemy_collide()

    def down(self):
        self.pos_y += 40
        self.update()
        if self.enemy_collide() == 'wall':
            self.pos_y -= 40
            self.update()
        elif self.enemy_collide() == 'monster':
            self.game.is_event('monster', self.pos_y//40, self.pos_x//40)

        elif self.enemy_collide() == 'item':
            self.game.is_event('item', self.pos_y//40, self.pos_x//40)

    def right(self):
        self.pos_x += 40
        self.update()
        if self.enemy_collide() == 'wall':
            self.pos_x -= 40
            self.update()
        elif self.enemy_collide() == 'monster':
            self.game.is_event('monster', self.pos_y // 40, self.pos_x // 40)
        elif self.enemy_collide() == 'item':
            self.game.is_event('item', self.pos_y//40, self.pos_x//40)

    def left(self):
        self.pos_x -= 40
        self.update()
        if self.enemy_collide() == 'wall':
            self.pos_x += 40
            self.update()
        elif self.enemy_collide() == 'monster':
            self.game.is_event('monster', self.pos_y // 40, self.pos_x // 40)
        elif self.enemy_collide() == 'item':
            self.game.is_event('item', self.pos_y//40, self.pos_x//40)

    def up(self):
        self.pos_y -= 40
        self.update()
        if self.enemy_collide() == 'wall':
            self.pos_y += 40
            self.update()
        elif self.enemy_collide() == 'monster':
            self.game.is_event('monster', self.pos_y // 40, self.pos_x // 40)
        elif self.enemy_collide() == 'item':
            self.game.is_event('item', self.pos_y//40, self.pos_x//40)

