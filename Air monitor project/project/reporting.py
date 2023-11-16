# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


import numpy as np
import pandas as pd
import utils as ut
##nested dictionary


data ={
    'Harlington':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London Harlington.csv"),
    'Marylebone':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London N Kensington.csv"),
    'Kensington':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London Marylebone Road.csv")
    }



# A = data['Harlington']['pm25'].to_list()
# print('\n\n\n\n')
# for i in range(24,48):
#     print(A[i],end=',')
# print('\n\n\n\n')

def daily_average(data, monitoring_station:str, pollutant:str):
    ## Your code goes here
    """Your documentation goes here
        The 1st for loop is for iteration between days and the 2nd for loop is for iteration between hours for that day
        We append one data to a list named day and calculate the mean and append the result to the array Q and append it through each days and save it to average """
    
    A = data[monitoring_station][pollutant].to_list()
    A = np.array(A)
    Averages = []
    
    for i in range(0 ,len(A), 24):
        day = [] #empty the day array
        # day = [
        #     A[j].astype(np.float) for j in range(i, i+24) if A[j] != "No data"
        # ]
        for j in range(i,i+24):
            if (A[j] != 'No data'):
                a = A[j]
                b = a.astype(np.float)
                 #changing the data type from str to float
                day.append(b)
                
                Q = np.mean(day)
                
        Q=np.round(Q, decimals=5)               
        Averages.append(Q)          
    return Averages     

def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    
    ## Your code goes here
    A = data[monitoring_station][pollutant].to_list() #Get the data from using dictionary in this format and convert to list
    A = np.array(A)
    Median = []

    
    for i in range(0 ,len(A), 24):
        day=[] #empty the day array for each day
        for j in range(i,i+24):#iterate through each hour
            if (A[j]!= 'No data'):
                a = A[j]
                b = a.astype(np.float)
                day.append(b)
            
            elif(A[j]== 'No data'):
                day.append(0.0)

           #changing the data type from str to float
            
        day = np.sort(day) 
        
        middle = float(len(day))/2# This part is for finding the median after sorting
        
        if middle % 2 != 0:
            Q = day[np.int(middle - 0.5)]

        else:
            c = day[np.int(middle-1)]+day[np.int(middle)]
            d= c/2
            Q=np.round(d, decimals=5)
            

        Median.append(Q)  
    return Median


def hourly_average(data, monitoring_station, pollutant):
    target_data = data[monitoring_station]
    target_data = target_data[target_data[pollutant].str.contains("No data") == False]
    for _,  rows in target_data.iterrows():
        if rows.time.startswith("24"):
            rows.time = "00" + rows.time[2:]
    target_data[pollutant] = target_data[pollutant].astype(float)

    return list(target_data.groupby(pd.PeriodIndex(target_data['time'], freq="h"))[pollutant].mean())
    ## Your code goes here


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    target_data = data[monitoring_station]
    target_data = target_data[target_data[pollutant].str.contains("No data") == False]
    target_data[pollutant] = target_data[pollutant].astype(float)
    
    return list(target_data.groupby(pd.PeriodIndex(target_data['date'], freq="M"))[pollutant].mean())
    ## Your code goes here



def peak_hour_date(data, date:str, monitoring_station:str,pollutant:str):
    """Your documentation goes here"""
    target_data = data[monitoring_station]
    target_data = target_data[target_data[pollutant].str.contains("No data") == False]
    
    target_data[pollutant] = target_data[pollutant].astype(float)
    target_data = pd.DataFrame(target_data[target_data['date'].str.contains(date) == True])
    
    biggest=(target_data[pollutant].max())
    
    for _,record in target_data.iterrows():
        if record[pollutant] == biggest:
            return record['time'], biggest
            
    
    ## Your code goes here

def count_missing_data(data,  monitoring_station:str,pollutant:str):
    """Your documentation goes here"""
    target_data = data[monitoring_station]
    return(target_data[data[monitoring_station][pollutant].str.contains('No data')== True].shape)[0]
    ## Your code goes here

def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Your documentation goes here"""
    target_data = data[monitoring_station]
    
    return(list(target_data[pollutant].replace(['No data'],new_value)))
    
    ## Your code goes here

if __name__ == '__main__':
    
    print('After if')