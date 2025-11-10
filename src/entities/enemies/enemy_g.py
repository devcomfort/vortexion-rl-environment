from entities.enemy import Enemy
from entity_config import get

SPEED_Y = get("enemy_g", "speed_y", 1.5)
SPEED_X_OFFSET = get("enemy_g", "speed_x_offset", 0.5)


class EnemyG(Enemy):
    def __init__(self, state, x, y) -> None:
        super().__init__(state, x, y)
        self.colour = 9  # pink
        self.u = 96
        self.v = 80

        self.speed = -state.get_scroll_x_speed()

    def update(self):
        super().update()  # hit frames

        if self.lifetime < 250:
            self.speed = -(self.game_state.get_scroll_x_speed() + SPEED_X_OFFSET)
        else:
            self.flip_x = True
            self.speed = self.game_state.get_scroll_x_speed() + SPEED_X_OFFSET

        if self.lifetime >= 250 and self.lifetime < 280:
            if self.y < 96:
                self.y += SPEED_Y
            else:
                self.y -= SPEED_Y

        self.x += self.speed
        if self.lifetime > 300 and self.x > 255:
            self.remove = True
            return
