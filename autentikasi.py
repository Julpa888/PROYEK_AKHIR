feat/autentikasi
def login():
    print("selamat datang ")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    return username 


login()
import json
import pwinput
from storage import Storage

def registrasi():
    storage = Storage()
    users = storage.load_users()
    admin = storage.load_admin()
    print("\n=== REGISTRASI AKUN ===")
    while True:
        username = input("Masukkan username baru: ").strip()
        if username in users or username in admin:
            print("Username sudah terdaftar, coba lagi!")
            continue
        password = pwinput.pwinput("Masukkan password: ")
        users[username] = {"password": password, "watchlist": []}
        storage.save_users(users)
        print("Registrasi berhasil! Silakan login.")
        break

def login():
    storage = Storage()
    users = storage.load_users()
    admin = storage.load_admin()
    print("\n=== LOGIN SISTEM ===")
    while True:
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ")
        if username in admin and password == admin[username]:
            print("Login berhasil sebagai ADMIN!")
            return username, True
        if username in users and password == users[username]["password"]:
            print("Login berhasil sebagai USER!")
            return username, False
        print("Input data akun tidak valid! Coba lagi...\n")

# testing
main
