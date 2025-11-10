from entities.enemy import Enemy


class EnemyF(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_f")
        self.flip_y = True if self.y < 96 else False
        self.speed_x = state.get_scroll_x_speed()

    def shoot(self):
        bullet_speed = self.config.get("bullet_speed", 2)
        # top
        if self.y < 96:
            self.shoot_at_angle(bullet_speed, 90)
            self.shoot_at_angle(bullet_speed, 110)
            self.shoot_at_angle(bullet_speed, 130)
        else:  # bottom
            self.shoot_at_angle(bullet_speed, 230)
            self.shoot_at_angle(bullet_speed, 250)
            self.shoot_at_angle(bullet_speed, 270)

    def update(self):
        super().update()  # hit frames

        self.speed_x = self.game_state.get_scroll_x_speed()

        self.x -= self.speed_x
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.lifetime == 100 or self.lifetime == 200 or self.lifetime == 300:
            self.shoot()
