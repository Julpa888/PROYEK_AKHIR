try:
    import pwinput
    _has_pwinput = True
except Exception:
    import getpass
    _has_pwinput = False

from storage import load_users, save_users, load_admin


def _get_password(prompt: str) -> str:
    if _has_pwinput:
        return pwinput.pwinput(prompt)
    return getpass.getpass(prompt)

def registrasi():
    storage_users = load_users()
    admin = load_admin()
    print("\n=== REGISTRASI AKUN ===")
    while True:
        username = input("Masukkan username baru: ").strip()
        if username in storage_users or username in admin:
            print("Username sudah terdaftar, coba lagi!")
            continue
        password = _get_password("Masukkan password: ")
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
        password = _get_password("Masukkan password: ")
        if username in admin and password == admin[username]:
            print("Login berhasil sebagai ADMIN!")
            return username, True
        if username in storage_users and password == storage_users[username]["password"]:
            print("Login berhasil sebagai USER!")
            return username, False
        print("Input data akun tidak valid! Coba lagi...\n")