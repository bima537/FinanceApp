import pandas as pd

# 1. Load Data Bersih
df = pd.read_csv('transaksi_bersih.csv')

# 2. PROSES AGREGASI (Sesuai Roadmap)
# a. Agregasi Harian (untuk tren waktu)
agregasi_hari = df.groupby('Date')['Amount'].sum().reset_index()

# b. Agregasi Kategori (untuk distribusi pengeluaran)
agregasi_kategori = df.groupby('Category')['Amount'].agg(['sum', 'count', 'mean']).reset_index()
# sum = total uang, count = berapa kali transaksi, mean = rata-rata sekali belanja

# 3. Menampilkan Hasil Agregasi
print("--- HASIL AGREGASI HARIAN ---")
print(agregasi_hari.head())

print("\n--- HASIL AGREGASI KATEGORI ---")
print(agregasi_kategori)

# 4. Simpan hasil agregasi untuk tahap Stage 3 (Reporting)
agregasi_hari.to_csv('data_agregasi_hari.csv', index=False)
agregasi_kategori.to_csv('data_agregasi_kategori.csv', index=False)