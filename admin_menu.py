from prettytable import PrettyTable
from drama import DramaManager
from storage import Storage

class AdminManager:
    def __init__(self):
        self.drama_manager = DramaManager()
        self.storage = Storage()
    
    def menu(self, username):
        while True:
            print("\n" + "="*60)
            print(f"SELAMAT DATANG, ADMIN {username.upper()}!")
            print("="*60)
            print("1. 📝 Tambah Drama Baru")
            print("2. 📖 Lihat Semua Drama")
            print("3. ✏️  Update Data Drama")
            print("4. 🗑️  Hapus Drama")
            print("5. 👥 Lihat Watchlist Pengguna")
            print("6. 🔍 Cari Drama")
            print("7. 🚪 Logout")
            
            choice = input("\nPilih menu (1-7): ").strip()
            
            if choice == '1':
                self.drama_manager.add_drama()
            elif choice == '2':
                self.drama_manager.display_all_dramas()
            elif choice == '3':
                self.drama_manager.update_drama()
            elif choice == '4':
                self.drama_manager.delete_drama()
            elif choice == '5':
                self.view_user_watchlists()
            elif choice == '6':
                self.search_drama()
            elif choice == '7':
                print("👋 Terima kasih, Admin!")
                break
            else:
                print("❌ Pilihan tidak valid!")
    
    def view_user_watchlists(self):
        print("\n" + "="*50)
        print("WATCHLIST PENGGUNA")
        print("="*50)
        
        users = self.storage.load_users()
        
        if not users:
            print("❌ Tidak ada pengguna terdaftar.")
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
        results = self.drama_manager.search_drama(keyword)
        
        if not results:
            print("❌ Tidak ditemukan drama dengan kata kunci tersebut.")
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