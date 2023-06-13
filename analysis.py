# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import date
import re
df = pd.read_csv('/home/niteshpant/Desktop/fifaAnalysis/fifa21_raw_data.csv')

#print(df.head())
#print(df.info())
#print(df.isnull().sum())
#print(df.columns)

#print(df['Hits'].unique())

'''
    Convert lbs weight to kg and create new column
'''
'''
    def convertLBStoKG(weight):
        for idx, w in weight.iteritems():
            df.loc[idx, 'Weight(KG)'] = int(w) * (0.453592)
        
        #print(df[['Weight', 'Height', 'Weight(KG)']].head(10))
        return df['Weight(KG)'] 
        
    print(df['Weight'].unique())
    newDf = df.dropna(subset=['Weight'])
    weightInKG = newDf['Weight'].str.replace('lbs', '')
    df['Weight(KG)'] = convertLBStoKG(weightInKG)
    print(df.head(10))
'''

'''
    Convert Height column from inches to cm
'''
'''
    print(df['Height'].unique())
    df['Height'] = df['Height'].str.replace('"', '').str.replace("'", '.')
    df['Height'] = (df['Height'].astype(float) * 30.48).round(2)
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

'''
    Remove new line character from Hits column and 1.5K to 1500
'''
'''
    def convertKtoThousand(Hits):
        if 'K' in Hits:
            Hits = Hits.replace('K', '')
            Hits = float(Hits) * 1000
            return int(Hits)
        else:
            return Hits

    df['Hits'] = df['Hits'].astype(str)
    df['Hits'] = df['Hits'].str.lstrip("\n")
    df['Hits'] = df['Hits'].apply(convertKtoThousand)
    #print(df['Hits'].head(10))
    print(df['Hits'].unique())
'''

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
'''
    def convertWage(wage):
        wage = wage.replace('K', '')
        wage = wage.lstrip("€")
        wage = float(wage) * 1000
        return wage

    print(df[['Wage', 'Value', 'Release Clause']].head(20))
    print(df['Wage'].unique())
    df['Complete_Wage'] = df['Wage'].apply(convertWage)
    print(df['Complete_Wage'].head(100))


    def convertValue(val):
        if 'M' in val:
            val = val.replace('M', '')
            val = float(val) * 1000000
        else:
            val = val.replace('K', '')
            val = float(val) * 1000
        return val

    df['Complete_Value'] = df['Value'].str.replace('€', '')
    print(df['Complete_Value'].unique())
    df['Complete_Value'] = df['Complete_Value'].apply(convertValue)
    print(df['Complete_Value'].head(20))


    def convertReleaseClause(rC):
        if 'M' in rC:
            rC = rC.replace('M', '')
            rC = float(rC) * 1000000
        else:
            rC = rC.replace('K', '')
            rC = float(rC) * 1000
        return int(rC)

    df['Complete_Release_Clause'] = df['Release Clause'].str.replace('€', '')
    print(df['Complete_Release_Clause'].unique())
    df['Complete_Release_Clause'] = df['Complete_Release_Clause'].apply(convertReleaseClause)
    print(df['Complete_Release_Clause'].head(100))
'''

'''
    Separate the Team & Contract column into sperate team & contract columns
'''
'''
    print(df['Team & Contract'].unique())
    df['Team & Contract'] = df['Team & Contract'].str.strip("\n")
    df['Team & Contract'] = df['Team & Contract'].str.split("\n")
    df['Updated Team'] = df['Team & Contract'].str[0]
    df['Updated Contract'] = df['Team & Contract'].str[1]
    print(df[['Team & Contract', 'Updated Team', 'Updated Contract']].head(10))
'''