from colorama import Fore, Style
from autentikasi import registrasi, login, login_tamu
from admin_menu import AdminManager
from user_menu import UserManager

ungu = Fore.MAGENTA
admin = AdminManager()
user = UserManager()
user = AdminManager()

def menu_admin(username):
    while True:
        print("\n" + "="*60)
        print(f"SELAMAT DATANG, ADMIN {username.upper()}!")
        print("="*60)
        print("1. Tambah Drama Baru")
        print("2. Lihat Semua Drama")
        print("3. Update Data Drama")
        print("4. Hapus Drama")
        print("5. Lihat Watchlist Pengguna")
        print("6. Cari Drama")
        print("7. Logout")

        choice = input("\nPilih menu (1-7): ").strip()
        if choice == '1':
            admin.create_drama()
        elif choice == '2':
            admin.read_drama()
        elif choice == '3':
            admin.update_drama()
        elif choice == '4':
            admin.delete_drama()
        elif choice == '5':
            admin.read_user_watchlists()
        elif choice == '6':
            admin.search_drama()
        elif choice == '7':
            print("Terima kasih, Admin!")
            menu_awal()
        else:
            print("Pilihan tidak valid!")
            return

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
            
            choice = input("\nPilih menu (1-6): ").strip()
            
            if choice == '1':
                user.read_drama()
            elif choice == '2':
                user.create_watchlist(username)
            elif choice == '3':
                user.read_watchlist(username)
            elif choice == '4':
                user.remove_watchlist(username)
            elif choice == '5':
                user.search_drama()
            elif choice == '6':
                print("Sampai jumpa!")
                menu_awal()
            else:
                print("Pilihan tidak valid!")
                return


## MENU UTAMA ##

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

menu_awal()
opsi = input("Silahkan pilih opsi: ").strip()

if opsi == "1":
    registrasi()
    username, is_admin = login()
    if is_admin:
        menu_admin(username)
    else:
        menu_user(username)

elif opsi == "2":
    username, is_admin = login()
    if is_admin:
        menu_admin(username)
    else:
        menu_user(username)

elif opsi == "3":
    print("Anda login sebagai tamu!")
    user.read_drama()
    menu_awal()

elif opsi == "4":
    exit()

else:
    print("Pilihan tidak valid.")
