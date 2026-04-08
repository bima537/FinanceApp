import pandas as pd

# Baca data yang sudah dibersihkan
df = pd.read_csv('transaksi_bersih.csv')

# Buat rangkuman harian (Ini yang disukai AI Engineer)
rangkuman_ai = df.groupby('Date')['Amount'].sum().reset_index()

print("--- DATA SIAP UNTUK AI ---")
print(rangkuman_ai.head())

# Simpan untuk diberikan ke tim AI
rangkuman_ai.to_csv('data_untuk_model_ai.csv', index=False)
print("\nFile 'data_untuk_model_ai.csv' siap diberikan ke AI Engineer!")