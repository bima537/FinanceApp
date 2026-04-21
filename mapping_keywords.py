import pandas as pd

# 1. Load data mentah kamu
df = pd.read_csv('transaksi_history_1tahun.csv')

# 2. Definisikan Fungsi Mapping
def mapping_kategori(deskripsi):
    # Ubah teks jadi huruf kecil agar pencarian lebih akurat
    text = str(deskripsi).lower()
    
    # Aturan Kata Kunci (Keywords)
    if any(key in text for key in ['makan', 'kopi', 'jajan', 'warung', 'restoran']):
        return 'Konsumsi'
    elif any(key in text for key in ['gojek', 'grab', 'bensin', 'parkir', 'transport']):
        return 'Transportasi'
    elif any(key in text for key in ['listrik', 'wifi', 'paket data', 'kos', 'laundry', 'tagihan']):
        return 'Tagihan & Kebutuhan'
    elif any(key in text for key in ['nonton', 'bioskop', 'mall', 'netflix', 'hiburan']):
        return 'Gaya Hidup'
    elif any(key in text for key in ['gaji', 'bonus', 'transfer masuk', 'cashback']):
        return 'Pendapatan'
    else:
        return 'Lain-lain'

# 3. Terapkan Mapping ke Kolom Deskripsi
df['Kategori_Otomatis'] = df['Deskripsi'].apply(mapping_kategori)

# 4. Simpan hasil mapping untuk diserahkan ke AI Engineer
df.to_csv('data_siap_nlp.csv', index=False)

print("--- TUGAS MAPPING KEYWORDS SELESAI ---")
print(df[['Deskripsi', 'Kategori_Otomatis']].head(10))