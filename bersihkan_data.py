import pandas as pd

# 1. MEMBACA DATA
nama_file = 'transaksi_history.csv'
df = pd.read_csv(nama_file, sep=';')

print("--- Data Sebelum Dibersihkan ---")
print(df.head())

# 2. MEMBERSIHKAN KOLOM AMOUNT (NOMINAL)
# Kita hilangkan 'Rp', '.', dan ',00' agar menjadi angka murni
df['Amount'] = df['Amount'].str.replace('Rp', '', regex=False)
df['Amount'] = df['Amount'].str.replace('.', '', regex=False)
df['Amount'] = df['Amount'].str.replace(',00', '', regex=False)

# Mengubah tipe data ke angka (Integer)
df['Amount'] = pd.to_numeric(df['Amount'])

# 3. MEMBERSIHKAN KOLOM DATE (TANGGAL)
# Mengubah teks tanggal menjadi format yang dipahami Python (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# 4. MENANGANI DATA KOSONG
# Jika ada baris yang kosong, kita hapus agar tidak merusak analisis
df = df.dropna()

# 5. MENYERAGAMKAN TEKS (KATEGORI)
# Mengubah semua kategori jadi huruf kecil agar konsisten (misal: 'MAKANAN' jadi 'makanan')
df['Category'] = df['Category'].str.lower()

print("\n--- Data Setelah Dibersihkan ---")
print(df.head())
print("\nInfo Tipe Data Sekarang:")
print(df.dtypes)

# 6. SIMPAN HASIL BERSIH
# Kita simpan agar bisa dipakai oleh AI Engineer atau untuk dashboard
df.to_csv('transaksi_bersih.csv', index=False)
print("\nSUKSES! File 'transaksi_bersih.csv' telah disimpan.")