from entities.enemy import Enemy


class EnemyJ(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_j")
        self.speed_x = state.get_scroll_x_speed()

    def update(self):
        super().update()  # hit frames

        self.speed_x = self.game_state.get_scroll_x_speed()

        self.x -= self.speed_x
        if self.x + self.w < 0:
            self.remove = True
            return

        shot_interval = self.config.get("shot_interval", 120)
        if self.lifetime % shot_interval == 0:
            bullet_speed = self.config.get("bullet_speed", 1.5)
            self.shoot_at_angle(bullet_speed, 210)
            self.shoot_at_angle(bullet_speed, 195, 10)
            self.shoot_at_angle(bullet_speed, 180, 20)
            self.shoot_at_angle(bullet_speed, 165, 30)
            self.shoot_at_angle(bullet_speed, 150, 40)
