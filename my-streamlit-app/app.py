import streamlit as st

# ========================= 🔥 KONFIGURASI HALAMAN UTAMA ========================= #
st.set_page_config(page_title="Kuesioner Analitik", layout="wide")

# 🔥 Redirect ke Home Menggunakan Query Params (Menghindari Error)
if "redirected" not in st.session_state:
    st.session_state["redirected"] = True
    st.experimental_set_query_params(page="home")
    st.rerun()  # 🔄 Refresh halaman untuk pindah ke `home`
