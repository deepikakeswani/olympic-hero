# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data = data.rename(columns={"Total":"Total_Medals"})
print(data.head(10))


# --------------
#Code starts here
print(data.columns)
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter')


data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
print(data.head(10))
better = data['Better_Event'].value_counts()
print(better)
if better['Summer'] > better['Winter']:
    better_event = 'Summer'
else:
    better_event = 'Winter'
print('Better event was',better_event)



# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
print(top_countries.head(3))
print(top_countries.shape)
top_countries = top_countries[:-1]
print(top_countries.shape)
def top_ten(top_countries,column_name):
    top = top_countries.nlargest(10,column_name)
    country_list = list(top['Country_Name'])
    return country_list
top_10_summer = top_ten(top_countries,"Total_Summer")
print(top_10_summer)
top_10_winter = top_ten(top_countries,"Total_Winter")
print(top_10_winter)
top_10 = top_ten(top_countries,"Total_Medals")
print(top_10)
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print("Commom countries",common)




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
fig, [ax1, ax2, ax3] = plt.subplots(nrows=3,ncols=1,figsize=(25, 20))
ax1.bar(summer_df['Country_Name'],summer_df['Total_Summer'],width = 0.8)
ax1.set_title('Top Summer', fontdict={'fontsize': 8, 'fontweight': 'medium'})
ax2.bar(winter_df['Country_Name'],winter_df['Total_Winter'],width = 0.8)
ax2.set_title('Top Winter', fontdict={'fontsize': 8, 'fontweight': 'medium'})
ax3.bar(top_df['Country_Name'],top_df['Total_Medals'],width = 0.8)
ax3.set_title('Overall Top', fontdict={'fontsize': 8, 'fontweight': 'medium'})


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)
#winter_df['Country_Name'] = summer_df['Country_Name']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)
#print(type(winter_country_gold))
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)


# --------------
#Code starts here
#print(data.tail(4))
data_1 = data[1:-1]
#print(data_1.tail(4))


data_1['Total_Points'] = (3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + data_1['Bronze_Total']
print(data_1.head(10))
most_points = max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print("Best Country is",best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
cols = ['Gold_Total','Silver_Total','Bronze_Total']
best = best[cols]
print(best.columns)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


