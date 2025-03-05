import streamlit as st
import os

# ========================= 🔥 KONFIGURASI HALAMAN UTAMA ========================= #
st.set_page_config(page_title="Kuesioner Analitik", layout="wide")

# HEADER INTERAKTIF
st.markdown("<h1 style='text-align: center; color: #FF5733;'>📊 Aplikasi Analisis Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Silakan navigasi ke halaman lain dari sidebar.</h3>", unsafe_allow_html=True)

# Logo (opsional)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=200)

st.markdown("---")

# ========================= 🔥 NAVIGASI & PETUNJUK ========================= #
st.sidebar.success("📍 Pilih halaman dari sidebar untuk mulai eksplorasi!")

st.subheader("🔍 Cara Menggunakan Aplikasi:")
st.markdown("""
- **📌 Home** → Halaman utama (ringkasan analitik awal).  
- **📝 Form** → Input data kuesioner baru.  
- **📊 Dashboard** → Visualisasi lengkap hasil analisis.  
""")

st.markdown("---")

# FOOTER
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Dibangun dengan 💙 Lammy Tutur Miaw🌍</h5>", unsafe_allow_html=True)
