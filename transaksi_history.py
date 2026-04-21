import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Pengaturan Waktu (1 Tahun = 365 Hari)
jumlah_hari = 365
start_date = datetime.now() - timedelta(days=jumlah_hari - 1)
tanggal_list = [start_date + timedelta(days=i) for i in range(jumlah_hari)]

data_final = []

for tgl in tanggal_list:
    tgl_str = tgl.strftime('%Y-%m-%d')
    
    # --- A. PEMASUKAN (INCOME) ---
    # Gaji Bulanan (Setiap Tanggal 1)
    if tgl.day == 1:
        data_final.append({
            'Tanggal': tgl_str, 'Deskripsi': 'Gaji Bulanan',
            'Nominal': 8000000, 'Tipe': 'Pemasukan', 'Kategori': 'Pendapatan'
        })
    
    # Bonus Tahunan (Misal di bulan Desember atau Juni)
    if tgl.month == 12 and tgl.day == 20:
        data_final.append({
            'Tanggal': tgl_str, 'Deskripsi': 'Bonus Akhir Tahun',
            'Nominal': 4000000, 'Tipe': 'Pemasukan', 'Kategori': 'Pendapatan'
        })

    # --- B. PENGELUARAN (EXPENSE) ---
    # 1. Makan & Kebutuhan Harian (Hampir setiap hari)
    data_final.append({
        'Tanggal': tgl_str, 'Deskripsi': np.random.choice(['Makan', 'Gojek', 'Kopi']),
        'Nominal': np.random.randint(40000, 90000),
        'Tipe': 'Pengeluaran', 'Kategori': 'Kebutuhan Harian'
    })

    # 2. Bensin (3 hari sekali)
    if tgl.day % 3 == 0:
        data_final.append({
            'Tanggal': tgl_str, 'Deskripsi': 'Bensin',
            'Nominal': 50000, 'Tipe': 'Pengeluaran', 'Kategori': 'Transportasi'
        })

    # 3. Weekend Seru (Sabtu/Minggu)
    if tgl.weekday() >= 5:
        data_final.append({
            'Tanggal': tgl_str, 'Deskripsi': 'Hiburan Weekend',
            'Nominal': np.random.randint(200000, 500000),
            'Tipe': 'Pengeluaran', 'Kategori': 'Gaya Hidup'
        })

    # 4. Tagihan Flat (Listrik, Wifi, Kos)
    if tgl.day == 5:
        data_final.append({
            'Tanggal': tgl_str, 'Deskripsi': 'Tagihan Rutin Bulanan',
            'Nominal': 1500000, 'Tipe': 'Pengeluaran', 'Kategori': 'Tagihan'
        })

# 2. Simpan ke DataFrame
df = pd.DataFrame(data_final)
df = df.sort_values(by='Tanggal')
df.to_csv('transaksi_history_1tahun.csv', index=False)

print(f"BERHASIL! Terbentuk {len(df)} baris data transaksi untuk 1 tahun.")