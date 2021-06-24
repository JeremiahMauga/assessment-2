import os.path
import csv
import string

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "../data/customers.csv")

class Customers:
    customer_list = []
    
    def __init__(self):
        pass
    
    # Appends all of our data from the csv to a list
    def get_customers_videos():
        with open(customer_path) as csvfile:
            read_data = csv.DictReader(csvfile)
            for line in read_data:
                Customers.customer_list.append(line)  
            
    # Prints out all data from the new list     
    def view_customers_videos():
        Customers.get_customers_videos()
        for line in Customers.customer_list:
            print(f"ID: {line['id']} NAME: {line['last_name']} CURRENT VIDEOS: {line['current_video_rentals']}")
    
    # Add a new customer to our customer.csv file
    def add_customer():
        Customers.get_customers_videos()
        # Getting new user input
        id = input("Enter Id: ")
        # Check to see if the Id input already exists or not
        for key in range(len(Customers.customer_list)):
            if id == Customers.customer_list[key]['id']:
                print("Id already exists!")
                Customers.customer_list.clear()
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