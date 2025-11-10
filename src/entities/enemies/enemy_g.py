from entities.enemy import Enemy


class EnemyG(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_g")
        self.speed = -state.get_scroll_x_speed()

    def update(self):
        super().update()  # hit frames

        speed_x_offset = self.config.get("speed_x_offset", 0.5)
        if self.lifetime < 250:
            self.speed = -(self.game_state.get_scroll_x_speed() + speed_x_offset)
        else:
            self.flip_x = True
            self.speed = self.game_state.get_scroll_x_speed() + speed_x_offset

        if self.lifetime >= 250 and self.lifetime < 280:
            speed_y = self.config.get("speed_y", 1.5)
            if self.y < 96:
                self.y += speed_y
            else:
                self.y -= speed_y

        self.x += self.speed
        if self.lifetime > 300 and self.x > 255:
            self.remove = True
            return
