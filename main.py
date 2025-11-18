from autentikasi import Auth
from admin_menu import AdminManager
from user_menu import UserManager
from drama import DramaManager

def main():
    auth = Auth()
    admin_manager = AdminManager()
    user_manager = UserManager()
    drama_manager = DramaManager()
    
    while True:
        auth.display_welcome()
        print("\n" + "="*50)
        print("MENU UTAMA")
        print("="*50)
        print("1. 👤 Login")
        print("2. 📝 Registrasi")
        print("3. 👀 Lihat Drama sebagai Tamu")
        print("4. 🚪 Keluar")
        
        choice = input("\nPilih menu (1-4): ").strip()
        
        if choice == '1':
            role, username = auth.login()
            if role == "admin":
                admin_manager.menu(username)
            elif role == "user":
                user_manager.menu(username)
        
        elif choice == '2':
            auth.register()
        
        elif choice == '3':
            print("\n" + "="*50)
            print("MELIHAT DRAMA SEBAGAI TAMU")
            print("="*50)
            drama_manager.display_all_dramas()
        
        elif choice == '4':
            print("👋 Terima kasih telah menggunakan K-Blacklist!")
            break
        
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()