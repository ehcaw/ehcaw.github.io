#importing libraries
import time
import calendar
from datetime import datetime
from __future__ import print_function
import httplib2
import os




#from matplotlib.dates import HourLocator, DateFormatter
import pandas as pd

class Schedule:
    
    
        
    '''
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
        '''

class UserDatabase:
    def __init__(self):
        self.users = pd.DataFrame(columns=['username'])

    def create_user(self, username):
        if username in self.users['username'].values:
            print("Username already exists.")
            return
        self.users.loc[len(self.users)] = [username]
        print("User created:", username)

    def get_user_by_username(self, username):
        user = self.users[self.users['username'] == username]
        if not user.empty:
            return user.iloc[0]
        else:
            print("User not found.")
            return None

class User:
    def __init__(self, username, user_db):  # Pass user_db as a parameter
        self.name = username
        self.busy_times = {}
        self.free_times = []
        self.friends = []
        user_db.create_user(username)

    def initialize_event(self, event_name, d, m, y, s, e):
        start_date_time = datetime(y, m, d, s)
        end_date_time = datetime(y, m, d, e)
        
        for busy_event_name, busy_times in self.busy_times.items():
            busy_start = busy_times[0]
            busy_end = busy_times[1]
            if start_date_time < busy_end and end_date_time > busy_start:
                print("Warning: You are busy during the invitation time.")
                return
        self.busy_times[event_name] = [start_date_time, end_date_time]
        print("Event added to busy times.")
    
    def add_friend(self, friend_username, user_db):
        friend = user_db.get_user_by_username(friend_username)
        if not friend.empty:  # Check if the DataFrame is not empty
            self.friends.append(friend_username)
            print(f"{friend_username} added to your friend list.")
        else:
            print(f"User {friend_username} does not exist.")

    def send_invite(self, event_name, user_db):
        invitee_username = input("Enter the username of the friend you want to invite: ")
        friend = user_db.get_user_by_username(invitee_username)
        if not friend.empty:
            if event_name in self.busy_times:
                event_times = self.busy_times[event_name]
                event_start_time = event_times[0].time()
                event_end_time = event_times[1].time()
                
                invite_date = event_times[0].date()
                invite_start_time = event_start_time
                invite_end_time = event_end_time
                
                for busy_times in friend.busy_times.values():
                    busy_start = busy_times[0].time()
                    busy_end = busy_times[1].time()
                    if invite_start_time < busy_end and invite_end_time > busy_start:
                        print(f"Warning: {invitee_username} is busy during the invitation time for event {event_name}.")
                        break
                else:  # Executed if the loop completes without a break
                    print(f"Invitation sent to {invitee_username} for event {event_name}.")
            else:
                print(f"Event {event_name} not found in your busy times.")
        else:
            print(f"User {invitee_username} not found.")


# Define the classes and main function...
def main():

    '''
    # Create instances of classes and interact as needed
    schedule_instance = Schedule()
    user_db = UserDatabase()
    user_instance = User('Bladee', user_db)
    user_instance2 = User('Ecco2k', user_db)
    
    user_instance.initialize_event('Drain Gang Meeting', 12, 8, 2023, 10, 12)
    user_instance.add_friend('Ecco2k', user_db)
    
    user_instance.send_invite('Drain Gang Meeting', user_db)

if __name__ == '__main__':
    main()  
    '''
s = Schedule()



