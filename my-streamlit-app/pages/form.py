import streamlit as st
import pandas as pd
import numpy as np
import os

# ========================= 🔥 SETUP HALAMAN FORM ========================= #
st.set_page_config(page_title="Form Kuesioner", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>📝 Form Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Silakan isi kuesioner berikut untuk analisis data</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 FORM INPUT ========================= #
st.subheader("📋 Silakan Isi Data Anda")

# Input Form
usia = st.number_input("Usia", min_value=18, max_value=100, step=1)
penghasilan = st.number_input("Penghasilan (USD)", min_value=1000, max_value=100000, step=500)
rating = st.slider("Rating Pelayanan (1 - 5)", min_value=1, max_value=5, step=1)
review = st.text_area("Review Singkat tentang Layanan")
frekuensi = st.slider("Frekuensi Belanja dalam Sebulan", min_value=1, max_value=30, step=1)
jenis_kelamin = st.radio("Jenis Kelamin", ["Pria", "Wanita"])

# ========================= 🔥 DATA HANDLING ========================= #
data_file = "data/sample_data.csv"

# Fungsi untuk menyimpan data baru
def save_data(usia, penghasilan, rating, review, frekuensi, jenis_kelamin):
    new_data = pd.DataFrame([{
        "Usia": usia,
        "Penghasilan": penghasilan,
        "Rating": rating,
        "Review": review,
        "Frekuensi": frekuensi,
        "Jenis_Kelamin": jenis_kelamin
    }])
    
    if os.path.exists(data_file):
        existing_data = pd.read_csv(data_file)
        df = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(data_file, index=False)
    return df

# ========================= 🔥 TOMBOL SIMPAN ========================= #
if st.button("💾 Simpan Data"):
    if usia and penghasilan and review:
        df = save_data(usia, penghasilan, rating, review, frekuensi, jenis_kelamin)
        st.success("✅ Data berhasil disimpan!")
        st.dataframe(df.tail(5))  # Tampilkan 5 data terbaru
    else:
        st.error("⚠️ Harap isi semua data sebelum menyimpan!")

st.markdown("---")

# ========================= 🔥 NAVIGASI ========================= #
st.subheader("🔍 Lanjutkan ke Analisis Data")
st.markdown("**Setelah mengisi kuesioner, lanjutkan ke halaman dashboard untuk melihat hasil analisis.**")

if st.button("📊 Lihat Dashboard Analitik"):
    st.switch_page("dashboard")  # ✅ PERBAIKAN: Hanya gunakan nama file tanpa ekstensi dan tanpa "pages/"

st.markdown("---")

# FOOTER
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Created by Lammy Tutur Miaw</h5>", unsafe_allow_html=True)
