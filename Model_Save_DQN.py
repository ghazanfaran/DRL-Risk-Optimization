import os
import numpy as np
import random

import gym 
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete 

from stable_baselines3 import DQN, A2C, DDPG, PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.monitor import Monitor

import Environment as En

#Making directories
models_dir="models/DQN"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
if not os.path.exists(logdir):
    os.makedirs(logdir)
    
#Load Environment
env = En.environment()
eval_env = Monitor(env)

#Model
model = DQN('MlpPolicy', eval_env, verbose=1, tensorboard_log=logdir)

#Model learn
TIMESTEPS=1000

for i in range(1,10000):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="DQN")
    model.save(f"{models_dir}/{TIMESTEPS*i}")


#tensorboard --logdir=logs