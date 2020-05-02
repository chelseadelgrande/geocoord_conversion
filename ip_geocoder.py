import pandas as pd
import requests
import csv
import random
import ipinfo, pprint

access_token = '217ab4bc91b10e'
handler = ipinfo.getHandler(access_token)
covid_data = pd.read_csv('full_file_here')
covid_arr = covid_data['IP_address'].values
csv_columns =['city', 'country', 'country_name', 'ip', 'latitude', 'loc', 'longitude', 'org', 'postal', 'region', 'timezone']
#api only allows 100 pull requests at a time
arr_list = handler.getBatchDetails(covid_arr[0:99])

df = pd.DataFrame(arr_list)

#transpose the data to get the headers on top
df_transposed = df.T
#output in append mode
df_transposed.to_csv('newoutput_path_here', mode = 'a')
print ("complete")

