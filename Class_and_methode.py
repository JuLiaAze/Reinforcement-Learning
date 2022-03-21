# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:20:25 2022

@author: julia
"""

#%% Class
from all_Imports import *

class Rn(): 
    def __init__(self,name,nb_episode,learningRATE,DISCOUNT,epsilon_decay):
        self.env = gym.make(name)
        print(self.env.action_space.n)
        
        #designate the variables needed
        #float variables
        self.LEARNING_RATE , self.DISCOUNT ,self.epsilon_decay_value= learningRATE,DISCOUNT,epsilon_decay
        #Int variables
        self.epsilon ,self.EPISODES= 1 , nb_episode 
        #Null variable
        self.total_reward =self.prior_reward= self.episode =self.total = self.discrete_state =self.done = self.episode_reward = 0
        self.t0 = time.time()#set the initial time
        self.Observation = [30, 30, 50, 50]
        self.np_array_win_size = np.array([0.25, 0.25, 0.01, 0.1])
        self.new_state = None
        
        #Q-Table
        self.q_table = np.random.uniform(low=0, high=1, size=(self.Observation + [self.env.action_space.n]))
        print(self.q_table.shape)

    #method to get the discrete state

    def get_discrete_state(self,reset = False,discret = False):
        if reset:
            self.new_state = self.env.reset()
        if discret:
            self.discrete_state = tuple((self.new_state/self.np_array_win_size+ np.array([15,10,1,10])).astype(np.int))
        else:
            self.new_discrete_state = tuple((self.new_state/self.np_array_win_size+ np.array([15,10,1,10])).astype(np.int))

    def initialisation_donnees(self): 
        self.get_discrete_state(True,True) #get the discrete start for the restarted environment 
        self.done=  False
    
    def periode_affichage_episode(self):
        if self.episode % 2000 == 0: 
            print("Episode: " + str(self.episode))
    
    def set_action(self):
        if np.random.random() > self.epsilon:
            self.action = np.argmax(self.q_table[self.discrete_state]) #take cordinated action
        else:
            self.action = np.random.randint(0, self.env.action_space.n) #do a random action
    
    def update_q_table(self):
        max_future_q = np.max(self.q_table[self.new_discrete_state])
        current_q = self.q_table[self.discrete_state + (self.action,)]
        new_q = (1 - self.LEARNING_RATE) * current_q + self.LEARNING_RATE * (self.reward + self.DISCOUNT * max_future_q)
        self.q_table[self.discrete_state + (self.action,)] = new_q
    
    def epsilon_modification(self):
        if self.episode_reward > self.prior_reward and self.episode > 10000:
            self.epsilon = math.pow(self.epsilon_decay_value, self.episode - 10000)
            if self.episode % 500 == 0:
                print("Epsilon: " + str(self.epsilon))
    
    def get_time(self):
        self.total = self.total + time.time() - self.t0 #episode total time
    
    def update_reward(self):
        self.total_reward += self.episode_reward #episode total reward
        self.prior_reward = self.episode_reward
    
    def average_time_and_reward(self):
        if self.episode % 1000 == 0: #every 1000 episodes print the average time and the average reward
            mean = self.total / 1000
            print("average time =",mean," the average reward")
    def close_env(self):
        self.env.close()