import pandas as pd

# 1. Load data bersih (yang masih ada kolom Title)
df = pd.read_csv('transaksi_bersih.csv')

# 2. Buat Kamus Kata Kunci (Mapping Dictionary)
# Kamu bisa tambah kata-kata lain di sini sesuai kebutuhan Desa Manumutin
keywords = {
    'makan & minum': ['nasi', 'warung', 'kopi', 'gofood', 'restoran', 'makan'],
    'tagihan': ['listrik', 'pln', 'internet', 'pulsa', 'iuran', 'pajak', 'wifi'],
    'belanja': ['alfamart', 'indomaret', 'pasar', 'tissue', 'sabun', 'belanja'],
    'hiburan': ['bioskop', 'netflix', 'streaming', 'game', 'wisata'],
    'transportasi': ['bensin', 'parkir', 'ojek', 'grab', 'gojek']
}

# 3. Fungsi untuk mengecek kata kunci
def mapping_kategori(title):
    title = str(title).lower() # Kecilkan semua huruf agar cocok
    for kategori, kata_kunci in keywords.items():
        for kata in kata_kunci:
            if kata in title:
                return kategori
    return 'lain-lain' # Jika tetap tidak ketemu

# 4. Terapkan Mapping hanya pada data yang kategorinya masih 'uncategorized' atau 'lain-lain'
# Kita perbaiki kategori berdasarkan kolom 'Title'
df.loc[df['Category'] == 'uncategorized', 'Category'] = df['Title'].apply(mapping_kategori)

# 5. Lihat hasilnya
print("--- HASIL SETELAH MAPPING ---")
print(df.groupby('Category')['Amount'].count())

# 6. Simpan hasil final
df.to_csv('data_final_mapped.csv', index=False)
print("\nFile 'data_final_mapped.csv' siap digunakan untuk Dashboard!")