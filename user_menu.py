from prettytable import PrettyTable
from admin_menu import read_drama, search_drama
from storage import load_dramas, load_users, save_users

def create_watchlist(username):
    print("\n" + "="*50)
    print("TAMBAH KE WATCHLIST")
    print("="*50)

    read_drama()
    judul = input("\nMasukkan judul drama yang ingin ditambahkan: ").strip()

    if not judul:
        print("Judul tidak boleh kosong!")
        return

    dramas = load_dramas()
    users = load_users()

    if judul not in dramas:
        print("Drama tidak ditemukan!")
        return

    if username not in users:
        print("Pengguna tidak ditemukan!")
        return

    if judul in users[username]["watchlist"]:
        print("Drama sudah ada di watchlist Anda!")
        return

    users[username]["watchlist"].append(judul)
    save_users(users)
    print(f" '{judul}' berhasil ditambahkan ke watchlist!")

def read_watchlist(username):
    print("\n" + "="*50)
    print("WATCHLIST SAYA")
    print("="*50)

    users = load_users()
    dramas = load_dramas()

    if username not in users:
        print("Pengguna tidak ditemukan!")
        return

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

def remove_watchlist(username):
    print("\n" + "="*50)
    print("HAPUS DARI WATCHLIST")
    print("="*50)

    read_watchlist(username)

    users = load_users()
    if username not in users:
        print("Pengguna tidak ditemukan!")
        return

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
    save_users(users)
    print(f" '{judul}' berhasil dihapus dari watchlist!")

def search_drama_user():
    print("\n" + "="*50)
    print("CARI DRAMA")
    print("="*50)

    keyword = input("Masukkan judul atau genre drama: ").strip()

    if not keyword:
        print("Kata kunci tidak boleh kosong!")
        return

    results = search_drama(keyword)

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
