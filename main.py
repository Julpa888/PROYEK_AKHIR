from colorama import Fore, Style
from autentikasi import registrasi, login
from admin_menu import (
    read_drama, create_drama, update_drama, delete_drama,
    read_user_watchlists, search_drama_menu
)
from user_menu import (
    create_watchlist, read_watchlist, remove_watchlist, search_drama_user
)
from storage import load_users

ungu = Fore.MAGENTA

def menu_admin(username):
    while True:
        print("\n" + "="*60)
        print(f"SELAMAT DATANG, ADMIN {username.upper()}!")
        print("="*60)
        print("1. Lihat Semua Drama")
        print("2. Tambah Drama Baru")
        print("3. Update Data Drama")
        print("4. Hapus Drama")
        print("5. Lihat Watchlist Pengguna")
        print("6. Cari Drama")
        print("7. Logout")

        opsi = input("\nPilih menu (1-7): ").strip()
        if opsi == '1':
            read_drama()
        elif opsi == '2':
            create_drama()
        elif opsi == '3':
            update_drama()
        elif opsi == '4':
            delete_drama()
        elif opsi == '5':
            read_user_watchlists()
        elif opsi == '6':
            search_drama_menu()
        elif opsi == '7':
            print("Terima kasih, Admin!")
            return
        else:
            print("Pilihan tidak valid!")

def menu_user(username):
    while True:
        print("\n" + "="*60)
        print(f"SELAMAT DATANG, {username.upper()}!")
        print("="*60)
        print("1. Lihat Semua Drama Korea")
        print("2. Tambah ke Watchlist")
        print("3. Lihat Watchlist Saya")
        print("4. Hapus dari Watchlist")
        print("5. Cari Drama")
        print("6. Logout")

        opsi = input("\nPilih menu (1-6): ").strip()

        if opsi == '1':
            read_drama()
        elif opsi == '2':
            create_watchlist(username)
        elif opsi == '3':
            read_watchlist(username)
        elif opsi == '4':
            remove_watchlist(username)
        elif opsi == '5':
            search_drama_user()
        elif opsi == '6':
            print("Sampai jumpa!")
            return
        else:
            print("Pilihan tidak valid!")

def menu_awal():
    print(f"{ungu}"
        "\n======================================================================\n"
        "|      WELCOME TO K-BLACKLIST: PLATFORM STREAMING DRAMA KOREA!      |\n"
        "======================================================================\n"
        f"{Style.RESET_ALL}"
    )
    print("1. Registrasi")
    print("2. Login")
    print("3. Lihat sebagai tamu")
    print("4. Keluar")
    opsi = input("Silahkan pilih opsi: ").strip()
    return opsi

def main():
    while True:
        opsi = menu_awal()
        if opsi == "1":
            registrasi()
            continue
        elif opsi == "2":
            username_isadmin = login()
            if username_isadmin is None:
                continue
            username, is_admin = username_isadmin
            if is_admin:
                menu_admin(username)
            else:
                menu_user(username)
        elif opsi == "3":
            print("Anda login sebagai tamu!")
            read_drama()
            continue
        elif opsi == "4":
            exit()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
