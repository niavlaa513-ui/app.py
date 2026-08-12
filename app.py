import streamlit as st
import pandas as pd
import io

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="E-Rapor Gen-Z Ultra Enterprise", page_icon="🚀", layout="wide")

mapel_cols = ["Matematika", "Sains & Fisika", "Bahasa Indonesia", "Bahasa Inggris", "Informatika (Coding)", "Ekonomi Digital", "Seni & Kreatif"]

# --- 2. DATABASE UTAMA (Session State) ---
if 'data_siswa' not in st.session_state:
    st.session_state.data_siswa = pd.DataFrame([
        {"Absen": 1, "Nama": "Oliver Revan", "Matematika": 88, "Sains & Fisika": 90, "Bahasa Indonesia": 82, "Bahasa Inggris": 95, "Informatika (Coding)": 98, "Ekonomi Digital": 85, "Seni & Kreatif": 78},
        {"Absen": 2, "Nama": "Zhafira Kayla", "Matematika": 75, "Sains & Fisika": 78, "Bahasa Indonesia": 92, "Bahasa Inggris": 88, "Informatika (Coding)": 80, "Ekonomi Digital": 84, "Seni & Kreatif": 95},
        {"Absen": 3, "Nama": "Kenzo Aditya", "Matematika": 62, "Sains & Fisika": 65, "Bahasa Indonesia": 70, "Bahasa Inggris": 74, "Informatika (Coding)": 85, "Ekonomi Digital": 68, "Seni & Kreatif": 72},
        {"Absen": 4, "Nama": "Aurelia Nadin", "Matematika": 95, "Sains & Fisika": 92, "Bahasa Indonesia": 88, "Bahasa Inggris": 96, "Informatika (Coding)": 90, "Ekonomi Digital": 94, "Seni & Kreatif": 89},
        {"Absen": 5, "Nama": "Devan Alvaro", "Matematika": 80, "Sains & Fisika": 82, "Bahasa Indonesia": 78, "Bahasa Inggris": 85, "Informatika (Coding)": 92, "Ekonomi Digital": 80, "Seni & Kreatif": 76},
        {"Absen": 6, "Nama": "Keisha Alexandra", "Matematika": 84, "Sains & Fisika": 80, "Bahasa Indonesia": 90, "Bahasa Inggris": 92, "Informatika (Coding)": 86, "Ekonomi Digital": 88, "Seni & Kreatif": 90},
        {"Absen": 7, "Nama": "Arka Pratama", "Matematika": 58, "Sains & Fisika": 60, "Bahasa Indonesia": 68, "Bahasa Inggris": 65, "Informatika (Coding)": 70, "Ekonomi Digital": 62, "Seni & Kreatif": 80},
        {"Absen": 8, "Nama": "Nabila Syahla", "Matematika": 89, "Sains & Fisika": 87, "Bahasa Indonesia": 94, "Bahasa Inggris": 91, "Informatika (Coding)": 88, "Ekonomi Digital": 90, "Seni & Kreatif": 92},
        {"Absen": 9, "Nama": "Gavin Raymond", "Matematika": 72, "Sains & Fisika": 75, "Bahasa Indonesia": 80, "Bahasa Inggris": 82, "Informatika (Coding)": 89, "Ekonomi Digital": 76, "Seni & Kreatif": 74},
        {"Absen": 10, "Nama": "Chloe Jovanka", "Matematika": 90, "Sains & Fisika": 94, "Bahasa Indonesia": 86, "Bahasa Inggris": 95, "Informatika (Coding)": 91, "Ekonomi Digital": 93, "Seni & Kreatif": 88},
        {"Absen": 11, "Nama": "Rafa Elvano", "Matematika": 66, "Sains & Fisika": 70, "Bahasa Indonesia": 75, "Bahasa Inggris": 72, "Informatika (Coding)": 82, "Ekonomi Digital": 70, "Seni & Kreatif": 71},
        {"Absen": 12, "Nama": "Amanda Putri", "Matematika": 83, "Sains & Fisika": 81, "Bahasa Indonesia": 89, "Bahasa Inggris": 87, "Informatika (Coding)": 84, "Ekonomi Digital": 86, "Seni & Kreatif": 91},
        {"Absen": 13, "Nama": "Bintang Syahreza", "Matematika": 78, "Sains & Fisika": 76, "Bahasa Indonesia": 82, "Bahasa Inggris": 80, "Informatika (Coding)": 88, "Ekonomi Digital": 79, "Seni & Kreatif": 85},
        {"Absen": 14, "Nama": "Talitha Azahra", "Matematika": 91, "Sains & Fisika": 89, "Bahasa Indonesia": 95, "Bahasa Inggris": 93, "Informatika (Coding)": 87, "Ekonomi Digital": 92, "Seni & Kreatif": 94},
        {"Absen": 15, "Nama": "Arkanio Malik", "Matematika": 64, "Sains & Fisika": 62, "Bahasa Indonesia": 72, "Bahasa Inggris": 68, "Informatika (Coding)": 76, "Ekonomi Digital": 65, "Seni & Kreatif": 70},
        {"Absen": 16, "Nama": "Keyla Putri", "Matematika": 77, "Sains & Fisika": 80, "Bahasa Indonesia": 84, "Bahasa Inggris": 86, "Informatika (Coding)": 81, "Ekonomi Digital": 83, "Seni & Kreatif": 88},
        {"Absen": 17, "Nama": "Rayhan Ibrahim", "Matematika": 85, "Sains & Fisika": 88, "Bahasa Indonesia": 80, "Bahasa Inggris": 84, "Informatika (Coding)": 95, "Ekonomi Digital": 87, "Seni & Kreatif": 79},
        {"Absen": 18, "Nama": "Nadine Chelsea", "Matematika": 96, "Sains & Fisika": 94, "Bahasa Indonesia": 91, "Bahasa Inggris": 97, "Informatika (Coding)": 93, "Ekonomi Digital": 96, "Seni & Kreatif": 92},
        {"Absen": 19, "Nama": "Dimas Raditya", "Matematika": 70, "Sains & Fisika": 72, "Bahasa Indonesia": 76, "Bahasa Inggris": 78, "Informatika (Coding)": 84, "Ekonomi Digital": 75, "Seni & Kreatif": 73},
        {"Absen": 20, "Nama": "Saskia Indy", "Matematika": 82, "Sains & Fisika": 85, "Bahasa Indonesia": 87, "Bahasa Inggris": 89, "Informatika (Coding)": 83, "Ekonomi Digital": 84, "Seni & Kreatif": 90}
    ])

# Proses Data Global
df = st.session_state.data_siswa.copy()
df['Rata-Rata'] = df[mapel_cols].mean(axis=1).round(1)
df['Total Nilai'] = df[mapel_cols].sum(axis=1)
df['Peringkat'] = df['Rata-Rata'].rank(ascending=False, method='min').astype(int)

# --- 3. FITUR 1: SISTEM LOGIN SIDEBAR (GURU VS SISWA) ---
st.sidebar.title("🔐 Keamanan Sistem")
role = st.sidebar.radio("Masuk Sebagai:", ["Siswa / Orang Tua", "Guru (Wali Kelas)"])

akses_guru = False
if role == "Guru (Wali Kelas)":
    password = st.sidebar.text_input("Masukkan Password Guru:", type="password")
    if password == "guru123":
        st.sidebar.success("Akses Guru Terbuka! ✅")
        akses_guru = True
    elif password != "":
        st.sidebar.error("Password Salah! ❌")

st.sidebar.markdown("---")
st.sidebar.title("⚡ Menu Utama")

daftar_menu = ["1. Dashboard Kelas", "4. Cetak Rapor", "5. Simulator Target", "6. Peringkat Kelas", "7. Pencapaian & Motivasi"]
if akses_guru:
    daftar_menu.insert(1, "2. Tambah Siswa Baru")
    daftar_menu.insert(2, "3. Edit Nilai & Upload Massal")

menu = st.sidebar.selectbox("Pilih Fitur Aplikasi:", daftar_menu)
kkm = st.sidebar.slider("Atur KKM Sekolah", 50, 80, 68)

# --- 4. LOGIKA INTEGRASI FITUR ---
if menu == "1. Dashboard Kelas":
    st.title("📊 Dashboard Analisis Kelas & Sebaran Nilai")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Siswa", f"{len(df)} Orang")
    col2.metric("Rata-Rata Angkatan", f"{df['Rata-Rata'].mean():.1f}")
    col3.metric("Siswa Tertinggi", df.loc[df['Rata-Rata'].idxmax()]['Nama'])
    st.dataframe(df[["Absen", "Peringkat", "Nama"] + mapel_cols + ["Rata-Rata"]], use_container_width=True)
    st.markdown("### 📈 Grafik Tren Distribusi Rata-Rata Kelas (Absen 1 - 20)")
    st.area_chart(df.set_index("Nama")['Rata-Rata'])

elif menu == "2. Tambah Siswa Baru":
    st.title("➕ Registrasi Siswa Baru")
    with st.form("form_add"):
        new_nama = st.text_input("Nama Lengkap Siswa Baru:")
        if st.form_submit_button("Simpan Data"):
            new_row = {"Absen": len(df)+1, "Nama": new_nama, "Matematika": 75, "Sains & Fisika": 75, "Bahasa Indonesia": 75, "Bahasa Inggris": 75, "Informatika (Coding)": 75, "Ekonomi Digital": 75, "Seni & Kreatif": 75}
            st.session_state.data_siswa = pd.concat([st.session_state.data_siswa, pd.DataFrame([new_row])], ignore_index=True)
            st.success("Siswa Berhasil Didaftarkan!")
            st.rerun()
            
elif menu == "3. Edit Nilai & Upload Massal":
    st.title("🔄 Pengelolaan Database Nilai (Guru Only)")
    st.markdown("### 📥 Import Data Massal via File Excel")
    uploaded_file = st.file_uploader("Unggah File Excel Nilai (.xlsx):", type=["xlsx"])
    if uploaded_file is not None:
        try:
            df_uploaded = pd.read_excel(uploaded_file)
            st.session_state.data_siswa = df_uploaded
            st.success("Database Kelas Berhasil Diperbarui Massal!")
            st.rerun()
        except Exception as e:
            st.error(f"Gagal memproses file! Pastikan format kolom sesuai. Detail: {e}")
            
    st.markdown("---")
    st.markdown("### ✏️ Edit Nilai Individual")
    siswa = st.selectbox("Pilih Siswa:", df["Nama"].tolist())
    idx = df[df["Nama"] == siswa].index
    val_edit = st.number_input("Ubah Nilai Matematika:", 0, 100, int(df.loc[idx, "Matematika"].iloc[0]))
    if st.button("Simpan Perubahan"):
        st.session_state.data_siswa.loc[idx, "Matematika"] = val_edit
        st.success("Nilai Berhasil Diperbarui!")
        st.rerun()

elif menu == "4. Cetak Rapor":
    st.title("📄 Cetak E-Rapor Online")
    siswa = st.selectbox("Pilih Nama Anda:", df["Nama"].tolist())
    dt = df[df["Nama"] == siswa].iloc[0]
    
    st.markdown("---")
    st.write(f"## LAPORAN HASIL BELAJAR SISWA: {dt['Nama'].upper()}")
    st.write(f"**Nomor Absen:** {dt['Absen']} | **Peringkat:** {dt['Peringkat']} | **Rata-Rata:** {dt['Rata-Rata']}")
    
    df_rapor_individual = pd.DataFrame({
        "Mata Pelajaran": mapel_cols, 
        "Nilai Angka": [dt[m] for m in mapel_cols],
        "KKM": kkm,
        "Status Kelulusan": ["TUNTAS" if dt[m] >= kkm else "REMEDI" for m in mapel_cols]
    })
    st.table(df_rapor_individual)
    
    st.markdown("### 💬 Catatan Wali Kelas (Evaluasi):")
    if dt['Rata-Rata'] >= 85:
        st.success("💡 *Catatan: Prestasi luar biasa! Pertahankan konsistensi belajar Anda di semester depan.*")
    elif dt['Rata-Rata'] >= 72:
        st.warning("💡 *Catatan: Hasil yang cukup baik. Tingkatkan sedikit lagi frekuensi belajar kelompok Anda.*")
    else:
        st.error("💡 *Catatan: Perlu bimbingan intensif. Kurangi waktu bermain gawai dan fokus pada perbaikan tugas harian.*")
    
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_rapor_individual.to_excel(writer, sheet_name='Rapor', index=False)
    buffer.seek(0)
    st.download_button(label="📥 Download File Excel Rapor Anda", data=buffer, file_name=f"Rapor_{dt['Nama']}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

elif menu == "5. Simulator Target":
    st.title("🎯 Simulator Target Nilai UAS (What-If)")
    n_sekarang = st.number_input("Nilai Akumulasi Tugas Saat Ini:", 0, 100, 70)
    t_rapor = st.slider("Target Nilai Akhir Rapor Impian:", 60, 100, 85)
    if st.button("Hitung"):
        butuh = (t_rapor - (n_sekarang * 0.6)) / 0.4
        if butuh > 100: st.error(f"Mustahil! Anda memerlukan skor ujian akhir sebesar {butuh:.1f} (Batas nilai maks adalah 100). Coba turunkan target.")
        else: st.warning(f"Anda wajib mengamankan nilai UAS minimal sebesar: {butuh:.1f}")

elif menu == "6. Peringkat Kelas":
    st.title("🏆 Hall of Fame - Urutan Peringkat Kelas")
    df_rank = df.sort_values("Peringkat")
    st.success(f"👑 Juara 1 Umum: {df_rank['Nama'].iloc[0]} (Rata-rata: {df_rank['Rata-Rata'].iloc[0]})")
    st.dataframe(df_rank[["Peringkat", "Absen", "Nama", "Rata-Rata"]], use_container_width=True)

elif menu == "7. Pencapaian & Motivasi":
    st.title("✨ Gelar Kompetensi & Motivasi Belajar")
    siswa = st.selectbox("Pilih Nama:", df["Nama"].tolist())
    dt = df[df["Nama"] == siswa].iloc[0]
    
    nilai_mapel = {m: dt[m] for m in mapel_cols}
    top_mapel = max(nilai_mapel, key=nilai_mapel.get)
    
    st.write(f"### 🎖️ Profil Kompetensi Siswa: **{dt['Nama']}**")
    st.success(f"Gelar Spesial Karakter: Master of {top_mapel} (Skor Unggul: {nilai_mapel[top_mapel]})")
    
    st.write("### 💡 Ruang Penguat Motivasi")
    if dt['Rata-Rata'] >= 80:
        st.info("💬 *'Keren banget prestasimu! Tetap rendah hati, pertahankan ritme belajarmu, dan ingat untuk selalu beristirahat yang cukup ya!'*")
    else:
        st.info("💬 *'Nilai rapor semester ini adalah evaluasi, bukan akhir
