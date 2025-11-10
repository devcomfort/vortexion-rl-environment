import math
import pyxel as px

from entities.enemy import Enemy


class EnemyB(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y, "enemy_b")

    def update(self):
        super().update()  # hit frames

        speed = self.config.get("speed", 1.5)
        self.x -= speed
        if self.x + self.w < 0:
            self.remove = True
            return

        self.y += px.sin(self.lifetime * math.pi)

        if self.lifetime == 20:
            bullet_speed = self.config.get("bullet_speed", 2)
            self.shoot_at_player(bullet_speed)
