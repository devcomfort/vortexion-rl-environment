from entities.enemy import Enemy


class EnemyI(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_i")
        self.vel_y_index = 0

    def update(self):
        super().update()  # hit frames

        vel_y = self.config.get("vel_y", [-0.5, 1, -1.25, 1.25, -1, 0.5])
        vel_y_change_interval = self.config.get("vel_y_change_interval", 45)

        if self.vel_y_index < len(vel_y) - 1:
            if self.lifetime % vel_y_change_interval == 0:
                self.vel_y_index += 1

        self.y += vel_y[self.vel_y_index]

        if self.lifetime == 30:
            bullet_speed = self.config.get("bullet_speed", 1.5)
            self.shoot_at_player(bullet_speed)

        speed = self.config.get("speed", 1.5)
        self.x -= speed
        if self.x + self.w < 0:
            self.remove = True
            return
