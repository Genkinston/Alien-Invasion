class Settings:
    '''Класс для хранение всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (123, 104, 238)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
