from entities.enemy import Enemy


class EnemyD(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_d")
        self.flip_y = True if self.y < 96 else False
        speed_x_offset = self.config.get("speed_x_offset", 0.25)
        self.vx = state.get_scroll_x_speed() + speed_x_offset
        self.vy = 0

    def update(self):
        super().update()  # hit frames

        self.x -= self.vx
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.vy == 0:
            if self.x - self.game_state.player.x < 24:
                speed_y = self.config.get("speed_y", 2)
                self.vy = speed_y if self.y < 96 else -speed_y
        else:
            self.y += self.vy
            if self.y + self.h < 16 or self.y > 176:
                self.remove = True
