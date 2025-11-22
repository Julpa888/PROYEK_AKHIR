import pwinput
from storage import load_users, save_users, load_admin

def registrasi():
    storage_users = load_users()
    admin = load_admin()
    print("\n=== REGISTRASI AKUN ===")
    while True:
        username = input("Masukkan username baru: ").strip()
        if username in storage_users or username in admin:
            print("Username sudah terdaftar, coba lagi!")
            continue
        password = pwinput.pwinput("Masukkan password: ")
        storage_users[username] = {"password": password, "watchlist": []}
        save_users(storage_users)
        print("Registrasi berhasil! Silakan login.")
        break

def login():
    storage_users = load_users()
    admin = load_admin()
    print("\n=== LOGIN SISTEM ===")
    while True:
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ")
        if username in admin and password == admin[username]:
            print("Login berhasil sebagai ADMIN!")
            return username, True
        if username in storage_users and password == storage_users[username]["password"]:
            print("Login berhasil sebagai USER!")
            return username, False
        print("Input data akun tidak valid! Coba lagi...\n")