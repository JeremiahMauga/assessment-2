from classes.customer import Customers
from classes.video import Videos

import time
import csv
import os.path
import sys

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "./data/customers.csv")

class Interface():
    customer_name = ""

    def __init__(self):
        
        self.runner()

# User interface
    def runner(self):
        while True:
            mode = input("\nWelcome to Code Platoon Video!\nOptions:\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n9. Quit\n")
            if mode == '1':
                # Views all of our inventory
                Videos.view_video_inventory()
                Videos.video_list.clear()
                input("\nHit Enter to continue")
            elif mode == '2':
                # Views all of our customers
                Customers.view_customers_videos()
                Customers.customer_list.clear()
                input("\nHit Enter to continue")
            elif mode == '3':
                # Builds our list of customers
                Customers.get_customers_videos()
                # Checks for three videos for a customer
                Interface.check_limit()
                # Adds video to an individual customers data
            elif mode == '4':
                # Builds our list of customers
                Customers.view_customers_videos()
                # Creates video title to return
                rented_video_title = input("Please enter video title to return: ")
                # Updates the videos csv file
                Videos.return_video(rented_video_title)
                # Updates the customers csv file
                for name in Customers.customer_list:
                    if Customers.customer_name == name['last_name']:
                        print(name["last_name"])
                        
                input("\nHit Enter to continue")
            elif mode == '5':
                Customers.add_customer()
                Customers.customer_list.clear()
                print("Customer added!")
                input("Hit Enter to continue")
            elif mode == '9':
                print("Exiting program")
                time.sleep(1)
                break  
    
    # Updates the customers.csv with rented movie            
    def update_customer():
        # Takes a video from inventory, Performs checks
        Videos.video_list.clear()
        Videos.rent_video()
        # Add the video to the customer lists key value
        for i in Customers.customer_list:
            # Find the customer
            if i['last_name'] == str(Interface.customer_name):
                # Place video into customers database
                print(type(f"Current Videos: {i['current_video_rentals']}"))
                if not i['current_video_rentals']:
                    video_toAdd = ''.join(Videos.video_title)
                    i['current_video_rentals'] = (f"{i['current_video_rentals']}{video_toAdd}")
                    # Update data to the original customers.csv
                    field_names = ['id','first_name','last_name','current_video_rentals']
                    with open(customer_path, "w") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames = field_names)
                        writer.writeheader()
                        writer.writerows(Customers.customer_list)
                        break
                else:
                    video_toAdd = ''.join(Videos.video_title)
                    i['current_video_rentals'] = (f"{i['current_video_rentals']}/{video_toAdd}")
                    # Update data to the original customers.csv
                    field_names = ['id','first_name','last_name','current_video_rentals']
                    with open(customer_path, "w") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames = field_names)
                        writer.writeheader()
                        writer.writerows(Customers.customer_list)
                        break        
                
    def check_limit():
        # Check to see if customer has 3 videos already checked out
        # Keeps track of our customers ID
        Interface.customer_name += input("Please enter customer Name: ")
        for key in Customers.customer_list:
            if key['last_name'] == str(Interface.customer_name): 
                num = key['current_video_rentals'].count('/')
                print(num)
                if num >= 2:
                    print("Customer already has 3 videos checked out!")
                    Interface.customer_name = ""
                    Interface.check_limit()
                else:
                    Interface.update_customer()
                    input("\nVideo rented!\nHit Enter to continue")
                    # I got it to break out of that loop!
            
            
    
    def __str__(self):
        return                


    