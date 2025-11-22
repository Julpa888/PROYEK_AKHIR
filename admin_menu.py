from prettytable import PrettyTable
from storage import Storage

class AdminManager:
    def __init__(self):
        self.storage = Storage()
        self.dramas = self.storage.load_dramas()

    def read_drama(self):
        if not self.dramas:
            print("Tidak ada drama yang tersedia.")
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

    def search_drama(self, keyword):
        hasil = {}
        for judul, data in self.dramas.items():
            if keyword.lower() in judul.lower() or keyword.lower() in data['genre'].lower():
                hasil[judul] = data
        return hasil

    def create_drama(self):
        print("\n" + "="*50)
        print("TAMBAH DRAMA BARU")
        print("="*50)
        
        judul = input("Judul: ").strip()
        if judul in self.dramas:
            print("Drama sudah ada dalam daftar!")
            return
        
        while True:
            genre = input("Genre: ").strip()
            if genre.replace(" ", "").isalpha():
                break
            print("Genre tidak boleh angka!")

        while True:
            episode = input("Jumlah Episode: ").strip()
            if episode.isdigit():
                episode = int(episode)
                break
            print("Episode harus berupa angka!")

        while True:
            status = input("Status (Finish/Ongoing): ").strip().capitalize()
            if status in ["Finish", "Ongoing"]:
                break
            print("Status hanya bisa 'Finish' atau 'Ongoing'!")

        while True:
            rating = input("Rating: ").strip()
            try:
                rating = float(rating)
                break
            except ValueError:
                print("Rating harus berupa angka!")

        self.dramas[judul] = {
            "genre": genre,
            "episode": episode,
            "status": status,
            "rating": rating
        }
        self.storage.save_dramas(self.dramas)
        print("Drama berhasil ditambahkan!")
    
    def update_drama(self):
        print("\n" + "="*50)
        print("UPDATE DATA DRAMA")
        print("="*50)
        
        self.read_drama()
        judul = input("\nMasukkan judul drama yang ingin diupdate: ").strip()
        
        if judul not in self.dramas:
            print("Drama tidak ditemukan!")
            return
        
        print(f"\nData saat ini untuk '{judul}':")
        print(f"Genre: {self.dramas[judul]['genre']}")
        print(f"Episode: {self.dramas[judul]['episode']}")
        print(f"Status: {self.dramas[judul]['status']}")
        print(f"Rating: {self.dramas[judul]['rating']}")
        
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")

        while True:
            genre = input(f"Genre [{self.dramas[judul]['genre']}]: ").strip()
            if not genre:
                break
            if genre.replace(" ", "").isalpha():
                break
            print("Genre tidak boleh angka!")

        while True:
            episode = input(f"Episode [{self.dramas[judul]['episode']}]: ").strip()
            if not episode:
                break
            if episode.isdigit():
                episode = int(episode)
                break
            print("Episode harus berupa angka!")

        while True:
            status = input(f"Status [{self.dramas[judul]['status']}]: ").strip()
            if not status:
                break
            status = status.capitalize()
            if status in ["Finish", "Ongoing"]:
                break
            print("Status hanya bisa 'Finish' atau 'Ongoing'!")

        while True:
            rating = input(f"Rating [{self.dramas[judul]['rating']}]: ").strip()
            if not rating:
                break
            try:
                rating = float(rating)
                break
            except ValueError:
                print("Rating harus berupa angka!")
        
        if genre:
            self.dramas[judul]['genre'] = genre
        if episode:
            self.dramas[judul]['episode'] = episode
        if status:
            self.dramas[judul]['status'] = status
        if rating:
            self.dramas[judul]['rating'] = rating
        
        self.storage.save_dramas(self.dramas)
        print("Data drama berhasil diupdate!")
    
    def delete_drama(self):
        print("\n" + "="*50)
        print("HAPUS DRAMA")
        print("="*50)
        
        self.read_drama()
        judul = input("\nMasukkan judul drama yang ingin dihapus: ").strip()
        
        if judul not in self.dramas:
            print("Drama tidak ditemukan!")
            return
        del self.dramas[judul]
        self.storage.save_dramas(self.dramas)
        users = self.storage.load_users()
        for username in users:
            users[username]["watchlist"] = [d for d in users[username]["watchlist"] if d != judul]
        self.storage.save_users(users)
        
        print("Drama berhasil dihapus!")
    
    def read_user_watchlists(self):
        print("\n" + "="*50)
        print("WATCHLIST PENGGUNA")
        print("="*50)
        users = self.storage.load_users()
        if not users:
            print("Tidak ada pengguna terdaftar.")
            return
        table = PrettyTable()
        table.field_names = ["Username", "Jumlah Watchlist", "Daftar Drama"]
        for username, data in users.items():
            watchlist = data["watchlist"]
            table.add_row([
                username,
                len(watchlist),
                ", ".join(watchlist) if watchlist else "Kosong"
            ])
        print(table)

    def search_drama(self):
        print("\n" + "="*50)
        print("CARI DRAMA")
        print("="*50)
        keyword = input("Masukkan judul atau genre drama: ").strip()
        results = self.search_drama(keyword)
        if not results:
            print("Tidak ditemukan drama dengan kata kunci tersebut.")
            return
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
        for i, (judul, data) in enumerate(results.items(), 1):
            table.add_row([
                i,
                judul,
                data["genre"],
                data["episode"],
                data["status"],
                data["rating"]
            ])
        print(f"\nHasil pencarian untuk '{keyword}':")
        print(table)
