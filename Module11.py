##Converting excel file to CSV and also printing one column from the excel file in python

import pandas as pd

read_file = pd.read_excel (r'C:\Users\Owner PC\AppData\Local\Programs\Python\Python39\COVID19_03242020_ByCounty.xls')
read_file.to_csv (r'C:\Users\Owner PC\AppData\Local\Programs\Python\Python39\NEW_COVID19_03242020_ByCountyv3.csv', index = None, header=True)


data = pd.read_excel (r'C:\Users\Owner PC\AppData\Local\Programs\Python\Python39\COVID19_03242020_ByCounty.xls') 
df = pd.DataFrame(data, columns= ['COUNTYNAME'])
print (df)


