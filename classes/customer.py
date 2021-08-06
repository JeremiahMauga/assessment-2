import os.path
import csv
import string

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "../data/customers.csv")

class Customers:
    customer_list = []
    customer_name = ""
    
    def __init__(self):
        pass
    
    # Appends all of our data from the csv to a list
    def get_customers_videos():
        with open(customer_path) as csvfile:
            read_data = csv.DictReader(csvfile)
            for line in read_data:
                Customers.customer_list.append(line)  
            
    # Prints out all data from the new list
    # Refactored to take in a customers name and only prints out their rented videos     
    def view_customers_videos():
        Customers.customer_list.clear()
        Customers.get_customers_videos()
        for line in Customers.customer_list:
            # print(f"ID: {line['id']} NAME: {line['last_name']} CURRENT VIDEOS: {line['current_video_rentals']}")
            print(f"NAME: {line['last_name']}")
        id = input("Enter Customer Name: ")
        Customers.customer_name = id
        for line in Customers.customer_list:
            if id == line['last_name']:
                print("Match!")
                print(f"Videos checked out: {line['current_video_rentals']}")
        
    # Add a new customer to our customer.csv file
    # Only adds one customer and breaks out of the loop
    def add_customer():      
        Customers.customer_list.clear()
        Customers.get_customers_videos()
        # Getting new user input
        input_id = input("Enter New Id: ")
        # Check to see if the Id input already exists or not
        customer_ids = []
        for line in (Customers.customer_list):
            customer_ids.append(line['id'])
        # Loop through our customer ids
        customer_ids_set = set(customer_ids)
        if input_id in customer_ids_set:
            print("Id already exists!")
            Customers.add_customer()
        else:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            new_data = {'id': f'{id}', 'first_name': f'{first_name}', 'last_name': f'{last_name}', 'current_video_rentals': ''}
            # Append new user input to our customer list
            Customers.customer_list.append(new_data)
            # Appending data with write over our customrs.csv
            field_names = ['id','first_name','last_name','current_video_rentals']
            with open(customer_path, "w") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = field_names)
                    writer.writeheader()
                    writer.writerows(Customers.customer_list)
            
    def __str__(self):
       return 