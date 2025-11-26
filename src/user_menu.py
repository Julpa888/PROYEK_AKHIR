ori_input = input
def input(prompt=""):
    while True:
        v = ori_input(prompt)
        if v.strip() == "":         
            print("Input tidak boleh kosong!")
            continue
        if v != v.strip():         
            print("Tidak boleh ada spasi di awal atau akhir input")
            continue
        return v                    

from prettytable import PrettyTable
from colorama import Fore, Style
from admin_menu import read_drama, search_drama
from storage import load_dramas, load_users, save_users

def create_watchlist(username):
    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}➕ TAMBAH KE WATCHLIST ➕")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")

    read_drama()
    judul_input = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin ditambahkan: {Style.RESET_ALL}").strip()

    if not judul_input:
        print(f"{Fore.RED}Judul tidak boleh kosong!")
        return

    dramas = load_dramas()
    users = load_users()

    judul_ditemukan = None
    for j in dramas:
        if j.lower() == judul_input.lower():
            judul_ditemukan = j
            break

    if not judul_ditemukan:
        print(f"{Fore.RED}Drama tidak ditemukan!")
        return

    judul = judul_ditemukan

    if username not in users:
        print(f"{Fore.RED}Pengguna tidak ditemukan!")
        return

    if judul in users[username]["watchlist"]:
        print(f"{Fore.RED}Drama sudah ada di watchlist Anda!")
        return

    users[username]["watchlist"].append(judul)
    save_users(users)
    print(f"{Fore.GREEN}'{judul}' berhasil ditambahkan ke watchlist!")

def read_watchlist(username):
    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}📋 WATCHLIST SAYA 📋")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")

    users = load_users()
    dramas = load_dramas()

    if username not in users:
        print(f"{Fore.RED}Pengguna tidak ditemukan!")
        return

    watchlist = users[username]["watchlist"]

    if not watchlist:
        print(f"{Fore.YELLOW}📭 Watchlist Anda masih kosong.")
        return

    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}No", f"{Fore.CYAN}Judul", f"{Fore.CYAN}Genre", f"{Fore.CYAN}Episode", f"{Fore.CYAN}Status", f"{Fore.CYAN}Rating{Style.RESET_ALL}"]

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
    print(f"\n{Fore.RED}{'█' * 50}")
    print(f"{Fore.YELLOW}🗑️  HAPUS DARI WATCHLIST 🗑️")
    print(f"{Fore.RED}{'█' * 50}{Style.RESET_ALL}")

    read_watchlist(username)

    users = load_users()
    if username not in users:
        print(f"{Fore.RED}Pengguna tidak ditemukan!")
        return

    watchlist = users[username]["watchlist"]

    if not watchlist:
        return

    judul_input = input(f"\n{Fore.CYAN}Masukkan judul drama yang ingin dihapus: {Style.RESET_ALL}").strip()

    if not judul_input:
        print(f"{Fore.RED}Judul tidak boleh kosong!")
        return

    judul_ditemukan = None
    for j in watchlist:
        if j.lower() == judul_input.lower():
            judul_ditemukan = j
            break

    if not judul_ditemukan:
        print(f"{Fore.RED}Drama tidak ditemukan di watchlist Anda!")
        return

    watchlist.remove(judul_ditemukan)
    save_users(users)
    print(f"{Fore.GREEN}'{judul_ditemukan}' berhasil dihapus dari watchlist!")

def search_drama_user():
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
