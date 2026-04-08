import pandas as pd

# 1. Membuat data sederhana
data = {
    'Nama_Produk': ['Kain Tenun', 'Kopi Manumutin', 'Madu Hutan'],
    'Harga': [500000, 25000, 80000]
}

# 2. Mengubah jadi tabel (DataFrame)
df = pd.DataFrame(data)

# 3. Menampilkan di layar hitam (Terminal)
print("--- Tes Berhasil! Ini datanya: ---")
print(df)

# 4. Menyimpan ke file CSV (tanpa folder data/)
df.to_csv("hasil_tes.csv", index=False)
print("\nFile 'hasil_tes.csv' sudah muncul di folder sebelah kiri!")