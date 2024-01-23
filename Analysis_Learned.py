import random
import numpy as np
import Community as Co


count_DS0_sum = []
count_DS1_sum = []
count_DS2_sum = []
count_DS3_sum = []
count_DS4_sum = []


reward_sum = []

Rft_sum = []

Casualty_sum = []
Cost_sum = []
Resilce_sum = []
CarbnEm_sum = []
Enbbd_sum = []

episodes=300

for episode in range(0, episodes):
    
    reward_all = []
    DS_all = []
    Rft_all = []
    Casualty_all = []
    Cost_all = []
    Resilce_all = []
    CarbnEm_all = []
    Enbbd_all = []
    
    for i in range(0,474):
        
        Rft=0
        #Rft=random.randint(0, 5)
        #Rft=np.loadtxt("action_all.txt", delimiter=",")
        
        reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = Co.community(Rft,i)
        print('Episode:{} reward:{} buildings:{}'.format(episode, reward, i))
        
        reward_all.append(reward)
        DS_all.append(DS)
        Rft_all.append(Rft_Cost)
        Casualty_all.append(Casualty)
        Cost_all.append(Cost)
        Resilce_all.append(Resilce)
        CarbnEm_all.append(CarbnEm)
        Enbbd_all.append(Enbbd)    
        
        

    count_DS0 = DS_all.count("DS0")
    count_DS1 = DS_all.count("DS1")
    count_DS2 = DS_all.count("DS2")
    count_DS3 = DS_all.count("DS3")
    count_DS4 = DS_all.count("DS4")
    
    
    
    reward_sum.append(np.sum(reward_all))
    
    count_DS0_sum.append(count_DS0)
    count_DS1_sum.append(count_DS1)
    count_DS2_sum.append(count_DS2)
    count_DS3_sum.append(count_DS3)
    count_DS4_sum.append(count_DS4)
    
    Rft_sum.append(np.sum(Rft_all))
    
    Casualty_sum.append(np.sum(Casualty_all))
    Cost_sum.append(np.sum(Cost_all))
    Resilce_sum.append(np.sum(Resilce_all))
    CarbnEm_sum.append(np.sum(CarbnEm_all))
    Enbbd_sum.append(np.sum(Enbbd_all))



# Convert the lists to numpy arrays
data = np.column_stack((reward_sum, count_DS0_sum, count_DS1_sum, count_DS2_sum, count_DS3_sum, count_DS4_sum, Rft_sum, Casualty_sum, Cost_sum, Resilce_sum, CarbnEm_sum, Enbbd_sum))

# Save the data as columns in a text file
np.savetxt('Episodes.txt', data, delimiter='\t', header='reward\tDS0\tDS1\tDS2\tDS3\t_DS4\tRft\tCasualty\tCost\tResilce\tCarbnEm\tEnbbd', fmt='%s')
