import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Memuat variabel dari file .env
load_dotenv()

# Mengambil API Key dari variabel lingkungan
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_research_section(section, topic, description):
    messages = [
        {"role": "system", "content": "Anda adalah AI yang membantu menulis bagian penelitian untuk berbagai bidang studi."},
        {"role": "user", "content": f"Tulislah {section} ntuk penelitian dalam topik {topic}. Penelitian ini tentang: {description}."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Menggunakan model gpt-3.5-turbo
        messages=messages,
        max_tokens=1000,  # Mengatur lebih tinggi untuk menampung teks panjang
        temperature=0.7,
    )

    # Mengembalikan hasil dari AI
    return response.choices[0].message['content'].strip()

# Judul aplikasi
st.title("Nyusun - Universitas Teknokrat Indonesia")

# Pilih bagian penelitian
section = st.selectbox(
    "Pilih Bagian Penelitian:",
    ["Pendahuluan", "Metode Penelitian", "Hasil dan Pembahasan"]
)

# Pilih topik studi/jurusan
topic = st.selectbox(
    "Pilih Topik Studi/Jurusan:",
    [
        "Sistem Informasi", "Informatika", "Teknik Komputer", "Teknologi Informasi", 
        "Teknik Sipil", "Teknik Elektro", "Manajemen", "Ekonomi", 
        "Sastra Inggris", "Pendidikan Bahasa Inggris", "Pendidikan Matematika"
    ]
)

# Input deskripsi singkat tentang studi
description = st.text_area("Masukkan Deskripsi Singkat tentang Studi:")

# Tombol untuk menghasilkan teks
if st.button("Buat Bagian Penelitian"):
    if description:
        result = generate_research_section(section, topic, description)
        
        # Menampilkan hasil yang dihasilkan oleh AI
        st.subheader(f"Bagian {section}:")
        st.write(result)
    else:
        st.error("Deskripsi singkat tentang studi harus diisi.")
st.markdown("Dibuat dengan ❤️ oleh Pusat Unggulan Kecerdasan Buatan Universitas Teknokrat Indonesia")