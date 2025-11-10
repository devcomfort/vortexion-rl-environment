from entities.enemy import Enemy
from entity_config import get

SPEED_X = get("enemy_h", "speed_x", 1.5)
BOUNCE_VEL = get("enemy_h", "bounce_vel", 5)
GRAVITY = get("enemy_h", "gravity", 0.2)


class EnemyH(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 6  # red
        self.u = 112
        self.v = 80

        self.hp = 4

        self.vel_y = BOUNCE_VEL

    def update(self):
        super().update()  # hit frames

        self.x -= SPEED_X

        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y >= 136:
            self.y = 136
            self.vel_y = -BOUNCE_VEL

        if self.x + self.w < 0:
            self.remove = True
            return
