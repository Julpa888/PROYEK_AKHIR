from prettytable import PrettyTable
from colorama import Fore, Style
from storage import load_dramas, save_dramas, load_users, save_users

def read_drama():
    dramas = load_dramas()
    if not dramas:
        print(f"{Fore.RED}❌ Tidak ada drama yang tersedia.")
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

    print(f"\n{Fore.MAGENTA}{'█' * 80}")
    print(f"{Fore.YELLOW}📺 DAFTAR DRAMA KOREA 📺")
    print(f"{Fore.MAGENTA}{'█' * 80}{Style.RESET_ALL}")
    print(table)

def search_drama(keyword):
    dramas = load_dramas()
    hasil = {}
    for judul, data in dramas.items():
        if keyword.lower() in judul.lower() or keyword.lower() in data['genre'].lower():
            hasil[judul] = data
    return hasil

def search_drama_menu():
    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}🔍 CARI DRAMA 🔍")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")
    keyword = input(f"{Fore.CYAN}Masukkan judul atau genre drama: {Style.RESET_ALL}").strip()
    if not keyword:
        print(f"{Fore.RED}❌ drama tidak tersedia")
        return
    results = search_drama(keyword)
    if not results:
        print(f"{Fore.RED}❌ Tidak ditemukan drama dengan kata kunci tersebut.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]
    for i, (judul, data) in enumerate(results.items(), 1):
        table.add_row([
            i,
            judul,
            data["genre"],
            data["episode"],
            data["status"],
            data["rating"]
        ])
    print(f"{Fore.GREEN}✅ Hasil pencarian untuk '{keyword}':")
    print(table)

def create_drama():
    dramas = load_dramas()

    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}➕ TAMBAH DRAMA BARU ➕")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}(Ketik 'cancel' kapan saja untuk membatalkan)\n{Style.RESET_ALL}")

    while True:
        judul = input(f"{Fore.CYAN}Judul: {Style.RESET_ALL}").strip()
        if judul.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan penambahan drama.")
            return
        if not judul:
            print(f"{Fore.RED}❌ input tidak valid")
            continue
        if judul in dramas:
            print(f"{Fore.RED}❌ Drama sudah ada dalam daftar!")
            return
        break

    while True:
        genre = input(f"{Fore.CYAN}Genre: {Style.RESET_ALL}").strip()
        if genre.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan penambahan drama.")
            return
        if genre.replace(" ", "").isalpha():
            break
        print(f"{Fore.RED}❌ input tidak valid")

    while True:
        episode = input(f"{Fore.CYAN}Jumlah Episode: {Style.RESET_ALL}").strip()
        if episode.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan penambahan drama.")
            return
        if episode.isdigit():
            episode = int(episode)
            break
        print(f"{Fore.RED}❌ input tidak valid")

    while True:
        status = input(f"{Fore.CYAN}Status (Finish/Ongoing): {Style.RESET_ALL}").strip()
        if status.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan penambahan drama.")
            return
        status = status.capitalize()
        if status in ["Finish", "Ongoing"]:
            break
        print(f"{Fore.RED}❌ input tidak valid")

    while True:
        rating = input(f"{Fore.CYAN}Rating (0.0-10): {Style.RESET_ALL}").strip()
        if rating.lower() == 'cancel':
            print(f"{Fore.YELLOW}⏹️  Pembatalan penambahan drama.")
            return
        try:
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                break
            else:
                print(f"{Fore.RED}❌ input tidak valid (rating harus 0.0-10)")
        except ValueError:
            print(f"{Fore.RED}❌ input tidak valid")

    dramas[judul] = {
        "genre": genre,
        "episode": episode,
        "status": status,
        "rating": rating
    }
    save_dramas(dramas)
    print(f"{Fore.GREEN}✅ Drama berhasil ditambahkan!")

def update_drama():
    dramas = load_dramas()

    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}✏️  UPDATE DATA DRAMA ✏️")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")

    if not dramas:
        print(f"{Fore.RED}❌ Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin diupdate: {Style.RESET_ALL}").strip()

    if judul not in dramas:
        print(f"{Fore.RED}❌ Drama tidak ditemukan!")
        return

    print(f"\n{Fore.GREEN}Data saat ini untuk '{judul}':")
    print(f"{Fore.CYAN}Genre: {dramas[judul]['genre']}")
    print(f"{Fore.CYAN}Episode: {dramas[judul]['episode']}")
    print(f"{Fore.CYAN}Status: {dramas[judul]['status']}")
    print(f"{Fore.CYAN}Rating: {dramas[judul]['rating']}{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Masukkan data baru (kosongkan jika tidak ingin mengubah):")

    while True:
        genre = input(f"{Fore.CYAN}Genre [{dramas[judul]['genre']}]: {Style.RESET_ALL}").strip()
        if not genre:
            genre = None
            break
        if genre.replace(" ", "").isalpha():
            break
        print(f"{Fore.RED}❌ input tidak valid")

    while True:
        episode = input(f"{Fore.CYAN}Episode [{dramas[judul]['episode']}]: {Style.RESET_ALL}").strip()
        if not episode:
            episode = None
            break
        if episode.isdigit():
            episode = int(episode)
            break
        print(f"{Fore.RED}❌ input tidak valid")

    while True:
        status = input(f"{Fore.CYAN}Status [{dramas[judul]['status']}]: {Style.RESET_ALL}").strip()
        if not status:
            status = None
            break
        status = status.capitalize()
        if status in ["Finish", "Ongoing"]:
            break
        print(f"{Fore.RED}❌ input tidak valid")

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
                print(f"{Fore.RED}❌ input tidak valid (rating harus 0.0-10)")
        except ValueError:
            print(f"{Fore.RED}❌ input tidak valid")

    if genre:
        dramas[judul]['genre'] = genre
    if episode is not None:
        dramas[judul]['episode'] = episode
    if status:
        dramas[judul]['status'] = status
    if rating is not None:
        dramas[judul]['rating'] = rating

    save_dramas(dramas)
    print(f"{Fore.GREEN}✅ Data drama berhasil diupdate!")

def delete_drama():
    dramas = load_dramas()

    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}🗑️  HAPUS DRAMA 🗑️")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")

    if not dramas:
        print(f"{Fore.RED}❌ Tidak ada drama yang tersedia.")
        return
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]
    for i, (judul, data) in enumerate(dramas.items(), 1):
        table.add_row([i, judul, data["genre"], data["episode"], data["status"], data["rating"]])
    print(table)

    judul = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin dihapus: {Style.RESET_ALL}").strip()

    if judul not in dramas:
        print(f"{Fore.RED}❌ Drama tidak ditemukan!")
        return
    del dramas[judul]
    save_dramas(dramas)
    users = load_users()
    for username in users:
        users[username]["watchlist"] = [d for d in users[username]["watchlist"] if d != judul]
    save_users(users)

    print(f"{Fore.GREEN}✅ Drama berhasil dihapus!")

def read_user_watchlists():
    users = load_users()
    print(f"\n{Fore.MAGENTA}{'█' * 50}")
    print(f"{Fore.YELLOW}👤 WATCHLIST PENGGUNA 👤")
    print(f"{Fore.MAGENTA}{'█' * 50}{Style.RESET_ALL}")
    if not users:
        print(f"{Fore.RED}❌ Tidak ada pengguna terdaftar.")
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
