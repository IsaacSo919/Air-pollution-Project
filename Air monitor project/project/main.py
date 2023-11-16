# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

def main_menu():
    """Your documentation goes here"""
    # Your code goes her
    option=True
    while option:
        print("""
        --------The AQUA platform----------

        1.reporting menu(R)
        2.intelligence menu(I)
        3.monitoring menu(M)
        4.About(A)
        5.quit(Q)
        """)
        option = input("Please enter your option? ") 
        if option=="R": 
            reporting_menu()
            print("\n Reporting Menu is called")
        elif option=="I":
            print("\n Intelligence Menu is called") 
        elif option=="M":
            print("\n Monitoring Menu is called") 
        elif option=="A":
             about()
        elif option =="Q":
            print("\n Goodbye")
            option = quit()

        elif option !="":
            print("\n Not Valid Choice! Try again")


def reporting_menu():
    
    """Your documentation goes here"""
    
    # Your code goes here
    import pandas as pd
    import reporting as rp

    data ={
        'Harlington':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London Harlington.csv"),
        'Marylebone':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London N Kensington.csv"),
        'Kensington':pd.read_csv("D:\programs\Programming_Project\project\project\data\Pollution-London Marylebone Road.csv")
        }
    monitoring_station = ['Harlington', 'Marylebone Road', 'N Kensington']
    stations = input("Please choose the monitoring station : H-Harlington, M-Marylebone Road, K-N Kensington : ")
    if stations == 'H' :
        monitoring_station = 'Harlington'
    elif stations == 'M' :
        monitoring_station = 'Marylebone Road'    
    elif stations == 'N' :
        monitoring_station = 'N Kensington'
    else:
        print("The input is invalid, please input your choice again") 
        main_menu()

    pollutant = input("Please enter the pollutant(no/pm10/pm25):")
   
    
    Option=True
    while Option:
        print("Please input 1-8") 
        print("""
        --------reporting_menu----------

        1.daily average
        2.daily median
        3.hourly average
        4.monthly average
        5.peak hour date
        6.count missing_data
        7.fill missing data
        8.Back to main menu
        """)
        option = input("Please enter your option?(1-8) ") 
        if option=="1": 
            print("\n Calculating the daily average")
            
            print("Heres the result:")
            print(rp.daily_average(data,monitoring_station,pollutant))  
            option=False
        elif option=="2":
            print("\n Calculating the daily_median") 
            print(rp.daily_median(data,monitoring_station,pollutant))
            option=False
        elif option=="3":
            print("\n hourly average") 
            print(rp.hourly_average(data,monitoring_station,pollutant))
            option=False
        elif option=="4":
            print("\n monthly average")
            print(rp.monthly_average(data,monitoring_station,pollutant))
            option=False
        elif option == "5":
            print("\n peak hour date")
            date = input("Please enter the date:(year-mm-day): ")
            print(rp.peak_hour_date(data,date,monitoring_station,pollutant)) 
            option=False
        elif option == "6":
            print("\n count missing_data") 
            print(rp.count_missing_data(data,monitoring_station,pollutant)) 
        elif option == "7":
            print("\n fill missing data") 
            new_value = input("Please enter the New value: ")
            data[monitoring_station][pollutant]=rp.fill_missing_data(data,new_value,monitoring_station,pollutant)   
        elif option=="8":
            print("\n Back to main menu")
            option= False
            
            break
        elif option !="":
            print("\n Not Valid Choice! Try again")
        
def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here


def intelligence_menu():
    """Your documentation goes here"""
    # Your code goes here

def about():
    """Your documentation goes here"""
    # Your code goes here
    print("ECM1400 Student No.720086526")
def quit():
    """Your documentation goes here"""
    # Your code goes here
    return False




if __name__ == '__main__':
    main_menu()