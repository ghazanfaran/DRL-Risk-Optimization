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



#Random episodes

# episodes = 10
# for episode in range(1, episodes+1):
#     state=env.reset()
#     done = False
#     score = 0 
    
#     while not done:
#         action = env.action_space.sample()
#         n_state, reward, done, info = env.step(action)
#         score+=reward
#     print('Episode:{} Score:{}'.format(episode, score))

#Learned episodes

episodes = 5
action_all = np.zeros((474, episodes))
for episode in range(1, episodes+1):
    state=env.reset()
    obs = env.reset()
    done = False
    score = 0    
    i=0
    
    while not done:
        obs = np.array([obs])  # Convert obs to a NumPy array
        action, _ = model.predict(obs.reshape(1, -1))
        obs, reward, done, info = env.step(action[0])
        action_all[i, episode-1] = action
        score += reward
        i+=1
        print(action, end=' ')
    print('Episode:{} Score:{}'.format(episode, score))

np.savetxt("action_all.txt", action_all, delimiter=",", fmt="%d")

