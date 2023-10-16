import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def df_creation(dataset):
    df = pd.read_csv(dataset)
    df = df.set_index('Datetime')
    df.index = pd.to_datetime(df.index)
    return df

def visualization(file,date):
    
    df = df_creation(file)
    train_data = df.loc[df.index < date]
    test_data = df.loc[df.index >= date]
    fig, ax = plt.subplots(figsize = (35,20))
    train_data.plot(ax = ax, label = 'Training Data')
    test_data.plot(ax = ax, label = 'Training Data')
    #df.plot(figsize=(35,20))
    plt.show()

def feature_creation(n, file):
    df = df_creation(file)
    file_header = ['AEP_MW','COMED_MW','DAYTON_MW','DEOK_MW','DOM_MW','DUQ_MW','EKPC_MW','FE_MW','NI_MW']
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    sns.set(style='darkgrid')
    fig, ax = plt.subplots(figsize = (12,9))
    sns.boxplot(x="month", y= file_header[n], data=df, palette='bright')
    ax.set_title("Energy Consumption/Month")
    plt.show()

if __name__ == '__main__':

    data = [['../IBM Project/Dataset/AEP_hourly.csv','02-01-2017'],
            ['../IBM Project/Dataset/COMED_hourly.csv','08-01-2017'],
            ['../IBM Project/Dataset/DAYTON_hourly.csv','10-01-16'],
            ['../IBM Project/Dataset/DEOK_hourly.csv','06-01-17'],
            ['../IBM Project/Dataset/DOM_hourly.csv','01-01-17'],
            ['../IBM Project/Dataset/DUQ_hourly.csv','06-01-16'],
            ['../IBM Project/Dataset/EKPC_hourly.csv','08-01-17'],
            ['../IBM Project/Dataset/FE_hourly.csv','02-01-17'],
            ['../IBM Project/Dataset/NI_hourly.csv','07-01-09']]

    print("1.AEP\n2.COMED\n3.DAYTON\n4.DEOK\n5.DOM\n6.DUQ\n7.EKPC\n8.FE\n9.NI\n")
    n = int(input())
    if(n in range(1,10)):
        visualization(data[n-1][0],data[n-1][1])
        feature_creation(n-1, data[n-1][0])
    else:
        print("Invalid Input!")
    
