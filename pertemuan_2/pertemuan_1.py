import streamlit as st

st.set_page_config(page_title="CV App", page_icon="😎", layout="wide")


st.sidebar.title("⚙️ Pengaturan Profile")
st.sidebar.write("Masukkan data diri anda di bawah ini:")


nama = st.sidebar.text_input("Nama:", "Nama Lengkap")
nim = st.sidebar.text_input("NIM:", "NIM Anda")
jurusan = st.sidebar.selectbox("Jurusan:", ["Teknik Informatika", "Sistem Informasi", "Teknik Elektro", "Teknik Mesin"])
deskripsi = st.sidebar.text_area("Deskripsi Diri:", "Tuliskan deskripsi singkat tentang diri anda di sini.")


st.sidebar.markdown("---")
st.sidebar.subheader("📌 Tambahan Informasi")
organisasi = st.sidebar.text_area("Pengalaman Organisasi:", "• Ketua Himpunan Mahasiswa (2023)\n• Anggota Divisi BEM (2022)")
sertifikat = st.sidebar.text_area("Sertifikat:", "• Sertifikat Python Basic (2023)\n• Sertifikat Web Development (2024)")



st.title("Curriculum Vitae")
st.markdown("---")

kolom_kiri, kolom_kanan = st.columns([1, 2])

with kolom_kiri:
    st.image("niamfotoweb.jpeg", width=180)
    st.header(nama)
    st.caption(f"**{jurusan}** | NIM: {nim}")

with kolom_kanan:
    st.subheader("👨‍💼 Tentang Saya")
    st.write(deskripsi)
    
    st.markdown("---")
    
  
    st.subheader("🏛️ Pengalaman Organisasi")
    st.write(organisasi)
    
    st.markdown("---")
    
  
    st.subheader("📜 Sertifikat")
    st.write(sertifikat)