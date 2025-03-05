import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import h3
from textblob import TextBlob
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.fft import fft
from qiskit import QuantumCircuit, Aer, assemble, execute
import xgboost as xgb
import tensorflow as tf
from fpdf import FPDF
import os

# ========================= 🔥 SETUP HALAMAN DASHBOARD ========================= #
st.set_page_config(page_title="Dashboard Analitik", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>📊 Dashboard Analitik Kuesioner</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33FFBD;'>Visualisasi dan Analisis Data</h3>", unsafe_allow_html=True)

st.markdown("---")

# ========================= 🔥 LOAD DATA ========================= #
data_file = "my-streamlit-app/data/Sample_Data_Kuesioner__1000_Data_.csv"
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    st.success("✅ Data terbaru telah dimuat!")
else:
    st.warning("⚠️ Belum ada data! Silakan isi kuesioner di halaman Form.")

# ========================= 🔥 ANALISIS STATISTIK ========================= #
if not df.empty:
    st.subheader("📌 Statistik Deskriptif")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="📊 Jumlah Responden", value=len(df))

    with col2:
        st.metric(label="💰 Rata-rata Penghasilan", value=f"${df['Penghasilan'].mean():,.2f}")

    with col3:
        st.metric(label="⭐ Rata-rata Rating", value=f"{df['Rating'].mean():.2f} / 5.0")

    with col4:
        st.metric(label="🛍️ Frekuensi Belanja", value=f"{df['Frekuensi'].mean():.1f} kali/bulan")

    st.markdown("---")

    # ========================= 🔥 VISUALISASI INTERAKTIF ========================= #
    st.subheader("📊 Distribusi Data Responden")

    fig1 = px.histogram(df, x="Usia", title="Distribusi Usia Responden", color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(df, y="Penghasilan", title="Distribusi Penghasilan Responden", color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.pie(df, names="Rating", title="Distribusi Rating", color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # ========================= 🔥 SENTIMEN ANALISIS ========================= #
    st.subheader("🧠 Analisis Sentimen dari Review")
    df["Sentimen"] = df["Review"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    fig4 = px.histogram(df, x="Sentimen", title="Distribusi Sentimen", color_discrete_sequence=['#19D3F3'])
    st.plotly_chart(fig4, use_container_width=True)

    # ========================= 🔥 NETWORK ANALYSIS ========================= #
    st.subheader("🌐 Network Science - Graph Centrality Analysis")
    G = nx.erdos_renyi_graph(50, 0.1)
    centrality = nx.betweenness_centrality(G)
    fig5 = px.bar(x=list(centrality.keys()), y=list(centrality.values()), title="Network Centrality")
    st.plotly_chart(fig5, use_container_width=True)

    # ========================= 🔥 GEOSPATIAL HEATMAP ========================= #
    st.subheader("🌍 Geospatial Heatmap")
    df["Latitude"] = np.random.uniform(-90, 90, len(df))
    df["Longitude"] = np.random.uniform(-180, 180, len(df))
    df["H3_Index"] = df.apply(lambda row: h3.geo_to_h3(row["Latitude"], row["Longitude"], 7), axis=1)

    fig6 = px.density_mapbox(df, lat="Latitude", lon="Longitude", z="Rating",
                             radius=10, mapbox_style="open-street-map",
                             title="Geospatial Heatmap berdasarkan Rating")
    st.plotly_chart(fig6, use_container_width=True)

    # ========================= 🔥 QUANTUM COMPUTING ========================= #
    st.subheader("⚛️ Quantum Computing Simulation")
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    simulator = Aer.get_backend('qasm_simulator')
    qobj = assemble(qc, shots=1024)
    result = execute(qc, simulator).result()
    quantum_pattern = result.get_counts()
    st.write(f"Quantum Measurement Result: {quantum_pattern}")

    st.markdown("---")

    # ========================= 🔥 GENERATE PDF REPORT ========================= #
    st.subheader("📢 Generate Report PDF")

    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="🚀 Laporan Analisis Kuesioner", ln=True, align='C')
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Rata-rata Penghasilan: ${df['Penghasilan'].mean():.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Rata-rata Usia: {df['Usia'].mean():.1f} tahun", ln=True)
        pdf.cell(200, 10, txt=f"Quantum Measurement Result: {quantum_pattern}", ln=True)

        pdf.output("Laporan_Analisis.pdf")
        st.success("✅ Laporan PDF Berhasil Dibuat! 📄")

    if st.button("Generate PDF Report"):
        generate_pdf()
        st.download_button(label="⬇️ Download Report PDF", data=open("Laporan_Analisis.pdf", "rb"), file_name="Laporan_Analisis.pdf", mime="application/pdf")

st.markdown("---")

# FOOTER
st.markdown("<h5 style='text-align: center; color: #888;'>🚀 Dibangun dengan 💙 oleh Data Science Terbaik di Muka Bumi 🌍</h5>", unsafe_allow_html=True)
