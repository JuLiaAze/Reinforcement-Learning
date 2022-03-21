# -*- coding: utf-8 -*-



#%% Imports 

from Class_and_methode import *
#%% Main

if __name__ == "__main__":
    
    name_env = select_env()
    ## 1) 
    if name_env != "Quit":
        nb_episode = select_episode()
        
        R1 = Rn(name_env,nb_episode,select_learningRATE(),select_DISCOUNT(),select_epsilon_decay_value())
        
        while( R1.episode < R1.EPISODES + 1): #go through the episodes
            R1.initialisation_donnees()
            R1.periode_affichage_episode()
            while not R1.done: 
        
                R1.set_action()
                R1.new_state,R1.reward, R1.done, _ = R1.env.step(R1.action) #step action to get new states, reward, and the "done" status.
                R1.episode_reward += R1.reward #add the reward
                R1.get_discrete_state()
        
                if R1.episode % 2000 == 0: #render
                    R1.env.render()
        
                if not R1.done: #update q-table
        
                    R1.update_q_table()
        
                R1.discrete_state = R1.new_discrete_state
            if R1.epsilon > 0.05: #epsilon modification
                R1.epsilon_modification()
    
        
            R1.get_time()
            R1.update_reward()
            R1.average_time_and_reward()
            R1.episode+=1
        R1.close_env()
