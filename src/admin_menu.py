from prettytable import PrettyTable
from colorama import Fore, Style
from storage import load_dramas, save_dramas, load_users, save_users
from InquirerPy import inquirer

GENRES = ["Crime", "Thriller", "Romance", "Action", "Drama", "Historical", "Youth", "Horror"]

def read_drama():
    dramas = load_dramas()
    if not dramas:
        print(f"{Fore.RED}Tidak ada drama yang tersedia.")
        return

    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]

    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([
            i,
            judul,
            data["genre"],
            data["episode"],
            data["status"],
            data["rating"]
        ])

    print(f"\n{Fore.RED}{'█' * 80}")
    print(f"{Fore.YELLOW}📺 DAFTAR DRAMA KOREA 📺")
    print(f"{Fore.RED}{'█' * 80}{Style.RESET_ALL}")
    print(table)

def search_drama(keyword):
    dramas = load_dramas()
    hasil = {}
    for judul, data in dramas.items():
        if keyword.lower() in judul.lower(): 
            hasil[judul] = data
    return hasil


def search_drama_menu():
    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}🔍 CARI DRAMA 🔍")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")
    keyword = input(f"{Fore.CYAN}Masukkan judul drama: {Style.RESET_ALL}").strip()
    if not keyword:
        print(f"{Fore.RED}Input tidak boleh kosong!")
        return
    results = search_drama(keyword)
    if not results:
        print(f"{Fore.RED}Tidak ditemukan drama dengan judul tersebut.")
        return

    table = PrettyTable()
    table.field_names = [
        f"{Fore.CYAN}No",
        f"{Fore.CYAN}Judul",
        f"{Fore.CYAN}Genre",
        f"{Fore.CYAN}Episode",
        f"{Fore.CYAN}Status",
        f"{Fore.CYAN}Rating{Style.RESET_ALL}",
    ]
    for i, (judul, data) in enumerate(results.items(), 1):
        table.add_row([
            i,
            judul,
            data["genre"],
            data["episode"],
            data["status"],
            data["rating"]
        ])
    print(f"{Fore.GREEN}Hasil pencarian untuk '{keyword}':")
    print(table)


def create_drama():
    dramas = load_dramas()

    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}➕ TAMBAH DRAMA BARU ➕")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}(Ketik 'cancel' kapan saja untuk membatalkan)\n{Style.RESET_ALL}")

    while True:
        judul_raw = input(f"{Fore.CYAN}Judul: {Style.RESET_ALL}").strip()
        if judul_raw.lower() == 'cancel':
            print(f"{Fore.YELLOW}Pembatalan penambahan drama.")
            return
        if not judul_raw:
            print(f"{Fore.RED}Input tidak valid")
            continue
        judul = judul_raw.title()
        valid_chars = all(c.isalnum() or c in " ,.-'?!:" for c in judul)
        if not valid_chars:
            print(f"{Fore.RED}Input tidak valid")
            continue
        if judul in dramas:
            print(f"{Fore.RED}Drama sudah ada dalam daftar!")
            return
        break

    genre = inquirer.select(message="Genre:", choices=GENRES).execute()

    while True:
        episode = input(f"{Fore.CYAN}Jumlah Episode: {Style.RESET_ALL}").strip()
        if episode.lower() == 'cancel':
            print(f"{Fore.YELLOW}Pembatalan penambahan drama.")
            return
        if episode.isdigit():
            episode = int(episode)
            break
        print(f"{Fore.RED}Input tidak valid")

    status = inquirer.select(message="Status (Finish/Ongoing):", choices=["Finish", "Ongoing"]).execute()

    while True:
        rating = input(f"{Fore.CYAN}Rating (0.0-10): {Style.RESET_ALL}").strip()
        if rating.lower() == 'cancel':
            print(f"{Fore.YELLOW}Pembatalan penambahan drama.")
            return
        try:
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                break
            else:
                print(f"{Fore.RED}Input tidak valid (rating harus 0.0-10)")
        except ValueError:
            print(f"{Fore.RED}Input tidak valid")

    dramas[judul] = {
        "genre": genre,
        "episode": episode,
        "status": status,
        "rating": rating
    }

    save_dramas(dramas)

    print(f"{Fore.GREEN}Drama berhasil ditambahkan!")

def update_drama():
    dramas = load_dramas()

    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}✏️  UPDATE DATA DRAMA ✏️")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")

    if not dramas:
        print(f"{Fore.RED}Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul_input = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin diupdate: {Style.RESET_ALL}").strip()
    if not judul_input:
        print(f"{Fore.RED}Input tidak valid!")
        return

    judul_ditemukan = None
    for j in dramas:
        if j.lower() == judul_input.lower():
            judul_ditemukan = j
            break

    if not judul_ditemukan:
        print(f"{Fore.RED}Drama tidak ditemukan!")
        return

    judul = judul_ditemukan

    print(f"\n{Fore.GREEN}Data saat ini untuk '{judul}':")
    print(f"{Fore.CYAN}Genre: {dramas[judul]['genre']}")
    print(f"{Fore.CYAN}Episode: {dramas[judul]['episode']}")
    print(f"{Fore.CYAN}Status: {dramas[judul]['status']}")
    print(f"{Fore.CYAN}Rating: {dramas[judul]['rating']}{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Masukkan data baru (kosongkan jika tidak ingin mengubah):")

    pilih_genre = inquirer.select(
        message=f"Genre [{dramas[judul]['genre']}]",
        choices=["(Biarkan Tetap)"] + GENRES
    ).execute()

    if pilih_genre == "(Biarkan Tetap)":
        genre = None
    else:
        genre = pilih_genre

    while True:
        episode = input(f"{Fore.CYAN}Episode [{dramas[judul]['episode']}]: {Style.RESET_ALL}").strip()
        if not episode:
            episode = None
            break
        if episode.isdigit():
            episode = int(episode)
            break
        print(f"{Fore.RED}Input tidak valid")

    pilih_status = inquirer.select(
        message=f"Status [{dramas[judul]['status']}]",
        choices=["(Biarkan Tetap)", "Finish", "Ongoing"]
    ).execute()

    if pilih_status == "(Biarkan Tetap)":
        status = None
    else:
        status = pilih_status

    while True:
        rating = input(f"{Fore.CYAN}Rating (0.0-10) [{dramas[judul]['rating']}]: {Style.RESET_ALL}").strip()
        if not rating:
            rating = None
            break
        try:
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                break
            else:
                print(f"{Fore.RED}Input tidak valid (rating harus 0.0-10)")
        except ValueError:
            print(f"{Fore.RED}Input tidak valid")

    if genre:
        dramas[judul]['genre'] = genre
    if episode is not None:
        dramas[judul]['episode'] = episode
    if status:
        dramas[judul]['status'] = status
    if rating is not None:
        dramas[judul]['rating'] = rating

    save_dramas(dramas)
    print(f"{Fore.GREEN}Data drama berhasil diupdate!")


def delete_drama():
    dramas = load_dramas()

    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}🗑️  HAPUS DRAMA 🗑️")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")

    if not dramas:
        print(f"{Fore.RED}Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul_input = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin dihapus: {Style.RESET_ALL}").strip()
    if not judul_input:
        print(f"{Fore.RED}Input tidak valid!")
        return

    judul_ditemukan = None
    for j in dramas:
        if j.lower() == judul_input.lower():
            judul_ditemukan = j
            break

    if not judul_ditemukan:
        print(f"{Fore.RED}Drama tidak ditemukan!")
        return

    judul = judul_ditemukan
    del dramas[judul]
    save_dramas(dramas)
    users = load_users()
    for username in users:
        users[username]["watchlist"] = [d for d in users[username]["watchlist"] if d != judul]
    save_users(users)

    print(f"{Fore.GREEN}Drama berhasil dihapus!")


def read_user_watchlists():
    users = load_users()
    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}👤 WATCHLIST PENGGUNA 👤")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")
    if not users:
        print(f"{Fore.RED}Tidak ada pengguna terdaftar.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}Username", f"{Fore.CYAN}Jumlah Watchlist", f"{Fore.CYAN}Daftar Drama{Style.RESET_ALL}"]
    for username, data in users.items():
        watchlist = data["watchlist"]
        table.add_row([
            username,
            len(watchlist),
            ", ".join(watchlist) if watchlist else f"{Fore.YELLOW}Kosong{Style.RESET_ALL}"
        ])
    print(table)
