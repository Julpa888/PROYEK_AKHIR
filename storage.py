import json
import os

class Storage:
    def __init__(self):
        self.data_dir = "data"
        self.create_data_dir()
        self.initialize_default_data()
    
    def create_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def initialize_default_data(self):
        if not os.path.exists(os.path.join(self.data_dir, "admin.json")):
            self.save_admin({"blacklist": "123"})
        
        if not os.path.exists(os.path.join(self.data_dir, "users.json")):
            self.save_users({
                "julpa": {"password": "321", "watchlist": []},
                "kikan": {"password": "321", "watchlist": []},
                "akmal": {"password": "321", "watchlist": []},
                "doni": {"password": "321", "watchlist": []}
            })
        
        if not os.path.exists(os.path.join(self.data_dir, "dramas.json")):
            self.save_dramas({
                "Taxi Driver": {"genre": "Crime", "episode": "16", "rating": "8.8", "status": "Finish"},
                "Vincenzo": {"genre": "Crime", "episode": "20", "rating": "8.9", "status": "Finish"},
                "Squid Game": {"genre": "Thriller", "episode": "9", "rating": "8.4", "status": "Finish"},
                "Goblin": {"genre": "Romance", "episode": "16", "rating": "8.8", "status": "Finish"},
                "Business Proposal": {"genre": "Romance", "episode": "12", "rating": "8.7", "status": "Finish"},
                "Weak Hero Class": {"genre": "Action", "episode": "8", "rating": "9.1", "status": "Finish"},
                "Itaewon Class": {"genre": "Drama", "episode": "16", "rating": "8.4", "status": "Finish"},
                "Mr Queen": {"genre": "Historical", "episode": "20", "rating": "8.6", "status": "Finish"},
                "Twinkling Watermelon": {"genre": "Youth", "episode": "16", "rating": "9.2", "status": "Finish"},
                "Hotel del Luna": {"genre": "Horror", "episode": "16", "rating": "8.6", "status": "Finish"},
                "Spirit Fingers": {"genre": "Romance", "episode": "12", "rating": "8.5", "status": "Ongoing"},
                "Would You Marry Me?": {"genre": "Romance", "episode": "12", "rating": "8.0", "status": "Ongoing"},
                "Dear X": {"genre": "Thriller", "episode": "12", "rating": "8.5", "status": "Ongoing"},
                "Typhoon Family": {"genre": "Drama", "episode": "16", "rating": "8.1", "status": "Ongoing"},
                "The Manipulated": {"genre": "Action", "episode": "12", "rating": "8.5", "status": "Ongoing"}
            })
    
    def load_data(self, filename):
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_data(self, filename, data):
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    
    def load_users(self):
        return self.load_data("users.json")
    
    def save_users(self, users):
        self.save_data("users.json", users)
    
    def load_admin(self):
        return self.load_data("admin.json")
    
    def save_admin(self, admin):
        self.save_data("admin.json", admin)
    
    def load_dramas(self):
        return self.load_data("dramas.json")
    
    def save_dramas(self, dramas):
        self.save_data("dramas.json", dramas)
