from gymnasium.envs.registration import register
from underwater_env.classes.UnderwaterEnv import UnderwaterEnv

register(
    id='underwater_env/Underwater-v0',
    entry_point='underwater_env.classes.UnderwaterEnv:UnderwaterEnv',
)