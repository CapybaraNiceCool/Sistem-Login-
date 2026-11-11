import os
import hashlib

FILE = "akun.txt"


def hash_password(password):
    # Menggunakan SHA-256 untuk hashing password
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def buat_akun_default():
    if not os.path.exists(FILE):
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(f"admin,{hash_password('admin123')}\n")


def baca_akun():
    akun = {}
    if not os.path.exists(FILE):
        return akun

    with open(FILE, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            if "," not in baris:
                continue
            username, password_hash = baris.split(",", 1)
            akun[username] = password_hash
    return akun


def simpan_akun(akun):
    with open(FILE, "w", encoding="utf-8") as f:
        for username, password_hash in akun.items():
            f.write(f"{username},{password_hash}\n")


buat_akun_default()

while True:
    print("\n1. Daftar")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        akun = baca_akun()
        username_baru = input("Masukkan username baru: ")
        if username_baru in akun:
            print("Username sudah digunakan. Silakan pilih username lain.")
        else:
            password_baru = input("Masukkan password baru: ")
            akun[username_baru] = hash_password(password_baru)
            simpan_akun(akun)
            print("Akun berhasil dibuat!")

    elif pilihan == "2":
        akun = baca_akun()
        kesempatan = 3
        while kesempatan > 0:
            username_login = input("Masukkan username: ")
            password_login = input("Masukkan password: ")

            password_hash = hash_password(password_login)
            if username_login in akun and akun[username_login] == password_hash:
                print("Login berhasil! Selamat datang,", username_login)

                while True:
                    print("\n--- Menu Utama ---")
                    print("1. Lihat daftar akun")
                    print("2. Logout")
                    menu = input("Pilih menu: ")

                    if menu == "1":
                        print("\nDaftar akun:")
                        for nama in baca_akun():
                            print("-", nama)
                    elif menu == "2":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
                break
            else:
                kesempatan -= 1
                print(f"Username atau password salah. Kesempatan tersisa: {kesempatan}")

        if kesempatan == 0:
            print("Kesempatan login habis. Kembali ke menu.")

    elif pilihan == "3":
        print("Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid.")
    

    



































































