''' All game constants are defined here '''

from enum import Enum
import sys

class GameMode(Enum):
    '''
    Defines two game mode formats:
    1. Solve maximum puzzles in constant time
    2. Minimum time taken to solve constant puzzles
    '''
    SOLVE_MAXIMUM_PUZZLES = 'puzzle'
    MINIMUM_TIME_TAKEN = 'time'


GAME_MODE = GameMode.MINIMUM_TIME_TAKEN

SUPPORTED_LANGS = {
    'Python': '.py',
    'Java': '.java',
    'C': '.c'
}
PUZZLES_DIR = sys.path[0] + '/Puzzles/'
ENV_LOCATION = sys.path[0] + '/.env'

GAME_DURATION = 120 # in seconds, for game mode `time`
MAX_PUZZLES = 3 # For game mode `puzzle`
