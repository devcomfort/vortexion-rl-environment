from entities.enemy import Enemy


class EnemyE(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_e")
        # spawn on left
        self.x -= 256 + 16

    def update(self):
        super().update()  # hit frames

        speed = self.config.get("speed", 1)
        self.x += speed
        if self.x > 255:
            self.remove = True
            return

        if self.lifetime == 200:
            bullet_speed = self.config.get("bullet_speed", 2)
            self.shoot_at_angle(bullet_speed, 180)
