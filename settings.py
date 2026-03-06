class Settings:
    '''Класс для хранение всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (123, 104, 238)
        # Настройки корабля
        self.ship_speed = 1.5
