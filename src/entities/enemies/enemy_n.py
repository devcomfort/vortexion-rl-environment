from entities.enemy import Enemy


class EnemyN(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_n")
        speed_y = self.config.get("speed_y", 0.5)
        if self.y < 96:
            self.speed_y = speed_y
        else:
            self.speed_y = -speed_y

    def update(self):
        super().update()  # hit frames

        speed_x = self.config.get("speed_x", 4)
        self.x -= speed_x
        if self.x + self.w < 0:
            self.remove = True
            return

        self.y += self.speed_y
