import pandas as pd

df = pd.read_json("./rckrdataset.json")

ls=[]
for i in range(len(df)):
    temp=[]
    for j in df['currencies'].iloc[i]:
        temp.append(j['code'])
    ls.append(temp)
temp_dict={}
for i in ls:
    for j in i:
        temp_dict[j]=temp_dict.get(j,0)+1
unique_code=[]
for k,v in temp_dict.items():
    if (v==1):
        unique_code.append(k)
rdf=pd.DataFrame()
rdf['cur_codes']=ls
rdf['name']=df['name']
rdf['latlng']=df['latlng']
rdf['population']=df['population']


limit=84497
first_20 = {}
        
for i in range(len(rdf)):
    if(rdf['population'].iloc[i]>=limit):
        for j  in rdf['cur_codes'].iloc[i]:
            if(j in unique_code  ):
                first_20[rdf['name'].iloc[i]]=[]
                first_20[rdf['name'].iloc[i]].append(rdf['latlng'].iloc[i])
                first_20[rdf['name'].iloc[i]].append(rdf['population'].iloc[i])
first_20=dict(sorted(first_20.items(),key=lambda x:x[1][1])[:20])
print(first_20)
# print(final)
# print(rdf[rdf['cur_codes']=='INR'])
# final=rdf.groupby('cur_codes').filter(lambda x: len(x)==1)
# final_final=(final.sort_values(by=['population'],ascending=True)[final['population']>=61954].head(20))
# print(final_final)
# latlnglist=(final_final['latlng'].tolist())
# print((latlnglist))
# cur_list=list((rdf['cur_codes'].value_counts()==1))
# print(cur_list)
# print(len(cur_list))
# print( rdf['cur_codes'].isin(cur_list))
# # df[df['cur_codes'].isin(df['cur_codes'].value_counts()[df['cur_codes'].value_counts()==1].index)]
from math import radians, cos, sin, asin, sqrt,pi
def find_dist(latlng_1, latlng_2):
    lat1, lon1 = radians(latlng_1[0][0]), radians(latlng_1[0][1])
    lat2, lon2 =  radians(latlng_2[0][0]), radians(latlng_2[0][1])
    d = 2*6371*asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2))
    
    return round(d,2)
     

total_dist = 0

keys = list(first_20.keys())
N=len(keys)
for i in range(N):
    for j in range(i+1,N):
        total_dist += find_dist(first_20[keys[i]], first_20[keys[j]])
total_dist = round(total_dist, 2)
print(total_dist)
# # name,cur_code,population,latlong
