import random
import numpy as np
import Community as Co
import geopandas as gpd
import matplotlib.pyplot as plt

shapefile_path = r'E:\2-Journals\14-DRL\2-Analysis\GISMap\Buildings.shp'
gdf = gpd.read_file(shapefile_path)


DS_all = []
Rft_all = []
Casualty_all = []
Cost_all = []
Resilce_all = []
CarbnEm_all = []
Enbbd_all = []

episode=1



for i in range(0,474):
    
    Rft=0
    #Rft=random.randint(0, 5)
    #Rft=np.loadtxt("action_all.txt", delimiter=",")
    
    #reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = Co.community(Rft[i,episode],i)
    reward, DS, Rft_Cost, Casualty, Cost, Resilce, CarbnEm, Enbbd = Co.community(Rft,i)
    print(i)
    
    gdf.loc[i, 'DS'] = DS
    gdf.loc[i, 'Retrofit'] = Rft_Cost
    gdf.loc[i, 'Risk1'] = Casualty
    gdf.loc[i, 'Risk2'] = Cost
    gdf.loc[i, 'Resilience'] = Resilce
    gdf.loc[i, 'Sus1'] = CarbnEm
    gdf.loc[i, 'Sus2'] = Enbbd

    DS_all.append(DS)
    Rft_all.append(Rft_Cost)
    Casualty_all.append(Casualty)
    Cost_all.append(Cost)
    Resilce_all.append(Resilce)
    CarbnEm_all.append(CarbnEm)
    Enbbd_all.append(Enbbd)

# Create a figure and axis for customization
fig, ax = plt.subplots(figsize=(12, 12))

# Customize the plot #CHANGE column, vmin, vmax
gdf.plot(ax=ax, column='DS', cmap='coolwarm', categorical=False, legend=True, markersize=1)
#gdf.plot(ax=ax, column='Risk1', cmap='Greys', vmin=0, vmax=1, categorical=False, legend=True, markersize=1)
#gdf.plot(ax=ax, column='Risk2', cmap='Purples', vmin=0, vmax=50000, categorical=False, legend=True, markersize=1)
#gdf.plot(ax=ax, column='Resilience', cmap='Greens', vmin=0, vmax=1000, categorical=False, legend=True, markersize=1)
#gdf.plot(ax=ax, column='Sus1', cmap='Oranges', vmin=0, vmax=2000, categorical=False, legend=True, markersize=1)
#gdf.plot(ax=ax, column='Retrofit', cmap='Oranges', vmin=0, vmax=10000, categorical=False, legend=True, markersize=1)

# Save the plot to a file
output_path = r'E:\2-Journals\14-DRL\2-Analysis\ResultMaps2\DS2.svg'
plt.savefig(output_path, dpi=600)

# Show the plot
plt.show()



















#Combine the values from the lists into one combined list
combined_list = []
for ds, rft, casualty, cost, resilce, carbnem, enbbd in zip(DS_all, Rft_all, Casualty_all, Cost_all, Resilce_all, CarbnEm_all, Enbbd_all):
      combined_list.append((ds, rft, casualty, cost, resilce, carbnem, enbbd))

# Specify the file path to save the data
output_file = 'Cons.txt'

# Open the file in write mode
with open(output_file, 'w') as f:
      # Write the combined list to the file
      for item in combined_list:
          f.write(','.join(str(value) for value in item) + '\n')

