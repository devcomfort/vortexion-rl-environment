from entities.enemy import Enemy


class EnemyC(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_c")
        self.flip_y = True if self.y < 96 else False
        self.speed = state.get_scroll_x_speed()

    def update(self):
        super().update()  # hit frames

        self.speed = self.game_state.get_scroll_x_speed()

        self.x -= self.speed
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.lifetime == 25 or self.lifetime == 50:
            bullet_speed = self.config.get("bullet_speed", 2)
            self.shoot_at_player(bullet_speed)
