import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import csv

# 1. PENGATURAN WAKTU (1 Tahun ke Belakang dari Hari Ini)
jumlah_hari = 365
# Kita buat mundur agar ada data historis untuk dianalisis
start_date = datetime.now() - timedelta(days=jumlah_hari - 1)
tanggal_list = [start_date + timedelta(days=i) for i in range(jumlah_hari)]

data_final = []

for tgl in tanggal_list:
    tgl_str = tgl.strftime('%Y-%m-%d')
    
    # --- A. PEMASUKAN (INCOME) ---
    # Gaji Bulanan (Setiap Tanggal 1)
    if tgl.day == 1:
        data_final.append({
            'tanggal': tgl_str, 
            'deskripsi': 'Gaji Bulanan',
            'nominal': 8000000, 
            'tipe': 'Pemasukan', 
            'kategori': 'Pendapatan'
        })
    
    # Pemasukan Tambahan (Acak, probabilitas 3% per hari)
    if np.random.random() < 0.03:
        data_final.append({
            'tanggal': tgl_str, 
            'deskripsi': 'Bonus / Cashback',
            'nominal': np.random.randint(50000, 200000),
            'tipe': 'Pemasukan', 
            'kategori': 'Pendapatan'
        })

    # --- B. PENGELUARAN (EXPENSE) ---
    # 1. Makan & Kebutuhan Harian (Pasti ada setiap hari)
    data_final.append({
        'tanggal': tgl_str, 
        'deskripsi': np.random.choice(['Makan Siang', 'Makan Malam', 'Kopi Senja']),
        'nominal': int(np.random.randint(35000, 80000)),
        'tipe': 'Pengeluaran', 
        'kategori': 'Konsumsi'
    })

    # 2. Bensin/Transportasi (Setiap 2 hari sekali)
    if tgl.day % 2 == 0:
        data_final.append({
            'tanggal': tgl_str, 
            'deskripsi': np.random.choice(['Bensin Motor', 'Gojek', 'Grab']),
            'nominal': int(np.random.randint(20000, 45000)),
            'tipe': 'Pengeluaran', 
            'kategori': 'Transportasi'
        })

    # 3. Hiburan Weekend (Sabtu & Minggu)
    if tgl.weekday() >= 5:
        data_final.append({
            'tanggal': tgl_str, 
            'deskripsi': 'Nonton / Jajan Weekend',
            'nominal': int(np.random.randint(150000, 350000)),
            'tipe': 'Pengeluaran', 
            'kategori': 'Gaya Hidup'
        })

    # 4. Tagihan Rutin (Setiap Tanggal 5)
    if tgl.day == 5:
        data_final.append({
            'tanggal': tgl_str, 
            'deskripsi': 'Listrik, Wifi, & Kos',
            'nominal': 1800000,
            'tipe': 'Pengeluaran', 
            'kategori': 'Tagihan'
        })

# 2. PROSES KE DATAFRAME & ADD ID
df = pd.DataFrame(data_final)
df = df.sort_values(by='tanggal').reset_index(drop=True)

# Tambahkan kolom ID di paling depan untuk Primary Key Supabase
df.insert(0, 'id', range(1, len(df) + 1))

# 3. SIMPAN KE CSV UNTUK SUPABASE
# Menggunakan quoting=csv.QUOTE_ALL agar aman saat di-import
df.to_csv('transaksi_history.csv', index=False, quoting=csv.QUOTE_ALL)

print(f"BERHASIL! File 'transaksi_history.csv' dibuat dengan {len(df)} baris.")
print(df.head())