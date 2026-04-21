import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# 1. Mengatur jumlah data
jumlah_data = 100

# 2. Membuat list tanggal (100 hari terakhir sampai hari ini)
start_date = datetime.now() - timedelta(days=jumlah_data - 1)
tanggal_list = [start_date + timedelta(days=i) for i in range(jumlah_data)]

# 3. Daftar Deskripsi untuk kebutuhan NLP (AI Engineer)
deskripsi_pilihan = ["Makan Siang", "Kopi", "Bensin", "Gojek", "Jajan", "Laundry", "Listrik"]

# 4. Membuat Data dengan Pola Mingguan (Weekend lebih mahal)
nominal_list = []
for tgl in tanggal_list:
    hari_ke = tgl.weekday()  # 0=Senin, 4=Jumat, 5=Sabtu, 6=Minggu
    if hari_ke >= 4:  # Jumat, Sabtu, Minggu pengeluaran naik
        nominal = np.random.randint(150000, 350000)
    else:
        nominal = np.random.randint(20000, 80000)
    nominal_list.append(nominal)

# 5. Membuat DataFrame (Tabel)
df = pd.DataFrame({
    'Tanggal': [t.strftime('%Y-%m-%d') for t in tanggal_list],
    'Deskripsi': [np.random.choice(deskripsi_pilihan) for _ in range(jumlah_data)],
    'Nominal': nominal_list
})

# 6. PENYELAMAT: Menyimpan di folder yang sama dengan skrip ini
# Kode ini akan memastikan file disimpan di tempat kamu berada sekarang
nama_file = "transaksi_history.csv"
df.to_csv(nama_file, index=False)

print("-" * 30)
print(f"BERHASIL!")
print(f"File '{nama_file}' telah dibuat dengan {len(df)} baris.")
print(f"Lokasi file: {os.getcwd()}")
print("-" * 30)