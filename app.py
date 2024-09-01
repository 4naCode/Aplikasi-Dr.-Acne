import streamlit as st
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create a layout with three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Add text to the first column
col1.markdown(" # Welcome To My app!")

# Define the HTML and CSS for justified text with top margin to align with col1
text = """
<div style="text-align: justify; margin-top: 20px;">
    DR. Acne adalah aplikasi sistem pakar yang dirancang untuk membantu pengguna dalam mengetahui jenis jerawat yang mereka alami dan memberikan rekomendasi solusi pengobatan yang tepat dan efektif.
</div>
"""

# Display the justified text in the second column
col2.markdown(text, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")

#load animation
animation_symbol="❄"
#❄❋
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>

    """,
    unsafe_allow_html=True
)
# Menyematkan HTML dan CSS dengan animasi latar belakang
# Data Gejala dengan Deskripsi
gejala = {
   'G01': 'Apakah Anda memiliki benjolan merah yang muncul di wajah atau tubuh?',
    'G02': 'Apakah Anda memiliki bintik-bintik kecil berwarna hitam atau putih di kulit?',
    'G03': 'Apakah jerawat Anda mengandung nanah di dalamnya?',
    'G04': 'Apakah kulit Anda terlihat mengkilap dan berminyak?',
    'G05': 'Apakah Anda memiliki noda atau bekas yang tersisa setelah jerawat sembuh?',
    'G06': 'Apakah Anda merasakan adanya benjolan di bawah kulit yang tidak memiliki kepala putih atau hitam?',
    'G07': 'Apakah Anda memiliki bercak gelap atau hiperpigmentasi setelah jerawat sembuh?'
    }

# Diagnosa dan pengobatan dummy (sesuaikan dengan kebutuhan)
diagnosa = {
    'D01': 'Jerawat Ringan',
    'D02': 'Jerawat Sedang',
    'D03': 'Jerawat Parah',
    'D04': 'Jerawat Batu',
    'D05': 'Post-Inflammatory Erythema',
    'D06': 'Post-Inflammatory Hyperpigmentation (PIH)',
    'D07': 'Jerawat Mendem (Jerawat Subkutan)'
}

#bisa di pake
#pengobatan = {
  #   'D01': 'Gunakan sabun muka yang ringan dan hindari penggunaan produk berminyak.',
  #   'D02': 'Gunakan obat jerawat yang mengandung benzoyl peroxide atau salicylic acid.',
  #   'D03': 'Konsultasikan dengan dokter kulit untuk perawatan lebih lanjut.',
  #   'D04': 'Pertimbangkan terapi intensif dan perawatan medis khusus.',
  #   'D05': 'Hindari paparan sinar matahari dan gunakan produk anti-inflamasi.'
#}
#saya tambahkan css agar kebih 
# Dictionary containing the treatments
pengobatan = {
    'D01': ('Jenis Komedo (blackheads dan whiteheads) serta bintik-bintik kecil. Gunakan sabun muka yang ringan dan hindari penggunaan produk berminyak. '
            'Kebutuhan: Pengelupasan ringan dan pembersihan mendalam untuk mencegah penyumbatan pori.\n'
            '\n**Solusi:**\n'
            '- Salicylic Acid: Membantu mengelupas sel-sel kulit mati dan membersihkan pori-pori. '
            'Produk seperti Neutrogena Oil-Free Acne Wash sangat efektif untuk jenis jerawat ini.\n'
            '- Benzoyl Peroxide: Mengurangi bakteri penyebab jerawat dan peradangan. '
            'Produk seperti Clean & Clear Persa-Gel 10 dapat digunakan untuk komedo yang lebih menonjol.\n'
            '- Retinoid Topikal: Membantu mencegah penyumbatan pori dan mengurangi pembentukan komedo.'),
    'D02': ('Jenis jerawat dengan peradangan ringan hingga sedang, seperti bintik merah dan bengkak. Gunakan obat jerawat yang mengandung: \n'
            '\n**Solusi:**\n'
            '- Benzoyl Peroxide: Mengatasi bakteri penyebab jerawat. Produk seperti La Roche-Posay Effaclar Duo dapat membantu.\n'
            '- Salicylic Acid: Untuk mengurangi kemerahan dan mengelupas sel-sel kulit mati.\n'
            '- Adapalene: Retinoid topikal yang membantu mempercepat pergantian sel dan mencegah penyumbatan pori. Differin Gel adalah pilihan yang baik'),
    'D03': ('Jenis jerawat yang meradang, besar, dan menyakitkan, seperti nodul dan kista. Konsultasikan dengan dokter kulit untuk perawatan lebih lanjut. \n'
            '\n**Solusi:**\n'
            '- Tretinoin: Retinoid topikal yang efektif untuk mengatasi jerawat parah dengan meningkatkan pergantian sel. Tretinoin Cream (Retin-A) dapat digunakan.\n'
            '- Antibiotik Topikal: Seperti Clindamycin Phosphate Lotion yang mengurangi bakteri penyebab jerawat dan peradangan.'
            '- Isotretinoin (Accutane): Untuk kasus jerawat parah yang tidak merespons pengobatan lain. Isotretinoin adalah terapi sistemik yang sangat efektif tetapi memerlukan resep dokter'),
    'D04': ('Jenis jerawat dalam bentuk kista besar dan dalam yang biasanya menyakitkan dan berisi nanah. Pertimbangkan terapi intensif dan perawatan medis khusus mengatasi jerawat batu yang tidak merespons perawatan topikal.\n'
            '\n**Solusi:**\n'
            '- Isotretinoin (Accutane): Merupakan solusi untuk jerawat batu dengan mengurangi ukuran kelenjar minyak dan produksi sebum.\n'
            '- Terapi Laser dan Terapi Lainnya: Teknik medis untuk mengurangi ukuran jerawat batu dan bekasnya.'),
    'D05': ('Kemerahan dan noda yang tertinggal setelah peradangan jerawat sembuh. Hindari paparan sinar matahari dan gunakan produk anti-inflamasi. \n'
            '\n**Solusi:**\n'
            '- Hydrocortisone Cream: Seperti CeraVe Hydrocortisone Cream untuk mengurangi kemerahan dan inflamasi.\n'
            '- Vitamin C: Skinceuticals C E Ferulic membantu mencerahkan kulit dan mengurangi kemerahan.'
            '- Niacinamide: The Ordinary Niacinamide 10% + Zinc 1% untuk meredakan kemerahan dan memperbaiki tekstur kulit.'),
    
    'D06': ('Noda gelap atau kecoklatan yang tertinggal setelah jerawat sembuh, sering terjadi pada kulit yang lebih gelap.. Hindari paparan sinar matahari dan gunakan produk anti-inflamasi. \n'
            '\n**Solusi:**\n'
            '- Hydroquinone: Agen pemutih yang efektif mengurangi hiperpigmentasi. Contoh Produk: Melanox. \n'
            '- Alpha Arbutin: Mencerahkan kulit dan mengurangi noda gelap, Contoh Produk: The Ordinary Alpha Arbutin 2% + HA'
            '- Retinoid: Meningkatkan pergantian sel dan mengurangi pigmentasi, Contoh Produk: Differin Gel'
            '- Sunscreen: Melindungi kulit dari sinar UV yang dapat memperburuk PIH. Contoh Produk: Skin Aqua UV Moisture Milk SPF 50+'),
    
    'D07': ('jenis jerawat yang terbentuk di bawah permukaan kulit, terasa keras, dan tidak memiliki kepala yang terlihat. Hindari paparan sinar matahari dan gunakan produk anti-inflamasi. \n'
            '\n**Solusi:**\n'
            '- Kompres Hangat: Membantu membuka pori-pori dan mempercepat penyembuhan jerawat mendem.\n'
            "- Salicylic Acid: Membantu membersihkan pori-pori yang tersumbat. Contoh Produk: Paula's Choice Skin Perfecting 2% BHA Liquid Exfoliant"
            '- Retinoid Topikal: Meningkatkan pergantian sel kulit untuk mencegah penyumbatan pori. Contoh Produk: Differin Gel'
            '- Spot Treatment dengan Benzoyl Peroxide: Mengurangi bakteri dan peradangan. Contoh Produk: Oxy 5 Acne Pimple Medication')
    

}


# Function to format the dictionary into a structured table
def format_pengobatan(pengobatan):
    formatted_str = ""
    for kode, deskripsi in pengobatan.items():
        formatted_str += f"**Diagnosa:** {kode}\n"
        formatted_str += f"**Pengobatan:** {deskripsi}\n\n"
    return formatted_str

# Generate the formatted output
formatted_pengobatan = format_pengobatan(pengobatan)


# Fungsi untuk menyimpan data konsultasi ke file CSV
# Fungsi untuk menyimpan data konsultasi ke file CSV jika tidak ada duplikat
def simpan_konsultasi_csv(id_konsultasi, nama_pasien, umur_pasien, kab_kota, tanggal_konsultasi, gejala_lap, diagnosa_hasil, pengobatan_saran):
    file_path = 'data/konsultasi.csv'
    
    # Cek dan buat direktori jika tidak ada
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Cek apakah file sudah ada dan buat header jika belum ada
    if not os.path.isfile(file_path):
        header = ['ID Konsultasi', 'Nama Pasien', 'Umur', 'Kota', 'Tanggal Konsultasi', 'Gejala yang Dilaporkan', 'Diagnosa Hasil', 'Pengobatan yang Disarankan']
        data = {
            'ID Konsultasi': [id_konsultasi],
            'Nama Pasien': [nama_pasien],
            'Umur': [umur_pasien],
            'Kota': [kab_kota],
            'Tanggal Konsultasi': [tanggal_konsultasi],
            'Gejala yang Dilaporkan': [gejala_lap],
            'Diagnosa Hasil': [diagnosa_hasil],
            'Pengobatan yang Disarankan': [pengobatan_saran]
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, mode='a', header=header, index=False)
    else:
        df_existing = pd.read_csv(file_path)
        new_data = {
            'ID Konsultasi': [id_konsultasi],
            'Nama Pasien': [nama_pasien],
            'Umur': [umur_pasien],
            'Kota': [kab_kota],
            'Tanggal Konsultasi': [tanggal_konsultasi],
            'Gejala yang Dilaporkan': [gejala_lap],
            'Diagnosa Hasil': [diagnosa_hasil],
            'Pengobatan yang Disarankan': [pengobatan_saran]
        }
        df_new = pd.DataFrame(new_data)
        
        # Cek jika data sudah ada
        if not df_existing[(df_existing['Nama Pasien'] == nama_pasien) & 
                           (df_existing['Umur'] == umur_pasien) &
                           (df_existing['Kota'] == kab_kota) &  
                           (df_existing['Tanggal Konsultasi'] == tanggal_konsultasi) & 
                           (df_existing['Gejala yang Dilaporkan'] == gejala_lap) & 
                           (df_existing['Diagnosa Hasil'] == diagnosa_hasil) & 
                           (df_existing['Pengobatan yang Disarankan'] == pengobatan_saran)].empty:
            #st.info("Data konsultasi sudah ada. solusi : ubah gejela")
             st.markdown("<div style='background-color: #BF0A30; color: white; padding: 10px; border-radius: 5px;'>Data konsultasi sudah ada. solusi: ubah gejala anda</div>", unsafe_allow_html=True)
        else:
            df_new.to_csv(file_path, mode='a', header=False, index=False)
            st.success("Data konsultasi berhasil disimpan.")

# Fungsi utama Streamlit
def main():
    #st.title("Sistem Pakar Jerawat")
 # CSS untuk animasi pada teks
# Define CSS for the animation
    st.markdown("""
    <style>
    @keyframes colorCycle {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .animated-title {
        background: linear-gradient(90deg, white, #BF0A30, purple, #BF0A30, white);
        background-size: 400% 400%;
        webkit-background-clip: text;
        webkit-text-fill-color: transparent;
        animation: colorCycle 5s infinite;
        font-size: 50px;
        text-align: center;
        margin-top: 20px;
        margin: 0; /* Menghapus margin */
        padding: 0; /* Menghapus padding */
    }
    .sub-title {
        font-size: 15px; /* Ukuran font untuk <h2> */
        color: #ffffff; /* Warna teks <h2> */
        text-align: center; /* Align teks di tengah */
        margin: 0; /* Menghapus margin */
        padding: 0; /* Menghapus padding */
    }
    .sub-sub-title {
        font-size: 15px; /* Ukuran font untuk <h3> */
        color: #ffffff; /* Warna teks <h3> */
        text-align: center; /* Align teks di tengah */
        margin: 0; /* Menghapus margin */
        padding: 0; /* Menghapus padding */
    }
    </style>
""", unsafe_allow_html=True)
# Add the animated title
    st.markdown('<h1 class="animated-title">DR. ACNE</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">HELPING WITH ACNE</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="sub-sub-title">ISSUES</h3>', unsafe_allow_html=True)
   
   # Menambahkan teks setelah <h3> untuk menunjukkan jarak
    st.title('')
    st.title('')
    # Inisialisasi st.session_state untuk informasi pribadi dan kontrol tampilan
    if 'informasi_selesai' not in st.session_state:
        st.session_state['informasi_selesai'] = False
    if 'previous_page' not in st.session_state:
        st.session_state['previous_page'] = 'informasi_pribadi'

    if st.session_state['informasi_selesai'] == False and st.session_state['previous_page'] == 'informasi_pribadi':
        #st.header("Informasi Pribadi")
        st.markdown("""<h1 style='font-size: 25px;'>Informasi Pribadi</h1>
                            """, unsafe_allow_html=True)
        
        
        # Formulir pengisian nama, alamat, dan kab/kota
        nama = st.text_input("Nama Lengkap")
        umur = st.number_input("Umur", min_value=0, max_value=120, step=1)
        kab_kota = st.text_input("Kabupaten/Kota")
        
        if st.button("Lanjutkan"):
            if not nama or not umur or not kab_kota:
                #st.warning("Silakan lengkapi semua kolom sebelum melanjutkan.")
                st.markdown("<div style='background-color: #BF0A30; color: white; padding: 10px; border-radius: 5px;'>Silakan lengkapi semua kolom sebelum melanjutkan.</div>", unsafe_allow_html=True)

            else:
                st.session_state['nama'] = nama
                st.session_state['umur'] = umur
                st.session_state['kota'] = kab_kota
                st.session_state['informasi_selesai'] = True
                st.session_state['previous_page'] = 'pengisian_gejala'
                st.experimental_rerun()  # Rerun untuk langsung berpindah ke halaman pengisian gejala
                
    elif st.session_state['informasi_selesai'] == True and st.session_state['previous_page'] == 'pengisian_gejala':
        #st.header("Pengisian Gejala")
        st.markdown("""
    <h1 style='font-size: 25px;'>Pengisian Gejala</h1>
""", unsafe_allow_html=True)
        selected_gejala = []
        for kode, pertanyaan in gejala.items():
            jawaban = st.radio(pertanyaan, options=['No', 'Yes'], key=kode)
            if jawaban == 'Yes':
                selected_gejala.append(kode)
        
        if st.button("Dapatkan Diagnosa"):
            if not selected_gejala:
                st.warning("Silakan jawab setidaknya satu pertanyaan dengan 'Yes'.")
            else:
                hasil_diagnosa = cari_diagnosa(selected_gejala)
                if hasil_diagnosa:
                    diagnosa_hasil = diagnosa[hasil_diagnosa]
                    pengobatan_saran = pengobatan[hasil_diagnosa] 
                    st.success(f"Diagnosa: {diagnosa_hasil}")
                    # Menampilkan teks tebal dalam st.info
                    st.info(f"**Rekomendasi Pengobatan:** {pengobatan_saran}")
                    
                    # Menyimpan data konsultasi ke CSV jika tidak ada duplikat
                    id_konsultasi = f"K{datetime.now().strftime('%y%m%d%H%M%S')}"
                    nama_pasien = st.session_state['nama']
                    umur_pasien = st.session_state['umur']
                    kab_kota = st.session_state['kota']
                    tanggal_konsultasi = datetime.now().strftime('%Y-%m-%d')
                    #jika ingain meberikan gejala bisa di aktivkan
                    gejala_lap = ', '.join(selected_gejala)
                    simpan_konsultasi_csv(id_konsultasi, nama_pasien, umur_pasien, kab_kota, tanggal_konsultasi, gejala_lap, hasil_diagnosa, pengobatan_saran)
                    
                    # Menampilkan data konsultasi
                    #st.header("Data Konsultasi")
                    st.markdown("""
                            <h1 style='font-size: 25px; text-align: center;'>Data Konsultasi</h1>
                            """, unsafe_allow_html=True)
                    tampilkan_data_konsultasi()
                else:
                    st.error("Gejala yang Anda pilih tidak sesuai dengan aturan yang ada.")
        
        # Tombol kembali ke informasi pribadi
        if st.button("Kembali ke Informasi Pribadi"):
            st.session_state['informasi_selesai'] = False
            st.session_state['previous_page'] = 'informasi_pribadi'
            st.experimental_rerun()

# Fungsi untuk mencocokkan diagnosa berdasarkan gejala yang dipilih
def cari_diagnosa(selected_gejala):
    # Contoh aturan sederhana untuk diagnosa modifikasi sesuai kebutuhan)
    aturan = {
    ('G01',): 'D01',  # Jerawat Ringan
    ('G02',): 'D01',  # Jerawat Ringan
    ('G03',): 'D02',  # Jerawat Sedang
    ('G04',): 'D01',  # Jerawat Ringan
    ('G05',): 'D05',  # Post-Inflammatory Erythema
    ('G06',): 'D06',  # Jerawat Mendem
    ('G07',): 'D07',  # PIH (Post-Inflammatory Hyperpigmentation)

    ('G01', 'G02'): 'D01',  # Jerawat Ringan
    ('G01', 'G03'): 'D02',  # Jerawat Sedang
    ('G01', 'G04'): 'D01',  # Jerawat Ringan
    ('G01', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G01', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G07'): 'D07',  # PIH

    ('G02', 'G03'): 'D02',  # Jerawat Sedang
    ('G02', 'G04'): 'D01',  # Jerawat Ringan
    ('G02', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G02', 'G06'): 'D06',  # Jerawat Mendem
    ('G02', 'G07'): 'D07',  # PIH

    ('G03', 'G04'): 'D03',  # Jerawat Parah
    ('G03', 'G05'): 'D04',  # Jerawat Batu
    ('G03', 'G06'): 'D06',  # Jerawat Mendem
    ('G03', 'G07'): 'D07',  # PIH

    ('G04', 'G05'): 'D04',  # Jerawat Batu
    ('G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G04', 'G07'): 'D07',  # PIH

    ('G05', 'G06'): 'D06',  # Jerawat Mendem
    ('G05', 'G07'): 'D07',  # PIH

    ('G01', 'G02', 'G03'): 'D02',  # Jerawat Sedang
    ('G01', 'G02', 'G04'): 'D01',  # Jerawat Ringan
    ('G01', 'G02', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G01', 'G02', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G02', 'G07'): 'D07',  # PIH

    ('G01', 'G03', 'G04'): 'D03',  # Jerawat Parah
    ('G01', 'G03', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G01', 'G03', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G03', 'G07'): 'D07',  # PIH

    ('G02', 'G03', 'G04'): 'D02',  # Jerawat Sedang
    ('G02', 'G03', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G02', 'G03', 'G06'): 'D06',  # Jerawat Mendem
    ('G02', 'G03', 'G07'): 'D07',  # PIH

    ('G02', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G02', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G02', 'G04', 'G07'): 'D07',  # PIH

    ('G03', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G03', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G03', 'G04', 'G07'): 'D07',  # PIH

    ('G01', 'G02', 'G03', 'G04'): 'D03',  # Jerawat Parah
    ('G01', 'G02', 'G03', 'G05'): 'D05',  # Post-Inflammatory Erythema
    ('G01', 'G02', 'G03', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G02', 'G03', 'G07'): 'D07',  # PIH

    ('G01', 'G02', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G01', 'G02', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G02', 'G04', 'G07'): 'D07',  # PIH

    ('G01', 'G03', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G01', 'G03', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G03', 'G04', 'G07'): 'D07',  # PIH

    ('G02', 'G03', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G02', 'G03', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G02', 'G03', 'G04', 'G07'): 'D07',  # PIH

    ('G01', 'G02', 'G03', 'G04', 'G05'): 'D04',  # Jerawat Batu
    ('G01', 'G02', 'G03', 'G04', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G02', 'G03', 'G04', 'G07'): 'D07',  # PIH

    ('G01', 'G02', 'G03', 'G05', 'G06'): 'D06',  # Jerawat Mendem
    ('G01', 'G02', 'G03', 'G05', 'G07'): 'D07',  # PIH
}


   # for rule, diagnosis in aturan.items():
   #     if all(gejala in selected_gejala for gejala in rule):
   #         return diagnosis
   # return None
 # Convert the selected_gejala to a set for faster lookup
    selected_gejala_set = set(selected_gejala)
    
    # Iterate through each rule in aturan, sorted by the length of the rule (longer rules first)
    for rule in sorted(aturan.keys(), key=len, reverse=True):
        # Check if all gejala in the rule are present in selected_gejala
        if all(gejala in selected_gejala_set for gejala in rule):
            print(f"Match found: Rule = {rule}, Diagnosis = {aturan[rule]}")  # Debug output
            return aturan[rule]
    
    # Return None if no matching diagnosis is found
    print("No match found")  # Debug output
    return 'Diagnosa Tidak Diketahui'

# Fungsi untuk menampilkan data konsultasi dari file CSV
def tampilkan_data_konsultasi():
    file_path = 'data/konsultasi.csv'
    try:
        # Baca data dari file CSV
        df = pd.read_csv(file_path)
        df1 = df.copy()
        # Ubah kode diagnosa menjadi deskripsi menggunakan dictionary
        df1['Diagnosa Hasil'] = df1['Diagnosa Hasil'].map(diagnosa)
        df_filtered = df1[['ID Konsultasi','Nama Pasien','Umur','Kota','Tanggal Konsultasi','Diagnosa Hasil']]
        # Tampilkan hanya 5 data pertama
        st.dataframe(df_filtered.head(5))
        
        # Jika data lebih dari 5 baris, tampilkan pilihan untuk melihat lebih banyak
        if len(df_filtered) > 5:
            with st.expander("Lihat Selengkapnya"):
                st.dataframe(df_filtered)


                 # Visualisasi nilai count dari Diagnosa Hasil
        st.subheader('Distribusi Diagnosa Hasil')
        
        # Hitung frekuensi diagnosa hasil
        count_diagnosa = df1['Diagnosa Hasil'].value_counts()

        # Buat figure dan axis
        fig, ax = plt.subplots(figsize=(12, 6))  # Ukuran figure disesuaikan

        # Set background color
        fig.patch.set_facecolor('#2B4869')  # Latar belakang figure
        ax.set_facecolor('#2B4869')         # Latar belakang area plot

        # Plot bar chart
        bars = sns.barplot(y=count_diagnosa.index, x=count_diagnosa.values, ax=ax, palette='viridis')

        # Set titles and labels
        ax.set_title('Frekuensi Diagnosa Hasil', fontsize=16, color='white')
        ax.set_xlabel('Jumlah', fontsize=14, color='white')
        ax.set_ylabel('Diagnosa Hasil', fontsize=14, color='white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', rotation=0, colors='white')  # Rotasi label y-axis jika diperlukan

        # Hilangkan garis atas dan kanan
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Ubah warna garis kiri dan bawah menjadi putih
        ax.spines['left'].set_color('white')
        ax.spines['left'].set_linewidth(1)
        ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_linewidth(1)

        # Tampilkan label nilai pada setiap bar
        for bar in bars.patches:
            # Ambil posisi x dan tinggi bar
            width = bar.get_width()
            # Tambahkan teks di atas bar
            ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.0f}', ha='left', va='center', color='white', fontsize=12)

        # Tampilkan plot di Streamlit
        st.pyplot(fig)
            


            #visualisasi 2

        # Hitung frekuensi umur
        count_usia = df1['Umur'].value_counts().sort_index()

        # Hitung frekuensi kota
        count_kota = df1['Kota'].value_counts()

        # Setup subplots
        fig, axs = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
        fig.patch.set_facecolor('#2B4869')  # Latar belakang figure

        # Set background color for each subplot
        for ax in axs:
            ax.set_facecolor('#2B4869')

        # Plot bar chart untuk Umur
        sns.barplot(x=count_usia.index, y=count_usia.values, ax=axs[0], palette='viridis')
        axs[0].set_title('Frekuensi Umur', fontsize=16, color='white')
        axs[0].set_xlabel('Usia', fontsize=14, color='white')
        axs[0].set_ylabel('Jumlah', fontsize=14, color='white')
        axs[0].tick_params(axis='x', rotation=45, colors='white')
        axs[0].tick_params(axis='y', colors='white')
        axs[0].spines['top'].set_visible(False)
        axs[0].spines['right'].set_visible(False)
        axs[0].spines['left'].set_color('white')
        axs[0].spines['left'].set_linewidth(1)
        axs[0].spines['bottom'].set_color('white')
        axs[0].spines['bottom'].set_linewidth(1)
        axs[0].grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
        for bar in axs[0].patches:
            height = bar.get_height()
            axs[0].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}', ha='center', va='bottom', color='white', fontsize=12)

        # Plot bar chart untuk Kota
        sns.barplot(x=count_kota.index, y=count_kota.values, ax=axs[1], palette='viridis')
        axs[1].set_title('Frekuensi Kota', fontsize=16, color='white')
        axs[1].set_xlabel('Kota', fontsize=14, color='white')
        axs[1].set_ylabel('Jumlah', fontsize=14, color='white')
        axs[1].tick_params(axis='x', rotation=45, colors='white')
        axs[1].tick_params(axis='y', colors='white')
        axs[1].spines['top'].set_visible(False)
        axs[1].spines['right'].set_visible(False)
        axs[1].spines['left'].set_color('white')
        axs[1].spines['left'].set_linewidth(1)
        axs[1].spines['bottom'].set_color('white')
        axs[1].spines['bottom'].set_linewidth(1)
        axs[1].grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
        for bar in axs[1].patches:
            height = bar.get_height()
            axs[1].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}', ha='center', va='bottom', color='white', fontsize=12)

        plt.tight_layout()
        plt.show()
        # Tampilkan plot di Streamlit
        st.pyplot(fig)
    except FileNotFoundError:
        st.write("Belum ada data konsultasi.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")





# Menambahkan teks Copyright yang bisa diklik di bagian bawah dan memusatkannya
# Menambahkan teks Copyright yang bisa diklik di bagian bawah dan memusatkannya
# Menambahkan teks Copyright yang bisa diklik di bagian bawah dan memusatkannya

st.markdown("""
    <style>
        .footer {
            position: fixed; /* Memastikan footer tetap di bawah */
            bottom: 0; /* Jarak dari bawah halaman */
            left: 0; /* Menjaga footer di kiri halaman */
            width: 100%; /* Memastikan footer lebar penuh */
            text-align: center; /* Memusatkan teks */
            background-color: transparent; /* Menghapus latar belakang */
            display: flex; /* Menggunakan Flexbox */
            justify-content: center; /* Memusatkan teks secara horizontal */
            align-items: center; /* Memusatkan teks secara vertikal */
            height: 40px; /* Menetapkan tinggi footer jika diperlukan */
            box-shadow: 0 -1px 5px rgba(0,0,0,0.1); /* Menambahkan bayangan ringan jika diperlukan */
        }
        .footer p {
            color: white; /* Warna teks copyright */
            margin: 0; /* Menghapus margin default */
        }
        .footer a {
            color: white; /* Warna teks link */
            text-decoration: none; /* Menghapus garis bawah pada link */
        }
        .footer a:hover {
            text-decoration: underline; /* Garis bawah saat hover */
        }
    </style>
    <div class="footer">
        <p>Copyright by <a href="https://noerilagians.blogspot.com/" target="_blank">agian</a></p>
    </div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()



# Konten aplikasi Anda di sini

