import random
import pygame

# 定义屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向从上向下移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """设置背景精灵"""

    def update(self):
        # 调用父类实现：垂直移动
        super().update()
        # 判断是否移出屏幕，如果移出，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 调用父类方法
        super().__init__('./images/enemy1.png')
        # 指定初始随机速度
        self.speed = random.randint(1, 3)
        # 指定初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            # kill 方法可以将精灵从所有精灵组中移出，就会调用__del__
            self.kill()

    def __del__(self):
        print("enemy died %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类，设置 image&speed
        super().__init__('./images/me1.png', 0)
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 一次发射三个子弹
        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        # 调用父类方法，子弹沿垂直飞行
        super().update()
        # 子弹飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('delete bullet...')
