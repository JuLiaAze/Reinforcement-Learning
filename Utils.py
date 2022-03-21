# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:37:19 2022

@author: julia
"""

from gym import envs
import numpy as np


def select_env():
    choise = -1
    env_possible = []
    
    for name in envs.registry.all():
        if "Cart"in str(name.id):
            env_possible.append(str(name.id))
    
    env_possible.append("Quit")       
    print(np.linspace(0, len(env_possible)-1,len(env_possible)).astype("int8"))
    while int(choise) not in np.linspace(0, len(env_possible)-1,len(env_possible)).astype("int8"):
       print("Select an environement : ")
       for i,element in enumerate(env_possible):
           print("\t",i,")",element)
       choise = input("Enter Choise:")
    
    
    print("you have chosed : ",env_possible[int(choise)])
    return env_possible[int(choise)]

def select_episode():
    
    value = (input("Enter number of episode (Default = 60 000) :"))
    if value == '':
        value = 60000
    return int(value)

def select_learningRATE():
    
    value = (input("Enter learningRATE (Default = 0.1) :"))
    if value == '':
        value = 0.1
    return float(value)

def select_DISCOUNT():
    value = (input("Enter DISCOUNT (Default = 0.95) :"))
    if value == '':
        value = 0.95
    return float(value)
    
def select_epsilon_decay_value():
    
    value =  (input("Enter epsilon_decay_value (Default = 0.99995) :"))
    if value == '':
        value = 0.99995
    return float(value)
