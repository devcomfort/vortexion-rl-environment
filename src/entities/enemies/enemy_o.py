from entities.enemy import Enemy


class EnemyO(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_o")
        initial_shot_delay = self.config.get("initial_shot_delay", 40)
        self.shot_delay = initial_shot_delay  # allow time to get on screen

    def update(self):
        super().update()  # hit frames

        speed = self.config.get("speed", 2.5)
        self.x -= speed
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.shot_delay == 0:
            self.shot_delay = self.config.get("shot_delay", 120)
            bullet_speed = self.config.get("bullet_speed", 2)
            self.shoot_at_player(bullet_speed)
        else:
            self.shot_delay -= 1
