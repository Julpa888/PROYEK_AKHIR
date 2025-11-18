from prettytable import PrettyTable
from storage import Storage

class DramaManager:
    def __init__(self):
        self.storage = Storage()
        self.dramas = self.storage.load_dramas()
    
    def display_all_dramas(self):
        if not self.dramas:
            print("❌ Tidak ada drama yang tersedia.")
            return
        
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
        
        for i, (judul, data) in enumerate(self.dramas.items(), 1):
            table.add_row([
                i,
                judul,
                data["genre"],
                data["episode"],
                data["status"],
                data["rating"]
            ])
        
        print("\n" + "="*80)
        print("DAFTAR DRAMA KOREA")
        print("="*80)
        print(table)
    
    def add_drama(self):
        print("\n" + "="*50)
        print("TAMBAH DRAMA BARU")
        print("="*50)
        
        judul = input("Judul: ").strip()
        if judul in self.dramas:
            print("❌ Drama sudah ada dalam daftar!")
            return
        
        genre = input("Genre: ").strip()
        episode = input("Jumlah Episode: ").strip()
        status = input("Status (Finish/Ongoing): ").strip().capitalize()
        rating = input("Rating: ").strip()
        
        self.dramas[judul] = {
            "genre": genre,
            "episode": episode,
            "status": status,
            "rating": rating
        }
        self.storage.save_dramas(self.dramas)
        print("✅ Drama berhasil ditambahkan!")
    
    def update_drama(self):
        print("\n" + "="*50)
        print("UPDATE DATA DRAMA")
        print("="*50)
        
        self.display_all_dramas()
        judul = input("\nMasukkan judul drama yang ingin diupdate: ").strip()
        
        if judul not in self.dramas:
            print("❌ Drama tidak ditemukan!")
            return
        
        print(f"\nData saat ini untuk '{judul}':")
        print(f"Genre: {self.dramas[judul]['genre']}")
        print(f"Episode: {self.dramas[judul]['episode']}")
        print(f"Status: {self.dramas[judul]['status']}")
        print(f"Rating: {self.dramas[judul]['rating']}")
        
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        genre = input(f"Genre [{self.dramas[judul]['genre']}]: ").strip()
        episode = input(f"Episode [{self.dramas[judul]['episode']}]: ").strip()
        status = input(f"Status [{self.dramas[judul]['status']}]: ").strip()
        rating = input(f"Rating [{self.dramas[judul]['rating']}]: ").strip()
        
        if genre:
            self.dramas[judul]['genre'] = genre
        if episode:
            self.dramas[judul]['episode'] = episode
        if status:
            self.dramas[judul]['status'] = status.capitalize()
        if rating:
            self.dramas[judul]['rating'] = rating
        
        self.storage.save_dramas(self.dramas)
        print("✅ Data drama berhasil diupdate!")
    
    def delete_drama(self):
        print("\n" + "="*50)
        print("HAPUS DRAMA")
        print("="*50)
        
        self.display_all_dramas()
        judul = input("\nMasukkan judul drama yang ingin dihapus: ").strip()
        
        if judul not in self.dramas:
            print("❌ Drama tidak ditemukan!")
            return
        
        confirm = input(f"Apakah Anda yakin ingin menghapus '{judul}'? (y/n): ").lower()
        if confirm == 'y':
            del self.dramas[judul]
            self.storage.save_dramas(self.dramas)
            
            # Also remove from all users' watchlists
            users = self.storage.load_users()
            for username in users:
                users[username]["watchlist"] = [d for d in users[username]["watchlist"] if d != judul]
            self.storage.save_users(users)
            
            print("✅ Drama berhasil dihapus!")
        else:
            print("❌ Penghapusan dibatalkan.")
    
    def search_drama(self, keyword):
        results = {}
        for judul, data in self.dramas.items():
            if keyword.lower() in judul.lower() or keyword.lower() in data['genre'].lower():
                results[judul] = data
        return results