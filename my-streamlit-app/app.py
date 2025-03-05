import streamlit as st

# ========================= 🔥 KONFIGURASI HALAMAN UTAMA ========================= #
st.set_page_config(page_title="Kuesioner Analitik", layout="wide")

# HEADER INTERAKTIF
st.markdown("<h1 style='text-align: center; color: #FF5733;'>📊 Aplikasi Analisis Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Silakan navigasi ke halaman lain dari sidebar atau tombol di bawah.</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 NAVIGASI VIA SIDEBAR ========================= #
st.sidebar.title("🔍 Navigasi Aplikasi")

# Gunakan st.page_link() untuk navigasi yang lebih aman
st.sidebar.page_link("pages/home", label="🏠 Home")
st.sidebar.page_link("pages/form", label="📝 Isi Form")
st.sidebar.page_link("pages/dashboard", label="📊 Dashboard")

st.sidebar.markdown("---")
st.sidebar.success("📍 Pilih halaman di sidebar untuk mulai eksplorasi!")

# ========================= 🔥 NAVIGASI KE HALAMAN LAIN (DENGAN TOMBOL) ========================= #
st.subheader("🔍 Ayo Mulai Analisis!")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Isi Form Kuesioner"):
        st.switch_page("form")  # ✅ Pastikan nama file ada di folder `pages/`

with col2:
    if st.button("📊 Lihat Dashboard Analitik"):
        st.switch_page("dashboard")  # ✅ Pastikan nama file ada di folder `pages/`

st.markdown("---")

# ========================= 🔥 FOOTER ========================= #
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Dibangun oleh Lammy Tutur Miaw</h5>", unsafe_allow_html=True)
