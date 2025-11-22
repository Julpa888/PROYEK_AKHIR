from prettytable import PrettyTable
from admin_menu import AdminManager
from storage import Storage

class UserManager:
    def __init__(self):
        self.drama_manager = AdminManager()
        self.storage = Storage()
    
    def create_watchlist(self, username):
        print("\n" + "="*50)
        print("TAMBAH KE WATCHLIST")
        print("="*50)
        
        self.drama_manager.read_drama()
        judul = input("\nMasukkan judul drama yang ingin ditambahkan: ").strip()

        if not judul:
            print("Judul tidak boleh kosong!")
            return
        
        dramas = self.storage.load_dramas()
        users = self.storage.load_users()
        
        if judul not in dramas:
            print("Drama tidak ditemukan!")
            return
        
        if judul in users[username]["watchlist"]:
            print("Drama sudah ada di watchlist Anda!")
            return
        
        users[username]["watchlist"].append(judul)
        self.storage.save_users(users)
        print(f" '{judul}' berhasil ditambahkan ke watchlist!")
    
    def read_watchlist(self, username):
        print("\n" + "="*50)
        print("WATCHLIST SAYA")
        print("="*50)
        
        users = self.storage.load_users()
        dramas = self.storage.load_dramas()
        watchlist = users[username]["watchlist"]
        
        if not watchlist:
            print("Watchlist Anda masih kosong.")
            return
        
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
        
        for i, judul in enumerate(watchlist, 1):
            if judul in dramas:
                data = dramas[judul]
                table.add_row([
                    i,
                    judul,
                    data["genre"],
                    data["episode"],
                    data["status"],
                    data["rating"]
                ])
        
        print(table)
    
    def remove_watchlist(self, username):
        print("\n" + "="*50)
        print("HAPUS DARI WATCHLIST")
        print("="*50)
        
        self.read_watchlist(username)
        
        users = self.storage.load_users()
        watchlist = users[username]["watchlist"]
        
        if not watchlist:
            return
        
        judul = input("\nMasukkan judul drama yang ingin dihapus: ").strip()

        if not judul:
            print("Judul tidak boleh kosong!")
            return
        
        if judul not in watchlist:
            print("Drama tidak ditemukan di watchlist Anda!")
            return

        watchlist.remove(judul)
        self.storage.save_users(users)
        print(f" '{judul}' berhasil dihapus dari watchlist!")
    
    def search_drama_user(self):
        print("\n" + "="*50)
        print("CARI DRAMA")
        print("="*50)
        
        keyword = input("Masukkan judul atau genre drama: ").strip()

        if not keyword:
            print("Kata kunci tidak boleh kosong!")
            return

        results = self.drama_manager.search_drama(keyword)
        
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
