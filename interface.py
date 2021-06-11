from classes.customer import Customers
from classes.video import Videos

import time
import csv
import os.path
import sys

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "./data/customers.csv")

class Interface():
    customer_id = 0

    def __init__(self):
        
        self.runner()

# User interface
    def runner(self):
        while True:
            mode = input("\nWelcome to Code Platoon Video!\nOptions:\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n9. Quit\n")
            if mode == '1':
                # Views all of our inventory
                Videos.view_video_inventory()
                input("\nHit Enter to continue")
                break
            elif mode == '2':
                # Views all of our customers
                Customers.view_customers_videos()
                input("\nHit Enter to continue")
                break
            elif mode == '3':
                # Builds our list of customers
                Customers.get_customers_videos()
                # Checks for three videos for a customer
                Interface.check_limit()
                # Takes a video from inventory
                Videos.rent_video()
                # Adds video to an individual customers data
                Interface.update_customer()
                input("\nVideo rented!\nHit Enter to continue")
                # I need to break otherwise I'll keep on adding to the list of customers :P
                break
            elif mode == '4':
                Videos.return_video()
                input("\nHit Enter to continue")
                break
            elif mode == '5':
                Customers.add_customer()
                print("Customer added!")
                input("Hit Enter to continue")
                break
            elif mode == '9':
                print("Exiting program")
                time.sleep(1)
                break  
    
    # Updates the customers.csv with rented movie            
    def update_customer():
        # Add the video to the customer lists key value
        for i in Customers.customer_list:
            # Find the customer
            if i['id'] == str(Interface.customer_id):
                # Place video into customers database
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
        Interface.customer_id += int(input("Please enter customer ID: "))
        for key in Customers.customer_list:
            if key['id'] == str(Interface.customer_id): 
                num = key['current_video_rentals'].count('/')
                print(num)
                if num >= 2:
                    print("Customer already has 3 videos checked out!")
                    sys.exit()
                else:
                    pass
            
            
    
    def __str__(self):
        return                


    