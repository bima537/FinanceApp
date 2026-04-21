import pandas as pd

# 1. Ambil data mentah yang sudah kamu buat sebelumnya
df = pd.read_csv('transaksi_history_1tahun.csv')

# 2. Pastikan format tanggal benar
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# 3. Filter hanya yang 'Pengeluaran' saja (sesuai tugas di gambar)
df_pengeluaran = df[df['Tipe'] == 'Pengeluaran']

# 4. AGREGASI: Hitung total pengeluaran per bulan
# 'ME' adalah Month End (akhir bulan)
ringkasan_bulanan = df_pengeluaran.resample('ME', on='Tanggal')['Nominal'].sum().reset_index()

# Rapikan nama kolom
ringkasan_bulanan.columns = ['Bulan', 'Total_Pengeluaran']

# 5. SIMPAN HASILNYA
ringkasan_bulanan.to_csv('agregasi_pengeluaran_bulanan.csv', index=False)

print("--- TUGAS DATA ANALYST SELESAI ---")
print("File 'agregasi_pengeluaran_bulanan.csv' telah berhasil dibuat.")
print(ringkasan_bulanan)