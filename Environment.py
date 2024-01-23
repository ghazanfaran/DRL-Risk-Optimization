import os
import numpy as np
import random

import gym 
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete 

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.monitor import Monitor

import Community as Co

class environment(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(6)
        # Temperature array
        self.observation_space = Box(low=np.array([0]), high=np.array([20000000]), shape=(1,))
        # Set start temp
        #self.state = 0
        # Total buildings
        #self.buildings = 474
        # Buildings count
        #self.building_count=0
        
    def step(self, action):
        #Extracting risk, resilience, and sustainability results
        reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = Co.community(action,self.building_count) 
        
        self.state += Cost
        # Reduce shower length by 1 second
        self.buildings -= 1
        self.building_count+=1
        
        # Check if shower is done
        if self.buildings <= 0: 
            done = True
        else:
            done = False
        
        # Apply temperature noise
        #self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        # Return step information
        return self.state, reward, done, info
        #return self.state, done, info, reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd

    def render(self):
        # Implement viz
        pass
    
    def reset(self):
        # Reset shower temperature
        self.state = 0
        # Reset shower time
        self.buildings = 474 
        self.building_count=0
        return self.state
