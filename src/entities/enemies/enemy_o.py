from entities.enemy import Enemy
from entity_config import get

SPEED = get("enemy_o", "speed", 2.5)
BULLET_SPEED = get("enemy_o", "bullet_speed", 2)
SHOT_DELAY = get("enemy_o", "shot_delay", 120)
INITIAL_SHOT_DELAY = get("enemy_o", "initial_shot_delay", 40)


class EnemyO(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 7  # cyan
        self.u = 224
        self.v = 80

        self.hp = 1

        self.shot_delay = INITIAL_SHOT_DELAY  # allow time to get on screen

    def update(self):
        super().update()  # hit frames

        self.x -= SPEED
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY
            self.shoot_at_player(BULLET_SPEED)
        else:
            self.shot_delay -= 1
