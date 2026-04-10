import pandas as pd

# 1. Load Data Final
df = pd.read_csv('data_final_mapped.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. FILTER: Hanya Pengeluaran (EXPENSE)
df_expense = df[df['Type'] == 'EXPENSE'].copy()

# 3. TAMBAHKAN KOLOM BULAN (Untuk pengelompokan per bulan)
# Kita buat format YYYY-MM agar urutan bulannya benar
df_expense['Month'] = df_expense['Date'].dt.to_period('M')

# 4. PROSES AGREGASI PER BULAN (Sesuai Perintah)
agregasi_bulanan = df_expense.groupby('Month')['Amount'].agg(['sum', 'count', 'mean']).reset_index()

# Rapikan tampilan angka
agregasi_bulanan['sum'] = agregasi_bulanan['sum'].apply(lambda x: f"Rp {x:,.0f}")
agregasi_bulanan['mean'] = agregasi_bulanan['mean'].apply(lambda x: f"Rp {x:,.0f}")

# 5. Menampilkan Hasil
print("--- RINGKASAN PENGELUARAN PER BULAN (6 BULAN) ---")
print(agregasi_bulanan)

# 6. Simpan untuk kebutuhan laporan/dashboard
agregasi_bulanan.to_csv('pengeluaran_per_bulan.csv', index=False)