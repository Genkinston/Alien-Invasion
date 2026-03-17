class Settings:
    '''Класс для хранение всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует статические настройки игры.'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (123, 104, 238)
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 2.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
