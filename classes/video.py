import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
video_path = os.path.join(my_path, "../data/inventory.csv")

class Videos:
    video_list = []
    video_title = []

    def __init__(self, id, titles, rating):
        self.id = id
        self.titles = titles
        self.rating = rating
        pass
    
    # Appends all items from the csv file to a list
    def get_video_inventory():
        with open(video_path) as csvfile:
            read_data = csv.DictReader(csvfile)
            for line in read_data:
                Videos.video_list.append(line)  

    # Views all of the items from the new list         
    def view_video_inventory():
        Videos.get_video_inventory()
        for line in Videos.video_list:
            print(f"ID: {line['id']} TITLE: {line['title']} RATING: {line['rating']} COPIES AVAILABLE: {line['copies_available']}")
    
    def rent_video():
        # Gets the inventory of videos
        Videos.view_video_inventory()
        rented_video_id = input("Please enter video ID: ")
        # Looping through our dictionary of videos and taking out 1 of the specified ids
        for key in Videos.video_list:
            if key['id'] == rented_video_id:
                Videos.video_title.append(key['title'])
                new_value = int(key['copies_available'])
                new_value -= 1
                key['copies_available'] = str(new_value)
        # Rewriting and appending our new data to the inventory.csv file
        field_names = ['id','title','rating','copies_available']
        with open(video_path, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(Videos.video_list)

    # Did not finish return video method (does not udate in customer.csv, only updates in the inventory.csv)     
    def return_video():
        Videos.view_video_inventory()
        rented_video_id = input("Please enter video ID: ")
        # Looping through our dictionary of videos and returning 1 of the specified ids
        for key in Videos.video_list:
            if key['id'] == rented_video_id:
                new_value = int(key['copies_available'])
                new_value += 1
                key['copies_available'] = str(new_value)
        # Rewriting and appending our new data to the inventory.csv file
        field_names = ['id','title','rating','copies_available']
        with open(video_path, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(Videos.video_list)

    def __str__(self):
       return 