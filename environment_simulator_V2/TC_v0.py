from gym.spaces import Box, Discrete, Dict
from scipy.ndimage import rotate
import matplotlib.pyplot as plt
from gym import Env
import numpy as np
import random
import math

class TC_environment(Env):
    def __init__(self):
        self.posX_limits = (0, 400)
        self.posY_limits = (0, 640)
        self.vel_limits =  (  1,  5)
        self.max_tor = 100
        self.car_init_pos = 3
        self.init_pos, self.init_vel = (0,0), 0
        self.path = []
        self.thetas = []
        self.observations = 4
        self.action_space = Box(low=0, high=self.max_tor, dtype=np.float32) # continous torque action [tao]
        self.observation_space = Dict({"position": Box(low=np.array([self.posX_limits[0], self.posY_limits[0]], dtype=np.float32),
                                                      high=np.array([self.posX_limits[1], self.posY_limits[1]], dtype=np.float32),
                                                     shape=(2,), dtype=np.float32),
                                       "velocity": Box(low=np.array([self.vel_limits[0]], dtype=np.float32), 
                                                      high=np.array([self.vel_limits[1]], dtype=np.float32), 
                                                    dtype=np.float32)})

    def reset(self):
        init_observation = self.observation_space.sample()
        self.init_pos = tuple(init_observation["position"])
        self.init_vel = tuple(init_observation["velocity"])
        return init_observation

    def path_generator(self, ptype ="random", step_size = 5):
        self.path = []
        self.thetas = []
        self.path.append(self.init_pos)