import pandas as pd
import os

# Nama file yang ada di foldermu (sesuaikan jika namanya berbeda sedikit)
nama_file = 'transaksi_history.csv'

print(f"Sedang mencari file: {nama_file}...")

# Cek apakah filenya benar-benar ada di folder ini
if os.path.exists(nama_file):
    print("Ketemu! Sedang membaca data...")
    
    # Membaca data dengan pemisah titik koma (;) sesuai data yang kamu kirim tadi
    df = pd.read_csv(nama_file, sep=';')
    
    # Menampilkan 5 data teratas
    print("\n--- Data Berhasil Dibaca ---")
    print(df.head())
    
    # Cek nama kolom agar tidak KeyError lagi
    print("\nKolom yang tersedia:", df.columns.tolist())
    
else:
    print(f"\nERROR: File '{nama_file}' tidak ada di folder ini.")
    print("Isi folder kamu saat ini adalah:")
    print(os.listdir('.'))