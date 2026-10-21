import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="TEPAK Neraca - BPS Sumut", page_icon="🏛️", layout="centered")

# Header & Deskripsi
st.markdown("<h1 style='text-align: center; color: #F26522;'>🏛️ TEPAK Neraca</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; margin-bottom: 30px;'>Tautan Eksplorasi & Portal Analitik Komprehensif Tim Neraca BPS Provinsi Sumatera Utara</p>", unsafe_allow_html=True)

# KATEGORI 1: Perdagangan & Ekspor-Impor
st.subheader("📦 Perdagangan & Ekspor-Impor")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("📊 Dasbor PAB", "https://fhrzrnd-pab-sumut.share.connect.posit.cloud/", use_container_width=True)
with col2:
    st.link_button("🚢 Eksim LN Provinsi", "https://fhrzrnd-eximln.share.connect.posit.cloud/", use_container_width=True)
with col3:
    st.link_button("📍 Eksim LN Kab/Kota", "https://nerpro-eximln-kako.share.connect.posit.cloud/", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True) # Jarak antar seksi

# KATEGORI 2: Makroekonomi & Investasi
st.subheader("📈 Makroekonomi & Investasi")
col4, col5, col6 = st.columns(3)
with col4:
    st.link_button("💰 Investasi BKPM", "https://investasi-sumut.streamlit.app/", use_container_width=True)
with col5:
    st.link_button("🏷️ Harga SHPED", "https://nerpro-harga-shped.share.connect.posit.cloud/", use_container_width=True)
with col6:
    st.link_button("🔄 Analisis IO", "https://nerpro-io-sumut-2016.share.connect.posit.cloud/", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# KATEGORI 3: Analitik Big Data & Manajemen
st.subheader("🌐 Analitik & Manajemen Tim")
col7, col8, col9 = st.columns(3)
with col7:
    st.link_button("📰 Sentimen Berita", "https://dashboard-berita-sumut.streamlit.app/", use_container_width=True)
with col8:
    st.link_button("📝 Kompilasi Fenomena", "https://script.google.com/macros/s/AKfycbzwHxcHfaqMcFCWAjBQONnyjssEPUYF2GIpnjmRrJjlNSUQJ1ZwluPjPcdAreaSEUQD/exec?authuser=0", use_container_width=True)
with col9:
    st.link_button("👥 Aktivitas Neraca", "https://sites.google.com/view/aktivitas-neraca1200", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# KATEGORI 4: Ambil Data Siasati Transportasi
st.subheader("🕷️ Ambil Data SIASATI Kemenhub")
col10, col11 = st.columns(2)
with col10:
    st.link_button("🌐 Scraping Umum", "https://siasati-terpadu-sumut.streamlit.app/", use_container_width=True)
with col11:
    st.link_button("⛴️ Scraping ASDP", "https://siasati-asdp-sumut.streamlit.app/", use_container_width=True)

st.divider()
st.markdown("<p style='text-align: center; font-size: 13px; color: #888;'>© 2026 Tim Neraca BPS Provinsi Sumatera Utara</p>", unsafe_allow_html=True)
