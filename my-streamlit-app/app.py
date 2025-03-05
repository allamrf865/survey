import streamlit as st

# ========================= 🔥 KONFIGURASI HALAMAN UTAMA ========================= #
st.set_page_config(page_title="Kuesioner Analitik", layout="wide")

# HEADER INTERAKTIF
st.markdown("<h1 style='text-align: center; color: #FF5733;'>📊 Aplikasi Analisis Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Silakan navigasi ke halaman lain dari sidebar atau tombol di bawah.</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 NAVIGASI VIA SIDEBAR ========================= #
st.sidebar.title("🔍 Navigasi Aplikasi")
st.sidebar.page_link("app.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/form.py", label="📝 Isi Form", icon="📝")
st.sidebar.page_link("pages/dashboard.py", label="📊 Dashboard", icon="📊")

st.sidebar.markdown("---")
st.sidebar.success("📍 Pilih halaman di sidebar untuk mulai eksplorasi!")

# ========================= 🔥 NAVIGASI KE HALAMAN LAIN (DENGAN TOMBOL) ========================= #
st.subheader("🔍 Ayo Mulai Analisis!")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Isi Form Kuesioner"):
        st.switch_page("pages/form.py")

with col2:
    if st.button("📊 Lihat Dashboard Analitik"):
        st.switch_page("pages/dashboard.py")

st.markdown("---")

# ========================= 🔥 FOOTER ========================= #
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Created by Lammy Tutur Miaw</h5>", unsafe_allow_html=True)
