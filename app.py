import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Prediksi Pengeluaran",
    page_icon="💰",
    layout="wide"
)

# CSS sederhana
st.markdown("""
<style>
    .title {
        color: #2E86C1;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #566573;
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .card {
        background-color: #F8F9F9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86C1;
        margin: 10px 0;
    }
    .pred-box {
        background-color: #2E86C1;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">💰 PREDIKSI PENGELUARAN</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Berdasarkan Data Bulanan Sebelumnya</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Pengaturan")
    
    # Input data manual atau upload
    data_option = st.radio("Pilih Sumber Data:", ["Input Manual", "Upload CSV"])
    
    if data_option == "Upload CSV":
        uploaded_file = st.file_uploader("Pilih file CSV", type="csv")
        if uploaded_file:
            st.success("File berhasil diupload!")
    
    # Jumlah bulan prediksi
    bulan_prediksi = st.slider("Jumlah Bulan Prediksi:", 1, 6, 3)
    
    st.info("📌 Format CSV: Tanggal, Pengeluaran")
    st.info("📌 Contoh: 2024-01-01, 5000000")

# Fungsi bikin data contoh
def buat_data_contoh():
    np.random.seed(42)
    tanggal = pd.date_range(start="2024-01-01", end="2024-12-01", freq='M')
    pengeluaran = np.random.randint(3000000, 10000000, size=len(tanggal))
    # Bikin trend naik
    pengeluaran = pengeluaran + np.linspace(0, 2000000, len(tanggal))
    return pd.DataFrame({
        'Tanggal': tanggal,
        'Pengeluaran': pengeluaran.astype(int)
    })

# Load data
if data_option == "Input Manual":
    df = buat_data_contoh()
    st.sidebar.success("📊 Menggunakan data contoh")
else:
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.columns = ['Tanggal', 'Pengeluaran']  # Asumsi kolom
            df['Tanggal'] = pd.to_datetime(df['Tanggal'])
            st.sidebar.success("✅ Data loaded")
        except:
            st.sidebar.error("❌ Format salah. Pakai data contoh")
            df = buat_data_contoh()
    else:
        df = buat_data_contoh()
        st.sidear.warning("📁 Upload file atau gunakan data contoh")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🔮 Prediksi", "📋 Data"])

with tab1:
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total = df['Pengeluaran'].sum()
        st.metric("Total Pengeluaran", f"Rp {total:,.0f}")
    
    with col2:
        rata = df['Pengeluaran'].mean()
        st.metric("Rata-rata per Bulan", f"Rp {rata:,.0f}")
    
    with col3:
        max_val = df['Pengeluaran'].max()
        st.metric("Tertinggi", f"Rp {max_val:,.0f}")
    
    with col4:
        min_val = df['Pengeluaran'].min()
        st.metric("Terendah", f"Rp {min_val:,.0f}")
    
    # Chart
    st.subheader("📈 Grafik Pengeluaran Bulanan")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['Tanggal'], df['Pengeluaran'], marker='o', linewidth=2, color='#2E86C1')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Pengeluaran (Rp)')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with tab2:
    st.subheader("🔮 Hasil Prediksi")
    
    # Simple linear regression manual
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['Pengeluaran'].values
    
    # Hitung slope dan intercept manual
    x_mean = X.mean()
    y_mean = y.mean()
    
    numerator = np.sum((X.flatten() - x_mean) * (y - y_mean))
    denominator = np.sum((X.flatten() - x_mean) ** 2)
    
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    # Prediksi
    last_idx = len(df)
    pred_idx = np.arange(last_idx, last_idx + bulan_prediksi)
    predictions = intercept + slope * pred_idx
    
    # Generate tanggal prediksi
    last_date = df['Tanggal'].iloc[-1]
    pred_dates = [last_date + timedelta(days=30*i) for i in range(1, bulan_prediksi+1)]
    
    # Tampilkan prediksi dalam card
    cols = st.columns(bulan_prediksi)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class="pred-box">
                Bulan {i+1}<br>
                Rp {predictions[i]:,.0f}<br>
                <small>{pred_dates[i].strftime('%B %Y')}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Grafik historis + prediksi
    st.subheader("📈 Grafik Historis dan Prediksi")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    
    # Data historis
    ax2.plot(df['Tanggal'], df['Pengeluaran'], 'o-', label='Data Historis', color='#2E86C1')
    
    # Data prediksi
    ax2.plot(pred_dates, predictions, 'o--', label='Prediksi', color='#E74C3C')
    
    ax2.set_xlabel('Bulan')
    ax2.set_ylabel('Pengeluaran (Rp)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)
    
    # Tabel prediksi
    st.subheader("📋 Detail Prediksi")
    pred_df = pd.DataFrame({
        'Bulan': [d.strftime('%B %Y') for d in pred_dates],
        'Prediksi': [f"Rp {x:,.0f}" for x in predictions]
    })
    st.table(pred_df)

with tab3:
    st.subheader("📋 Data Pengeluaran Historis")
    
    # Tampilkan data
    st.dataframe(df.style.format({'Pengeluaran': 'Rp {:,.0f}'}))
    
    # Statistik sederhana
    st.subheader("📊 Statistik")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Info Dataset:**")
        st.write(f"- Jumlah data: {len(df)} bulan")
        st.write(f"- Periode: {df['Tanggal'].min().strftime('%B %Y')} - {df['Tanggal'].max().strftime('%B %Y')}")
        st.write(f"- Total pengeluaran: Rp {df['Pengeluaran'].sum():,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Analisis Sederhana:**")
        
        trend = "Naik" if df['Pengeluaran'].iloc[-1] > df['Pengeluaran'].iloc[0] else "Turun"
        st.write(f"- Trend: {trend}")
        
        perubahan = ((df['Pengeluaran'].iloc[-1] / df['Pengeluaran'].iloc[0]) - 1) * 100
        st.write(f"- Perubahan: {perubahan:.1f}%")
        
        # Prediksi untuk bulan depan
        st.write(f"- Estimasi bulan depan: Rp {predictions[0]:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

# Download data
st.sidebar.markdown("---")
if st.sidebar.button("📥 Download Data Contoh"):
    df.to_csv("data_pengeluaran_contoh.csv", index=False)
    st.sidebar.success("File siap di download!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 - Aplikasi Prediksi Pengeluaran Sederhana</p>", unsafe_allow_html=True)