import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        #初始化飞船并设置初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像获取其原图外接矩形
        self.origin_image = pygame.image.load('images/spaceship.png')
        #缩放比例
        scale_factor = 0.08
        new_width = int(self.origin_image.get_width()*scale_factor)
        new_height = int(self.origin_image.get_height()*scale_factor)
        #设置新尺寸的图像
        self.image = pygame.transform.scale(self.origin_image,(new_width,new_height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #centerx中储存小数
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在合适的地方绘制飞船"""
        self.screen.blit(self.image,self.rect)