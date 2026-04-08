import pandas as pd
import matplotlib.pyplot as plt

# 1. Baca data yang sudah bersih
df = pd.read_csv('transaksi_bersih.csv')
df['Date'] = pd.to_datetime(df['Date']) # Pastikan tanggal terbaca benar

# 2. TUGAS ANALIS: Menghitung Pengeluaran per Kategori
analisis_kategori = df[df['Type'] == 'EXPENSE'].groupby('Category')['Amount'].sum()

print("--- HASIL ANALISIS ---")
print(analisis_kategori)

# 3. TUGAS ANALIS: Membuat Visualisasi untuk Laporan
plt.figure(figsize=(10, 6))
analisis_kategori.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Persentase Pengeluaran per Kategori')
plt.ylabel('') # Menghilangkan label y agar rapi
plt.show()