import numpy as np
import random
import pandas as pd
from scipy.stats import norm
from scipy.stats import lognorm

def community(Rft,i):

    BuildingData = pd.read_excel(r'E:\2-Journals\14-DRL\2-Analysis\BuildingData/BuildingData.xlsx')
    nB = BuildingData.shape[0] # Number of buildings
    
    PGA = 0.33
    
    # 1=no-retrofit, 2=GFRP, 3=CFRP, 4=RCJ, 5=SJ
    if Rft == 0:
        DSF = 1 # Damage state factor
        CRF = 0 # Retrofit consequence factor
    elif Rft == 1:
        DSF = 1.6
        CRF = 0.05
    elif Rft == 2:
        DSF = 2.1
        CRF = 0.1
    elif Rft == 3:
        DSF = 2.5
        CRF = 0.2
    elif Rft == 4:
        DSF = 2.7
        CRF = 0.4
    elif Rft == 5:
        DSF = 2.8
        CRF = 0.6
    
    # Determine building types
    if BuildingData.values[i, 3] == 1:
        k = 1
        FA = BuildingData.values[0, 6] # Floor area in ft2
    elif BuildingData.values[i, 3] == 2:
        k = 2
        FA = BuildingData.values[1, 6]
    elif BuildingData.values[i, 3] == 3:
        k = 3
        FA = BuildingData.values[2, 6]
    elif BuildingData.values[i, 3] == 4:
        k = 4
        FA = BuildingData.values[3, 6]
    elif BuildingData.values[i, 3] == 5:
        k = 5
        FA = BuildingData.values[4, 6]
    
    
    iB = np.loadtxt(f"E:\\2-Journals\\14-DRL\\2-Analysis\BuildingData/B{k}.txt") # Loading building data
    
    Rn = np.random.rand()
    
    # Predicting Damage state and repair time of a building
    
    # Loading probability of damage state of a building
    PDS = np.zeros(4)
    PDS[0] = norm.cdf(np.log(PGA), np.log(iB[0, 0] * DSF), iB[0, 1])
    PDS[1] = norm.cdf(np.log(PGA), np.log(iB[1, 0] * DSF), iB[1, 1])
    PDS[2] = norm.cdf(np.log(PGA), np.log(iB[2, 0] * DSF), iB[2, 1])
    PDS[3] = norm.cdf(np.log(PGA), np.log(iB[3, 0] * DSF), iB[3, 1])
    
    # Loading ranges of damage state of a building
    RDS = np.zeros(5)
    RDS[0] = 1 - PDS[0]
    RDS[1] = PDS[0] - PDS[1] + RDS[0]
    RDS[2] = PDS[1] - PDS[2] + RDS[1]
    RDS[3] = PDS[2] - PDS[3] + RDS[2]
    RDS[4] = PDS[3] + RDS[3]
    
    if Rn <= RDS[0]:
        DS = "DS0"
    elif Rn <= RDS[1]:
        DS = "DS1"
    elif Rn <= RDS[2]:
        DS = "DS2"
    elif Rn <= RDS[3]:
        DS = "DS3"
    elif Rn <= RDS[4]:
        DS = "DS4"
    
    
    # Social consequences
    if DS == "DS0":
        level1 = 0
        level2 = 0
        level3 = 0
        level4 = 0
    elif DS == "DS1":
        level1 = 0.05
        level2 = 0
        level3 = 0
        level4 = 0
    elif DS == "DS2":
        if k <= 3:
            level1 = 0.35
            level2 = 0.4
            level3 = 0.001
            level4 = 0.001
        elif k <= 5:
            level1 = 0.2
            level2 = 0.025
            level3 = 0
            level4 = 0
        else:
            level1 = 0.25
            level2 = 0.03
            level3 = 0
            level4 = 0
    elif DS == "DS3":
        if k <= 3:
            level1 = 2
            level2 = 0.2
            level3 = 0.002
            level4 = 0.002
        else:
            level1 = 1
            level2 = 0.1
            level3 = 0.001
            level4 = 0.001
    elif DS == "DS4":
        if np.random.rand() <= 0.15:
            level1 = 40
            level2 = 20
            level3 = 5
            level4 = 10
        elif k <= 3:
            level1 = 10
            level2 = 2
            level3 = 0.02
            level4 = 0.02
        else:
            level1 = 5
            level2 = 1
            level3 = 0.01
            level4 = 0.01

    # Loading data related to damage states
    if DS == "DS0":
        DamSus = 100
        EngMob = 0
        ContMob = 0
        Permit = 0
        BRtime = 0
    elif DS == "DS1":
        DamSus = 75
        EngMob = lognorm.rvs(s=0.4, scale=np.exp(np.log(6 * 7)))
        ContMob = lognorm.rvs(s=0.43, scale=np.exp(np.log(11 * 7)))
        Permit = lognorm.rvs(s=0.86, scale=np.exp(np.log(1 * 7)))
        BRtime = lognorm.rvs(s=iB[0, 3], scale=iB[0, 2])
    elif DS == "DS2":
        DamSus = 50
        EngMob = lognorm.rvs(s=0.4, scale=np.exp(np.log(12 * 7)))
        ContMob = lognorm.rvs(s=0.41, scale=np.exp(np.log(23 * 7)))
        Permit = lognorm.rvs(s=0.32, scale=np.exp(np.log(8 * 7)))
        BRtime = lognorm.rvs(s=iB[1, 3], scale=iB[1, 2])
    elif DS == "DS3":
        DamSus = 25
        EngMob = lognorm.rvs(s=0.4, scale=np.exp(np.log(12 * 7)))
        ContMob = lognorm.rvs(s=0.41, scale=np.exp(np.log(23 * 7)))
        Permit = lognorm.rvs(s=0.32, scale=np.exp(np.log(8 * 7)))
        BRtime = lognorm.rvs(s=iB[2, 3], scale=iB[2, 2])
    elif DS == "DS4":
        DamSus = 0
        EngMob = lognorm.rvs(s=0.32, scale=np.exp(np.log(50 * 7)))
        ContMob = lognorm.rvs(s=0.41, scale=np.exp(np.log(23 * 7)))
        Permit = lognorm.rvs(s=0.32, scale=np.exp(np.log(8 * 7)))
        BRtime = lognorm.rvs(s=iB[3, 3], scale=iB[3, 2])
    
    # Loading Remaining Impeding factors
    Insp = lognorm.rvs(s=0.54, scale=np.exp(np.log(5)))
    Fincg = lognorm.rvs(s=1.11, scale=np.exp(np.log(6 * 7)))
    
    A = [Insp + Fincg, Insp + EngMob + Permit, Insp + ContMob]
    if k <= 8:
        TotalDelay = max(A)
    else:
        TotalDelay = max(A) / 2
    
    
    # Loading total tons of construction
    bricks_total_tons = FA * BuildingData.values[i, 4] / 1000 * np.random.lognormal(mean=np.log(iB[4, 0]), sigma=0.4)
    wood_total_tons = FA * BuildingData.values[i, 4] / 1000 * np.random.lognormal(mean=np.log(iB[4, 1]), sigma=0.4)
    concrete_total_tons = FA * BuildingData.values[i, 4] / 1000 * np.random.lognormal(mean=np.log(iB[4, 2]), sigma=0.4)
    steel_total_tons = FA * BuildingData.values[i, 4] / 1000 * np.random.lognormal(mean=np.log(iB[4, 3]), sigma=0.4)
    
    # Loading total cost of construction in USD
    bricks_total_cost = bricks_total_tons * np.random.uniform(14.71, 21.85)
    wood_total_cost = wood_total_tons * np.random.uniform(200, 500)
    concrete_total_cost = concrete_total_tons * np.random.uniform(15.4, 19.6)
    steel_total_cost = steel_total_tons * np.random.uniform(1012, 1035)
    
    # Loading total Embodied energy in GJ
    bricks_total_EmbEnergy = bricks_total_tons * np.random.uniform(0.9, 4.6)
    wood_total_EmbEnergy = wood_total_tons * np.random.uniform(8.5, 15)
    concrete_total_EmbEnergy = concrete_total_tons * np.random.uniform(0.5, 1.6)
    steel_total_EmbEnergy = steel_total_tons * np.random.uniform(9.9, 35)
    
    # Loading total carbon emissions in Tons kgCO2
    bricks_total_CO2_Em = bricks_total_tons * np.random.uniform(0.2, 0.6)
    wood_total_CO2_Em = wood_total_tons * np.random.uniform(0.75, 1.35)
    concrete_total_CO2_Em = concrete_total_tons * np.random.uniform(0.05, 5.15)
    steel_total_CO2_Em = steel_total_tons * np.random.uniform(1.72, 2.82)
    
    
    
    # Loading consequences (wastage in tons)
    if DS == "DS0":
        bricks_tons = 0
        wood_tons = 0
        concrete_tons = 0
        steel_tons = 0
    elif DS == "DS1":
        bricks_tons = bricks_total_tons * iB[5, 0] / 100
        wood_tons = wood_total_tons * iB[5, 0] / 100
        concrete_tons = concrete_total_tons * iB[6, 0] / 100
        steel_tons = steel_total_tons * iB[6, 0] / 100
    elif DS == "DS2":
        bricks_tons = bricks_total_tons * iB[5, 1] / 100
        wood_tons = wood_total_tons * iB[5, 1] / 100
        concrete_tons = concrete_total_tons * iB[6, 1] / 100
        steel_tons = steel_total_tons * iB[6, 1] / 100
    elif DS == "DS3":
        bricks_tons = bricks_total_tons * iB[5, 2] / 100
        wood_tons = wood_total_tons * iB[5, 2] / 100
        concrete_tons = concrete_total_tons * iB[6, 2] / 100
        steel_tons = steel_total_tons * iB[6, 2] / 100
    elif DS == "DS4":
        bricks_tons = bricks_total_tons * iB[5, 3] / 100
        wood_tons = wood_total_tons * iB[5, 3] / 100
        concrete_tons = concrete_total_tons * iB[6, 3] / 100
        steel_tons = steel_total_tons * iB[6, 3] / 100
    
    
    #Loading consequences
    bricks_GJ = bricks_tons * np.random.uniform(0.9, 4.6)
    wood_GJ = wood_tons * np.random.uniform(8.5, 15)
    concrete_GJ = concrete_tons * np.random.uniform(0.5, 1.6)
    steel_GJ = steel_tons * np.random.uniform(9.9, 35)
    
    bricks_CO2 = bricks_tons * np.random.uniform(0.2, 0.6)
    wood_CO2 = wood_tons * np.random.uniform(0.75, 1.35)
    concrete_CO2 = concrete_tons * np.random.uniform(0.05, 5.15)
    steel_CO2 = steel_tons * np.random.uniform(1.72, 2.82)
    
    bricks_cost = bricks_tons * np.random.uniform(14.71, 21.85)
    wood_cost = wood_tons * np.random.uniform(200, 500)
    concrete_cost = concrete_tons * np.random.uniform(15.4, 19.6)
    steel_cost = steel_tons * np.random.uniform(1012, 1035)

    
    DamSus  # All buildings damage states
    BRtime  # All buildings repair times
    TotalDelay  # All buildings delay times
    
    Total_Social_C = np.round(BuildingData.values[i, 5] * BuildingData.values[i, 4] / 100 * np.random.normal([level1, level2, level3, level4], 0.001))
    
    Total_building_material_tons = [bricks_total_tons, wood_total_tons, concrete_total_tons, steel_total_tons]
    Total_construction_cost_USD = [bricks_total_cost, wood_total_cost, concrete_total_cost, steel_total_cost]
    Total_construction_time_days = np.random.lognormal(np.log(iB[3,2]), iB[3,3])
    Total_construction_EmbEnergy_GJ = [bricks_total_EmbEnergy, wood_total_EmbEnergy, concrete_total_EmbEnergy, steel_total_EmbEnergy]
    Total_construction_TonskgCO2 = [bricks_total_CO2_Em, wood_total_CO2_Em, concrete_total_CO2_Em, steel_total_CO2_Em]
    
    Damaged_building_material_tons = [bricks_tons, wood_tons, concrete_tons, steel_tons]
    Damaged_construction_cost_USD = [bricks_cost, wood_cost, concrete_cost, steel_cost]
    Damaged_repair_time_days = [TotalDelay, BRtime]
    Damaged_construction_EmbEnergy_GJ = [bricks_GJ, wood_GJ, concrete_GJ, steel_GJ]
    Damaged_construction_TonskgCO2_Em = [bricks_CO2, wood_CO2, concrete_CO2, steel_CO2]

    
    Retrofit_cost_USD = CRF * sum(Total_construction_cost_USD)
    
    Risk1 = sum(Total_Social_C)
    Risk2 = sum(Damaged_construction_cost_USD)
    Resilience = sum(Damaged_repair_time_days)
    Sustainability1 = sum(Damaged_construction_TonskgCO2_Em)
    Sustainability2 = sum(Damaged_construction_EmbEnergy_GJ)
    
    
    Rew1=Risk1/(BuildingData.values[i, 5] * BuildingData.values[i, 4])
    Rew2=Risk2/sum(Total_construction_cost_USD)
    Rew3=Resilience/(Total_construction_time_days+TotalDelay)
    Rew4=Sustainability1/sum(Total_construction_TonskgCO2)
    Rew5=Sustainability2/sum(Total_construction_EmbEnergy_GJ)
    
    Reward=1-((0.2*CRF)+(0.2*Rew1)+(0.2*Rew2)+(0.2*Rew3)+(0.1*Rew4)+(0.1*Rew5))
        

    return Reward, DS, Retrofit_cost_USD, Risk1, Risk2, Resilience, Sustainability1, Sustainability2
