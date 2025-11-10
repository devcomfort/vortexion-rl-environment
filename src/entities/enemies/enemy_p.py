from entities.enemy import Enemy
from entity_config import get

SPEED = get("enemy_p", "speed", 2.5)
BULLET_SPEED = get("enemy_p", "bullet_speed", 4)
SHOT_DELAY = get("enemy_p", "shot_delay", 120)
INITIAL_SHOT_DELAY = get("enemy_p", "initial_shot_delay", 25)


class EnemyP(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 9  # pink
        self.u = 240
        self.v = 80

        self.shot_delay = INITIAL_SHOT_DELAY  # allow time to get on screen

    def update(self):
        super().update()  # hit frames

        self.x -= SPEED
        if self.x + self.w < 0:
            self.remove = True
            return

        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY
            self.shoot_at_angle(BULLET_SPEED, 190)
            self.shoot_at_angle(BULLET_SPEED, 170)
        else:
            self.shot_delay -= 1
