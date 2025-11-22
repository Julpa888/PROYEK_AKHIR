from prettytable import PrettyTable
from storage import load_dramas, save_dramas, load_users, save_users

def read_drama():
    dramas = load_dramas()
    if not dramas:
        print("Tidak ada drama yang tersedia.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]

    for i, (judul, data) in enumerate(dramas.items(), 1):
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

def search_drama(keyword):
    dramas = load_dramas()
    hasil = {}
    for judul, data in dramas.items():
        if keyword.lower() in judul.lower() or keyword.lower() in data['genre'].lower():
            hasil[judul] = data
    return hasil

def search_drama_menu():
    print("\n" + "="*50)
    print("CARI DRAMA")
    print("="*50)
    keyword = input("Masukkan judul atau genre drama: ").strip()
    if not keyword:
        print("drama tidak tersedia")
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

def create_drama():
    dramas = load_dramas()

    print("\n" + "="*50)
    print("TAMBAH DRAMA BARU")
    print("="*50)

    while True:
        judul = input("Judul: ").strip()
        if not judul:
            print("input tidak valid")
            continue
        if judul in dramas:
            print("Drama sudah ada dalam daftar!")
            return
        break

    while True:
        genre = input("Genre: ").strip()
        if genre.replace(" ", "").isalpha():
            break
        print("input tidak valid")

    while True:
        episode = input("Jumlah Episode: ").strip()
        if episode.isdigit():
            episode = int(episode)
            break
        print("input tidak valid")

    while True:
        status = input("Status (Finish/Ongoing): ").strip().capitalize()
        if status in ["Finish", "Ongoing"]:
            break
        print("input tidak valid")

    while True:
        rating = input("Rating: ").strip()
        try:
            rating = float(rating)
            break
        except ValueError:
            print("input tidak valid")

    dramas[judul] = {
        "genre": genre,
        "episode": episode,
        "status": status,
        "rating": rating
    }
    save_dramas(dramas)
    print("Drama berhasil ditambahkan!")

def update_drama():
    dramas = load_dramas()

    print("\n" + "="*50)
    print("UPDATE DATA DRAMA")
    print("="*50)

    if not dramas:
        print("Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul = input("\nMasukkan judul drama yang ingin diupdate: ").strip()

    if judul not in dramas:
        print("Drama tidak ditemukan!")
        return

    print(f"\nData saat ini untuk '{judul}':")
    print(f"Genre: {dramas[judul]['genre']}")
    print(f"Episode: {dramas[judul]['episode']}")
    print(f"Status: {dramas[judul]['status']}")
    print(f"Rating: {dramas[judul]['rating']}")

    print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")

    while True:
        genre = input(f"Genre [{dramas[judul]['genre']}]: ").strip()
        if not genre:
            genre = None
            break
        if genre.replace(" ", "").isalpha():
            break
        print("input tidak valid")

    while True:
        episode = input(f"Episode [{dramas[judul]['episode']}]: ").strip()
        if not episode:
            episode = None
            break
        if episode.isdigit():
            episode = int(episode)
            break
        print("input tidak valid")

    while True:
        status = input(f"Status [{dramas[judul]['status']}]: ").strip()
        if not status:
            status = None
            break
        status = status.capitalize()
        if status in ["Finish", "Ongoing"]:
            break
        print("input tidak valid")

    while True:
        rating = input(f"Rating [{dramas[judul]['rating']}]: ").strip()
        if not rating:
            rating = None
            break
        try:
            rating = float(rating)
            break
        except ValueError:
            print("input tidak valid")

    if genre:
        dramas[judul]['genre'] = genre
    if episode is not None:
        dramas[judul]['episode'] = episode
    if status:
        dramas[judul]['status'] = status
    if rating is not None:
        dramas[judul]['rating'] = rating

    save_dramas(dramas)
    print("Data drama berhasil diupdate!")

def delete_drama():
    dramas = load_dramas()

    print("\n" + "="*50)
    print("HAPUS DRAMA")
    print("="*50)

    if not dramas:
        print("Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = ["No", "Judul", "Genre", "Episode", "Status", "Rating"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul = input("\nMasukkan judul drama yang ingin dihapus: ").strip()

    if judul not in dramas:
        print("Drama tidak ditemukan!")
        return
    del dramas[judul]
    save_dramas(dramas)
    users = load_users()
    for username in users:
        users[username]["watchlist"] = [d for d in users[username]["watchlist"] if d != judul]
    save_users(users)

    print("Drama berhasil dihapus!")

def read_user_watchlists():
    users = load_users()
    print("\n" + "="*50)
    print("WATCHLIST PENGGUNA")
    print("="*50)
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
