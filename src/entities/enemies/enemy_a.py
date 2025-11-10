from entities.enemy import Enemy


class EnemyA(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_a")
        self.shot_delay = self.config.get(
            "initial_shot_delay", 20
        )  # allow time to get on screen

    def update(self):
        super().update()  # hit frames

        speed = self.config.get("speed", 1)
        self.x -= speed
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.shot_delay == 0:
            self.shot_delay = self.config.get("shot_delay", 120)
            bullet_speed = self.config.get("bullet_speed", 2)
            self.shoot_at_angle(bullet_speed, 180, 0, -8, -10)
            self.shoot_at_angle(bullet_speed, 180, 0, -8, 6)
        else:
            self.shot_delay -= 1
