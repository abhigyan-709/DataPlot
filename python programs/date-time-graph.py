from datetime import datetime
import pandas as pd
import plotly.express as px 

def inputDate():
    global from_date
    global to_date
    global no_days
    try:
        fromDate = input("Enter from date (DD/MM/YYYY): ")
        toDate = input("Enter to Date (DD/MM/YYYY): ")
        from_date = datetime.strptime(fromDate,"%d/%m/%Y").date()
        to_date = datetime.strptime(toDate,"%d/%m/%Y").date()
        no_days = abs((from_date-to_date).days)
        print("Difference between Date: ", no_days)
    except ValueError:
        print("Wrong input format given.")

    

def inputTime():
    global minutes
    try:
        fromTime = input("Enter from time (HH:MM:SS): ")
        toTime = input("Enter to time (HH:MM:SS): ")
        from_time = datetime.strptime(fromTime, "%H:%M:%S")
        to_time = datetime.strptime(toTime, "%H:%M:%S")
        print('Start Time: ', from_time.time())
        print('End Time: ', to_time.time())
        delta = abs(from_time - to_time)
        seconds = delta.total_seconds()
        minutes = seconds / 60
        print("Difference between time in minutes: ", minutes)
    except ValueError:
        print("Wrong input format given.")
    
def interval():
    global lst
    global mins
    global choice
    global interval_date
    global interval_mins
    mins = int(minutes)
    lst = []
    print("Total Time in Minutes ", mins)
    print("Total Days: ", no_days)

    try:
        choice = input("What type of interval you want to calculate(Days/Time) enter in D/T: ")
        if choice == "D":
            interval_date = int(input("Please enter the date enterval: "))
            for j in range(0, no_days, interval_date):
                lst.append(j)
            print("Date in equal intervals: ", lst)
        elif choice == "T":
            interval_mins = int(input("Please input the interval: "))
            for i in range(0, mins, interval_mins):
                lst.append(i)
            print("Time in equal intervals: ", lst)
    except ValueError:
        print("Wrong input format given.")
    

def dataplot():
    """
    Let's begin the data plotting.
    This is how we do, as we are having 2 dates as the X axis.
    Two intervals as min and maximum as y axis.
    """
    if choice == "D":
        fig = px.line(x=[0, mins, 2], y=[0, no_days, interval_date]) 
        fig.show()
    elif choice == "T":
        fig = px.line(x=[0, mins, interval_mins], y=[0, no_days, 2]) 
        fig.show()

def pdDataframe():
    if choice == "D":
        dataframe_date = {
            'Date' : lst,
            'Interval' : interval_date
        }
        df = pd.DataFrame(dataframe_date)
        print(df)
    elif choice == "T":
        dataframe_time = {
            'Time' : lst,
            'Interval' : interval_mins
        }
        df = pd.DataFrame(dataframe_time)
        print(df)
    

def main():
    inputDate()
    inputTime()
    interval()
    dataplot()
    pdDataframe()

if __name__=="__main__":
    main()