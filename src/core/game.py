from enum import Enum, auto

from core.game_state import GameState
from states import GameStateTitles, GameStateStage, GameStateComplete


class GameStateType(Enum):
    NONE = 0
    TITLES = auto()
    STAGE = auto()
    GAME_COMPLETE = auto()


class Game:
    def __init__(self, app) -> None:
        self.app = app
        self.next_state = None
        self.game_vars = GameState(self)

        self.state = GameStateTitles(self)
        # self.state = GameStateStage(self)
        # self.state = GameStateComplete(self)

    def go_to_titles(self):
        self.next_state = GameStateType.TITLES

    def go_to_new_game(self):
        self.game_vars.new_game()
        self.next_state = GameStateType.STAGE

    def go_to_continue(self):
        self.game_vars.continue_game()
        self.next_state = GameStateType.STAGE

    def go_to_game_complete(self):
        self.next_state = GameStateType.GAME_COMPLETE

    def go_to_next_stage(self):
        if self.game_vars.go_to_next_stage():
            self.next_state = GameStateType.STAGE
        else:
            self.go_to_game_complete()

    def switch_state(self):
        new_state = None
        if self.next_state == GameStateType.TITLES:
            new_state = GameStateTitles
        elif self.next_state == GameStateType.STAGE:
            new_state = GameStateStage
        elif self.next_state == GameStateType.GAME_COMPLETE:
            new_state = GameStateComplete
        else:
            return
        self.state.on_exit()
        self.state = new_state(self)
        self.next_state = None

    def update(self):
        if self.next_state is not None:
            self.switch_state()
        self.state.update()

    def draw(self):
        self.state.draw()
