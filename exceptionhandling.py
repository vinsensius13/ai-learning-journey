import logging
import time
from colorama import Fore, Style, init

# Setup logging ke file
logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Inisialisasi colorama untuk Windows
init(autoreset=True)

while True:
    try:
        angka = input(Fore.CYAN + "Masukkan angka (0 untuk keluar): ")
        
        if angka == "0":
            print(Fore.YELLOW + "Keluar dari program...")
            for i in range(3):
                print(Fore.YELLOW + "." * (i + 1), end="\r")
                time.sleep(0.5)
            print("\n")  # Tambah newline biar rapi
            break  # Keluar dari loop

        angka = int(angka)
        hasil = 10 / angka
        print(Fore.GREEN + f"Hasil pembagian: {hasil:.2f}")

    except ValueError:
        print(Fore.RED + "Error: Input harus berupa angka!")
        time.sleep(1)  # Delay 1 detik sebelum input ulang
    except ZeroDivisionError:
        print(Fore.RED + "Error: Tidak bisa membagi dengan nol!")
        time.sleep(1)
    except Exception as e:
        print(Fore.RED + f"Error yang tidak terduga: {e}")
        logging.error(f"Error tidak terduga: {e}")  # Simpan error ke file
        time.sleep(1)
    finally:
        if angka != 0:
            print(Style.DIM + "Coba lagi atau masukkan 0 untuk keluar.\n")
