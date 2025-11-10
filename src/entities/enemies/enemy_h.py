from entities.enemy import Enemy


class EnemyH(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_h")
        bounce_vel = self.config.get("bounce_vel", 5)
        self.vel_y = bounce_vel

    def update(self):
        super().update()  # hit frames

        speed_x = self.config.get("speed_x", 1.5)
        self.x -= speed_x

        gravity = self.config.get("gravity", 0.2)
        self.vel_y += gravity
        self.y += self.vel_y

        if self.y >= 136:
            self.y = 136
            bounce_vel = self.config.get("bounce_vel", 5)
            self.vel_y = -bounce_vel

        if self.x + self.w < 0:
            self.remove = True
            return
