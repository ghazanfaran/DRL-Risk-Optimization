import numpy as np
from stable_baselines3 import A2C

import Environment as En

env = En.environment()
env.reset()

#Making directories
models_dir="models/A2C"
model_path =f"{models_dir}/150000"

#Model
model = A2C.load(model_path, env=env)

action_all = []
DS_all = []
Rft_all = []
Casualty_all = []
Cost_all = []
Resilce_all = []
CarbnEm_all = []
Enbbd_all = []

#Learned episodes

episodes = 10
for episode in range(1, episodes+1):
    state=env.reset()
    obs = env.reset()
    done = False
    score = 0    
    
    while not done:
        obs = np.array([obs])  # Convert obs to a NumPy array
        action, _ = model.predict(obs.reshape(1, -1))
        n_state, done, info, reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = env.step(action[0])
        
        action_all.append(action)
        DS_all.append(DS)
        Rft_all.append(Rft_Cost)
        Casualty_all.append(Casualty)
        Cost_all.append(Cost)
        Resilce_all.append(Resilce)
        CarbnEm_all.append(CarbnEm)
        Enbbd_all.append(Enbbd)
        
        score += reward
        print(action, end=' ')
    
    #Combine the values from the lists into one combined list
    combined_list = []
    for action, ds, rft, casualty, cost, resilce, carbnem, enbbd in zip(action_all, DS_all, Rft_all, Casualty_all, Cost_all, Resilce_all, CarbnEm_all, Enbbd_all):
          combined_list.append((action, ds, rft, casualty, cost, resilce, carbnem, enbbd))

    # Specify the file path to save the data
    output_file = (f"{episode}Cons_Learned.txt")
    
    # Open the file in write mode
    with open(output_file, 'w') as f:
          # Write the combined list to the file
          for item in combined_list:
              f.write(','.join(str(value) for value in item) + '\n')
    
    
        
    print('Episode:{} Score:{}'.format(episode, score))
















# #Random episodes

# episodes = 10
# for episode in range(1, episodes+1):
#     state=env.reset()
#     done = False
#     score = 0 
    
#     while not done:
#         action = env.action_space.sample()
#         n_state, reward, done, info, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = env.step(action)
#         score+=reward
#     print('Episode:{} Score:{}'.format(episode, score))