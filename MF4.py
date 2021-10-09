# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:04:33 2021

@author: home
"""

import requests
import json
import pandas as pd

master_df = pd.DataFrame(columns=['Fund_House','Scheme_Type'
                                           ,'Scheme_Category','Scheme_Code'
                                           ,'Scheme_Name','Date'
                                           ,'NAV'])

master_list=[]
    
    


baseurl = "https://api.mfapi.in/mf/"

list_mf = open("mf_list_145001_150000.csv","r")

for mf in list_mf:
#mf="100028"

    url = baseurl+mf
    print(url)
    
    #response = requests.get("https://api.mfapi.in/mf/100028")
    response = requests.get(url)
    
    print("Downloaded" + url)
    
    
    
    dmp=json.dumps(response.json())
   
    
    mf_dict=json.loads(dmp)
    
      
       
    
    
    current_row=[]
    for data in mf_dict['data']:
        current_row=[list(mf_dict['meta'].values())[0]
                     ,list(mf_dict['meta'].values())[1]
                     ,list(mf_dict['meta'].values())[2]
                     ,list(mf_dict['meta'].values())[3]
                     ,list(mf_dict['meta'].values())[4]
                     ,data['date']
                     ,data['nav']
                     ]
        master_list.append(current_row)
        
                     
    print("Data Frame Append Over")
    #print(mf)  
    
master_df = pd.DataFrame(master_list,columns=['Fund_House','Scheme_Type'
                                           ,'Scheme_Category','Scheme_Code'
                                           ,'Scheme_Name','Date'
                                           ,'NAV'])
    
master_df.to_csv('df_list_145001_150000.csv',index=False)


        
    
   