import streamlit as st
import pandas as pd
import os

# ========================= 🔥 KONFIGURASI HALAMAN ========================= #
st.set_page_config(page_title="Dashboard Home", layout="wide")

# CSS Styling untuk UI
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #FF5733;
            font-size: 36px;
            font-weight: bold;
        }
        .sub-title {
            text-align: center;
            color: #33FFBD;
            font-size: 20px;
        }
        .info-card {
            padding: 15px;
            border-radius: 10px;
            background-color: #f8f9fa;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 20px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# ========================= 🔥 HEADER ========================= #
st.markdown("<h1 class='main-title'>📊 Dashboard Analisis Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Dapatkan insight terbaik dari data kuesioner secara otomatis</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 NAVIGASI SIDEBAR ========================= #
st.sidebar.title("🔍 Navigasi Aplikasi")
st.sidebar.page_link("home", label="🏠 Home")
st.sidebar.page_link("form", label="📝 Isi Form")
st.sidebar.page_link("dashboard", label="📊 Dashboard")

st.sidebar.markdown("---")
st.sidebar.success("📍 Pilih halaman di sidebar untuk mulai eksplorasi!")

# ========================= 🔥 RINGKASAN DATA (STATISTIK) ========================= #
data_file = "my-streamlit-app/data/Sample_Data_Kuesioner__1000_Data_.csv"
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    st.success("✅ Data terbaru telah dimuat!")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='info-card'>📊 <br> Jumlah Responden <br><b>{}</b></div>".format(len(df)), unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='info-card'>💰 <br> Rata-rata Penghasilan <br><b>${:,.2f}</b></div>".format(df["Penghasilan"].mean()), unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='info-card'>⭐ <br> Rata-rata Rating <br><b>{:.2f} / 5.0</b></div>".format(df["Rating"].mean()), unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='info-card'>🛍️ <br> Frekuensi Belanja <br><b>{:.1f} kali/bulan</b></div>".format(df["Frekuensi"].mean()), unsafe_allow_html=True)

    st.markdown("---")

else:
    st.warning("⚠️ Data belum tersedia. Silakan isi kuesioner terlebih dahulu.")

# ========================= 🔥 NAVIGASI KE HALAMAN LAIN ========================= #
st.subheader("🔍 Ayo Mulai Analisis!")
st.markdown("**Klik tombol di bawah untuk memasukkan data kuesioner atau melihat analisis lengkap!**")

colA, colB = st.columns(2)

with colA:
    if st.button("📝 Isi Form Kuesioner"):
        st.switch_page("form")  # ✅ Tanpa "pages/"

with colB:
    if st.button("📊 Lihat Dashboard Analitik"):
        st.switch_page("dashboard")  # ✅ Tanpa "pages/"

st.markdown("---")

# ========================= 🔥 FOOTER ========================= #
st.markdown("<h5 class='footer'>🚀 Created by Lammy Tutur Miaw </h5>", unsafe_allow_html=True)
