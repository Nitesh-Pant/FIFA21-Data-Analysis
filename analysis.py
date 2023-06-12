import pandas as pd
import numpy as np
from datetime import date
import re

df = pd.read_csv('/home/niteshpant/Desktop/fifaAnalysis/fifa21_raw_data.csv')

def convertLBStoKG(weight):
    for idx, w in weight.iteritems():
        df.loc[idx, 'Weight(KG)'] = int(w) * (0.453592)
    
    #print(df[['Weight', 'Height', 'Weight(KG)']].head(10))
    return df['Weight(KG)'] 

#print(df.head())
#print(df.info())
#print(df.isnull().sum())
#print(df.columns)

'''
    Convert lbs weight to kg and create new column
'''
'''
    #print(df[['Height', 'Weight']].head(10))
    newDf = df.dropna(subset=['Weight'])
    weightInKG = newDf['Weight'].str.replace('lbs', '')
    df['Weight(KG)'] = convertLBStoKG(weightInKG)
    #print(df.head(10))

'''

'''
    Convert Height column from inches to cm
'''
'''
    df['Height'] = df['Height'].str.replace('"', '')
    df['Height'] = df['Height'].str.replace("'", ".")
    df['Height'] = df['Height'].astype(float) * 30.48
print(df['Height'].head(10))
'''

'''
    Convert Joined column to day, month and year columns
'''
'''
    #print(df['Joined'].head(10))

    df['Joined'] = pd.to_datetime(df['Joined'])     #convert df['Joined'] (object) to datetime data type
    #print(df['Joined'].dtype)
    #print(df['Joined'].dt.month.head(10))          # get month number
    #print(df['Joined'].dt.month_name().head(10))   # get month name
    #print(df['Joined'].dt.day.head(10))             # get day number 
    #print(df['Joined'].dt.day_name().head(10))      # get day name (mom, tue...)
    #print(df['Joined'].dt.year.head(10))            # get year number

    df['Joined Year'] = df['Joined'].dt.year
    df['Joined Month'] = df['Joined'].dt.month_name()
    df['Joined Day'] = df['Joined'].dt.day_name()

    print(df[['Joined', 'Joined Year', 'Joined Month', 'Joined Day']].head(10))
'''

df['Hits'] = df['Hits'].str.replace("\n", "")
#df['Hits'] = df['Hits'].str.strip()
#df['Hits'] = df['Hits'].astype('float')
#print(df['Hits'].head())
#print(df['Hits'].describe)

'''
    Player playing for current club more than 10 years
'''
'''
    df['Joined'] = pd.to_datetime(df['Joined'])
    df['Joined'] = df['Joined'].dt.date         # removed time from date
    #print(df['Joined'].head())) 

    days_in_year = 365.2425
    for idx, join in df['Joined'].iteritems():
        if(int((date.today() - join).days / days_in_year) >= 10):
            df.loc[idx, 'Ten_Years'] = True
        else:
            df.loc[idx, 'Ten_Years'] = False

    print(df[['Joined', 'Ten_Years']].head(10))
'''

'''
    Convert wage, value, Relase clause from string to int (M =million)
'''
print(df[['Wage', 'Value', 'Release Clause']].head(20))
df['Complete_Wage'] = df['Wage'].str.replace('K', '000')

#print(df['Complete_Wage'].head(20))
df['Complete_Value'] = df['Value'].str.replace('M', '')
df['Complete_Value'] = df['Complete_Value'] * 1000000
print(df['Complete_Value'].head(20))