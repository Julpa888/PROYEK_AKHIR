# K-BLACKLIST: Platform Streaming Drama Korea

Aplikasi manajemen dan streaming drama Korea berbasis CLI (Command Line Interface) dengan fitur admin panel dan user watchlist management.

## 📋 Daftar Isi

- [Fitur](#fitur)
- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Struktur Project](#struktur-project)
- [Fitur Admin](#fitur-admin)
- [Fitur User](#fitur-user)

## ✨ Fitur

### 🔐 Autentikasi
- Registrasi akun baru
- Login dengan sistem role-based (Admin/User)
- Akses tamu tanpa login

### 👑 Admin Panel
- **Lihat Semua Drama**: Menampilkan daftar lengkap semua drama Korea
- **Tambah Drama Baru**: Menambah drama dengan validasi input (rating 0.0-10, genre hanya huruf, dll)
- **Update Data Drama**: Mengubah informasi drama yang sudah ada
- **Hapus Drama**: Menghapus drama dari sistem (otomatis hapus dari watchlist semua user)
- **Lihat Watchlist Pengguna**: Melihat watchlist setiap user
- **Cari Drama**: Mencari drama berdasarkan judul atau genre

### 👤 User Features
- **Lihat Semua Drama**: Browsing drama yang tersedia
- **Tambah ke Watchlist**: Menambahkan drama favorit ke watchlist pribadi
- **Lihat Watchlist**: Melihat drama yang sudah ditambahkan
- **Hapus dari Watchlist**: Menghapus drama dari watchlist
- **Cari Drama**: Mencari drama dengan keyword

### 🎨 UI/UX Enhancements
- Warna-warni dengan `colorama` (Cyan, Magenta, Yellow, Green, Red)
- Emoji untuk setiap menu option
- Pesan error yang jelas dan informatif
- Validasi input yang komprehensif
- Fitur cancel/back di form penambahan drama

## 📦 Persyaratan

- Python 3.7+
- pip (Python Package Manager)

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/elkhuwas20/PROYEK_AKHIR.git
cd PROYEK_AKHIR
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Atau manual:
```bash
pip install colorama pwinput
```

### 3. (Opsional) Setup Virtual Environment
```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

Kemudian install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Penggunaan

### Jalankan Aplikasi
```bash
python main.py
```

### Menu Utama
Setelah menjalankan aplikasi, Anda akan melihat menu utama dengan pilihan:
1. **Registrasi** - Daftar akun baru
2. **Login** - Masuk dengan akun yang sudah terdaftar
3. **Lihat sebagai Tamu** - Lihat daftar drama tanpa login
4. **Keluar** - Keluar aplikasi

### Login Credentials (Default Admin)
Sistem telah menyediakan akun admin default. Silakan cek file `data/admin.json` untuk kredensial admin.

Contoh format:
```json
{
  "admin": "password123"
}
```

### Contoh Flow

#### Flow Admin
```
1. Pilih "Login" → Masukkan username admin & password
2. Menu Admin Panel tampil
3. Pilih opsi (1-7):
   - Lihat Semua Drama
   - Tambah Drama Baru (ketik 'cancel' untuk batalkan)
   - Update Data Drama
   - Hapus Drama
   - Lihat Watchlist Pengguna
   - Cari Drama
   - Logout
```

#### Flow User
```
1. Pilih "Registrasi" atau "Login"
2. Menu User Panel tampil
3. Pilih opsi (1-6):
   - Lihat Semua Drama Korea
   - Tambah ke Watchlist
   - Lihat Watchlist Saya
   - Hapus dari Watchlist
   - Cari Drama
   - Logout
```

## 📁 Struktur Project

```
PROYEK_AKHIR/
├── main.py                 # Entry point aplikasi
├── autentikasi.py         # Modul registrasi & login
├── admin_menu.py          # Semua fitur admin panel
├── user_menu.py           # Semua fitur user panel
├── storage.py             # Manajemen penyimpanan data (JSON)
├── data/
│   ├── admin.json         # Data admin
│   ├── users.json         # Data user & watchlist
│   └── dramas.json        # Data drama Korea
├── .gitignore             # File yang diabaikan git
├── requirements.txt       # Dependency list
└── README.md             # File dokumentasi ini
```

## 🔧 Fitur Admin

### Validasi Input
- **Judul**: Tidak boleh kosong, tidak boleh duplikat
- **Genre**: Hanya huruf (tanpa angka)
- **Episode**: Hanya angka
- **Status**: Hanya "Finish" atau "Ongoing"
- **Rating**: Hanya angka 0.0-10.0

### Fitur Cancel
Ketika menambah drama baru, user admin bisa mengetik `cancel` di field manapun untuk membatalkan operasi tanpa menyimpan data.

## 👥 Fitur User

### Watchlist Management
- User bisa menambahkan drama favorit ke watchlist pribadi
- Watchlist disimpan per user
- Ketika drama dihapus oleh admin, otomatis hilang dari watchlist semua user

### Search Feature
- Cari berdasarkan judul atau genre
- Case-insensitive search
- Notifikasi jika drama tidak ditemukan

## 📊 Data Storage

Semua data disimpan dalam format JSON di folder `data/`:

### admin.json
```json
{
  "admin_username": "password"
}
```

### users.json
```json
{
  "username": {
    "password": "encrypted_or_plaintext",
    "watchlist": ["Drama Title 1", "Drama Title 2"]
  }
}
```

### dramas.json
```json
{
  "Drama Title": {
    "genre": "Romance, Comedy",
    "episode": 16,
    "status": "Finish",
    "rating": 8.5
  }
}
```

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+** - Bahasa pemrograman utama
- **colorama** - Colorized terminal output
- **pwinput** - Secure password input (dengan fallback ke getpass)
- **PrettyTable** - Formatted table display
- **JSON** - Data storage format

## 🔒 Security Notes

- Password disimpan secara plaintext (untuk development only)
- Untuk production, gunakan hashing (bcrypt, werkzeug.security, dll)
- Input validation sudah diimplementasikan
- Error handling komprehensif

## 📝 Error Handling

Aplikasi memiliki error handling untuk:
- Input kosong
- Input format invalid
- Duplikasi data
- File not found
- Module import errors (pwinput fallback)

Semua error ditampilkan dengan pesan yang jelas dan emoji 🔴 untuk user experience yang baik.

## 🐛 Troubleshooting

### Error: ModuleNotFoundError: No module named 'colorama'
```bash
pip install colorama
```

### Error: ModuleNotFoundError: No module named 'pwinput'
```bash
pip install pwinput
```
(Aplikasi memiliki fallback ke `getpass` jika pwinput tidak tersedia)

### Error: Data file not found
Pastikan folder `data/` dan file JSON sudah ada. Jalankan aplikasi sekali untuk membuat struktur awal.

## 🎓 Project Info

- **Nama Project**: K-Blacklist: Platform Streaming Drama Korea
- **Tipe**: Praktikum APD (Algortima & Pemrograman Data)
- **Status**: Under Development (feat/menu-admin branch)
- **Repository**: https://github.com/elkhuwas20/PROYEK_AKHIR

## 🤝 Kontribusi

Untuk kontribusi:
1. Fork repository
2. Buat branch fitur (`git checkout -b feature/NamaFitur`)
3. Commit changes (`git commit -m 'Add: Deskripsi fitur'`)
4. Push ke branch (`git push origin feature/NamaFitur`)
5. Open Pull Request

## 📄 Lisensi

Project ini bersifat open-source untuk keperluan pembelajaran.

## 📞 Kontak

- GitHub: [@elkhuwas20](https://github.com/elkhuwas20)

---

**Selamat menggunakan K-Blacklist! 🎬📺**
