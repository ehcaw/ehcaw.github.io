#importing libraries
import time
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter
import pandas as pd

'''
class schedule:
    def __init__(self):
        today = datetime.now()
        c = calendar.HTMLCalendar(firstweekday=0)
        str = c.formatmonth(today.year, today.month)
        print(str)
    
    def zoomToDay(self):
        zoomDate = input("Please enter the numeric date you would like to view: ")
        start_time = datetime(datetime.now().year, datetime.now().month, int(zoomDate), 0, 0, 0)
        end_time = datetime(datetime.now().year, datetime.now().month, int(zoomDate), 23, 59, 59)

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 2))

        # Plot the timeline
        ax.hlines(y=0, xmin=start_time, xmax=end_time, colors='b', linewidth=4)

        # Set the x-axis limits and ticks
        ax.set_xlim(start_time, end_time)
        ax.xaxis.set_major_locator(HourLocator(interval=1))  # Use HourLocator from matplotlib.dates
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))  # Use DateFormatter from matplotlib.dates

        # Remove y-axis
        ax.yaxis.set_visible(False)

        # Set title and show the plot
        plotTitle = "Schedule for {}/{}/{}.".format(datetime.now().month, zoomDate, datetime.now().year)
        plt.title(plotTitle)
        plt.show()

class userDatabase:
    def __init__(self):
        self.users = pd.DataFrame(columns=['username', 'email'])

    def create_user(self, username, email):
        if username in self.users['username'].values:
            print("Username already exists.")
            return
        self.users = self.users.append({'username': username, 'email': email}, ignore_index=True)
        print("User created:", username, email)

    def get_user_by_username(self, username):
        user = self.users[self.users['username'] == username]
        if not user.empty:
            return user.iloc[0]
        else:
            print("User not found.")
            return None


class user:
    def __init__(self, name):
        self.userName = name  # Add 'self' to instance variables
        self.busyTimes = []
        self.freeTimes = []
    
    def initializeEvent(self, name, d, m, y, s, e):  # Remove 'user' parameter
        startDateTime = datetime(y, m, d, s)
        endDateTime = datetime(y, m, d, e)
        for i in range(len(self.busyTimes)):
            busy_start = self.busyTimes[i].date[0]
            busy_end = self.busyTimes[i].date[1]
            if startDateTime < busy_end and endDateTime > busy_start:
                print("Warning: You are busy during the invitation time.")
            else:
                e = event(self, name, d, m, y, s, e)  # Pass 'self' instead of 'user'
                self.busyTimes.append(e)  # Append the instantiated event object
    
class event:
    def __init__(self, user, name, d, m, y, s, e):  # Add 'self' parameter and fix date initialization
        self.people = []
        self.eventName = name
        self.date = [datetime(y, m, d, s), datetime(y, m, d, e)]  # Store start and end date times


class group():
    def __init__(self, n):  
        name = n
        members = []
    def invite(groupMember):
        inviteUser = input("Please enter the name of the user you would like to invite: ")
        if user 

def main():
    c = schedule()
    c.zoomToDay()

main()
'''
class Schedule:
    def zoom_to_day(self):
        zoom_date = input("Please enter the numeric date you would like to view: ")
        start_time = datetime(datetime.now().year, datetime.now().month, int(zoom_date), 0, 0, 0)
        end_time = datetime(datetime.now().year, datetime.now().month, int(zoom_date), 23, 59, 59)

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 2))

        # Plot the timeline
        ax.hlines(y=0, xmin=start_time, xmax=end_time, colors='b', linewidth=4)

        # Set the x-axis limits and ticks
        ax.set_xlim(start_time, end_time)
        ax.xaxis.set_major_locator(HourLocator(interval=1))  # Use HourLocator from matplotlib.dates
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))  # Use DateFormatter from matplotlib.dates

        # Remove y-axis
        ax.yaxis.set_visible(False)

        # Set title and show the plot
        plot_title = "Schedule for {}/{}/{}.".format(datetime.now().month, zoom_date, datetime.now().year)
        plt.title(plot_title)
        plt.show()

class UserDatabase:
    def __init__(self):
        self.users = pd.DataFrame(columns=['username', 'email'])

    def create_user(self, username, email):
        if username in self.users['username'].values:
            print("Username already exists.")
            return
        self.users = self.users.append({'username': username, 'email': email}, ignore_index=True)
        print("User created:", username, email)

    def get_user_by_username(self, username):
        user = self.users[self.users['username'] == username]
        if not user.empty:
            return user.iloc[0]
        else:
            print("User not found.")
            return None

class User:
    def __init__(self, name):
        self.username = name
        self.busy_times = []
        self.free_times = []

    def initialize_event(self, name, d, m, y, s, e):
        start_date_time = datetime(y, m, d, s)
        end_date_time = datetime(y, m, d, e)
        for busy_time in self.busy_times:
            busy_start = busy_time[0]
            busy_end = busy_time[1]
            if start_date_time < busy_end and end_date_time > busy_start:
                print("Warning: You are busy during the invitation time.")
                return
        self.busy_times.append((start_date_time, end_date_time))
        print("Event added to busy times.")

# Define the classes and main function...
def main():
    # Create instances of classes and interact as needed
    schedule_instance = Schedule()
    user_db = UserDatabase()
    user_instance = User('John')
    user_instance.initialize_event('Meeting', 12, 8, 2023, 10, 12)

if __name__ == '__main__':
    main()




