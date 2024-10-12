import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

# Menghilangkan warning
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

# Judul Dashboard
st.markdown("<h1 style='text-align: center;'>🚴‍♂️ Bike Sharing Dashboard 🚴‍♀️</h1>", unsafe_allow_html=True)

# Penjelasan - Background
st.markdown("<h2 style='text-align: center;'>🌍 Background</h2>", unsafe_allow_html=True)
st.write(""" 
Selamat datang di dunia Bike Sharing Systems! 🚲✨ 
Ini adalah inovasi dalam penyewaan sepeda, di mana proses mulai dari keanggotaan hingga pengembalian telah menjadi otomatis. Dengan sistem ini, pengguna dapat dengan mudah menyewa sepeda dari lokasi tertentu dan mengembalikannya di tempat lain. 🌟 
""")

# Load data
data_path = 'data/day.csv'  # Path relatif untuk deployment
try:
    day_data = pd.read_csv(data_path)
    st.success("Data berhasil dimuat! ✅")
except FileNotFoundError:
    st.error("File tidak ditemukan. Silakan periksa jalur file. ❌")

# Tampilkan Deskripsi Statistik
if 'day_data' in locals():
    st.write("<h3 style='text-align: center;'>📈 Deskripsi Statistik</h3>", unsafe_allow_html=True)
    st.write(day_data.describe(include='all'))

    # Visualisasi 1: Distribusi Jumlah Rental
    st.write("<h3 style='text-align: center;'>📉 Distribusi Jumlah Rental Sepeda</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    sns.histplot(day_data['cnt'], bins=30, kde=True)
    plt.title('Distribusi Jumlah Rental Sepeda')
    plt.xlabel('Jumlah Rental')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)
    st.write(""" 
    Distribusi jumlah rental sepeda menunjukkan pola distribusi yang mirip dengan distribusi normal, 
    dengan puncak yang menunjukkan rentang jumlah rental yang lebih tinggi. Ini mengindikasikan bahwa sebagian besar 
    pengguna lebih cenderung menggunakan sepeda pada frekuensi yang moderat. 🌟 
    """)

    # Visualisasi 2: Hubungan antara Suhu dan Jumlah Rental
    st.write("<h3 style='text-align: center;'>🌡️ Hubungan antara Suhu dan Jumlah Rental</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='temp', y='cnt', data=day_data)
    plt.title('Hubungan antara Suhu dan Jumlah Rental')
    plt.xlabel('Suhu (Celsius)')
    plt.ylabel('Jumlah Rental')
    st.pyplot(plt)
    st.write(""" 
    Dari grafik ini, kita dapat melihat adanya hubungan positif antara suhu dan jumlah rental. 
    Ini berarti ketika suhu meningkat, jumlah rental sepeda cenderung meningkat, menunjukkan bahwa cuaca yang 
    lebih hangat dapat mendorong lebih banyak orang untuk menggunakan sepeda. ☀️ 
    """)

    # Visualisasi 3: Rata-rata Jumlah Rental berdasarkan Kategori Cuaca
    st.write("<h3 style='text-align: center;'>☁️ Rata-rata Jumlah Rental berdasarkan Kategori Cuaca</h3>", unsafe_allow_html=True)
    weather_cnt = day_data.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x='weathersit', y='cnt', data=weather_cnt)
    plt.title('Rata-rata Jumlah Rental berdasarkan Kategori Cuaca')
    plt.xlabel('Kategori Cuaca')
    plt.ylabel('Rata-rata Jumlah Rental')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Hujan', 'Berkabut'])
    st.pyplot(plt)
    st.write(""" 
    Grafik ini menunjukkan bahwa kategori cuaca cerah memiliki rata-rata jumlah rental yang jauh lebih tinggi 
    dibandingkan dengan kondisi cuaca lainnya. Hal ini menunjukkan bahwa pengguna lebih cenderung menggunakan sepeda 
    pada hari-hari yang cerah, sementara hujan dan cuaca berkabut mengurangi minat untuk menyewa sepeda. 🌧️🚫 
    """)

    # Visualisasi 4: Matriks Korelasi
    st.write("<h3 style='text-align: center;'>🔗 Matriks Korelasi</h3>", unsafe_allow_html=True)
    numeric_columns = day_data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_columns.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Matriks Korelasi')
    st.pyplot(plt)
    st.write(""" 
    Matriks korelasi menunjukkan hubungan antara variabel numerik. Misalnya, kita dapat melihat bahwa 
    variabel 'temp' memiliki korelasi positif yang kuat dengan 'cnt', menunjukkan bahwa suhu berkontribusi 
    signifikan terhadap jumlah rental. Variabel lain, seperti 'hum' dan 'windspeed', menunjukkan korelasi 
    negatif dengan jumlah rental, yang mengindikasikan bahwa peningkatan kelembapan dan kecepatan angin dapat 
    mengurangi jumlah pengguna sepeda. 📉 
    """)

# Kontak
st.markdown("<h2 style='text-align: center;'>📧 Kontak</h2>", unsafe_allow_html=True)
st.write(""" 
Untuk informasi lebih lanjut tentang dataset ini, silakan hubungi **Hadi Fanaee-T** (hadi.fanaee@fe.up.pt)
""")

st.markdown("---")
st.markdown("<h2 style='text-align: center;'>✨ Words of Wisdom ✨</h2>", unsafe_allow_html=True)
st.write(""" 
_"Life is like riding a bicycle. To keep your balance, you must keep moving."_  
– **Albert Einstein**
""")
