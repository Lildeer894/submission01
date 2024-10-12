import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

# Menghilangkan warning
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

# Judul Dashboard
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🚴‍♂️ Bike Sharing Dashboard 🚴‍♀️</h1>", unsafe_allow_html=True)

# Penjelasan - Background
st.markdown("<h2 style='text-align: center; color: #5D6D7E;'>🌍 🌍 🌍</h2>", unsafe_allow_html=True)
st.write(""" 
<div style='text-align: center;'>
Selamat datang di dunia Bike Sharing Systems! 🚲✨ 
Dengan sistem ini, pengguna dapat menyewa sepeda dengan mudah dari lokasi tertentu dan mengembalikannya di tempat lain. Mari kita jelajahi lebih dalam!
</div>
""", unsafe_allow_html=True)

# Load data
data_path = 'data/day.csv'  # Path relatif untuk deployment
try:
    day_data = pd.read_csv(data_path)
    st.success("Data berhasil dimuat! ✅")
except FileNotFoundError:
    st.error("File tidak ditemukan. Silakan periksa jalur file. ❌")

# Tampilkan Deskripsi Statistik
if 'day_data' in locals():
    st.markdown("<h3 style='text-align: center; color: #5D6D7E;'>📈 Deskripsi Statistik</h3>", unsafe_allow_html=True)
    st.write(day_data.describe(include='all'))

    # Visualisasi 1: Distribusi Jumlah Rental
    st.markdown("<h3 style='text-align: center; color: #F39C12;'>📉 Distribusi Jumlah Rental Sepeda</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    sns.histplot(day_data['cnt'], bins=30, kde=True, color='skyblue')
    plt.title('Distribusi Jumlah Rental Sepeda', fontsize=16, loc='center')
    plt.xlabel('Jumlah Rental', fontsize=12)
    plt.ylabel('Frekuensi', fontsize=12)
    st.pyplot(plt)
    st.markdown(""" 
    <div style='text-align: center;'>
    Distribusi jumlah rental sepeda menunjukkan pola distribusi yang mirip dengan distribusi normal, 
    dengan puncak yang menunjukkan rentang jumlah rental yang lebih tinggi. Ini mengindikasikan bahwa sebagian besar 
    pengguna lebih cenderung menggunakan sepeda pada frekuensi yang moderat. 🌟 
    </div>
    """, unsafe_allow_html=True)

    # Visualisasi 2: Hubungan antara Suhu dan Jumlah Rental
    st.markdown("<h3 style='text-align: center; color: #F39C12;'>🌡️ Hubungan antara Suhu dan Jumlah Rental</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='temp', y='cnt', data=day_data, color='orange', alpha=0.7)
    plt.title('Hubungan antara Suhu dan Jumlah Rental', fontsize=16, loc='center')
    plt.xlabel('Suhu (Celsius)', fontsize=12)
    plt.ylabel('Jumlah Rental', fontsize=12)
    st.pyplot(plt)
    st.markdown(""" 
    <div style='text-align: center;'>
    Dari grafik ini, kita dapat melihat adanya hubungan positif antara suhu dan jumlah rental. 
    Ini berarti ketika suhu meningkat, jumlah rental sepeda cenderung meningkat, menunjukkan bahwa cuaca yang 
    lebih hangat dapat mendorong lebih banyak orang untuk menggunakan sepeda. ☀️ 
    </div>
    """, unsafe_allow_html=True)

    # Visualisasi 3: Rata-rata Jumlah Rental berdasarkan Kategori Cuaca
    st.markdown("<h3 style='text-align: center; color: #F39C12;'>☁️ Rata-rata Jumlah Rental berdasarkan Kategori Cuaca</h3>", unsafe_allow_html=True)
    weather_cnt = day_data.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x='weathersit', y='cnt', data=weather_cnt, palette='pastel')
    plt.title('Rata-rata Jumlah Rental berdasarkan Kategori Cuaca', fontsize=16, loc='center')
    plt.xlabel('Kategori Cuaca', fontsize=12)
    plt.ylabel('Rata-rata Jumlah Rental', fontsize=12)
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Hujan', 'Berkabut'])
    st.pyplot(plt)
    st.markdown(""" 
    <div style='text-align: center;'>
    Grafik ini menunjukkan bahwa kategori cuaca cerah memiliki rata-rata jumlah rental yang jauh lebih tinggi 
    dibandingkan dengan kondisi cuaca lainnya. Hal ini menunjukkan bahwa pengguna lebih cenderung menggunakan sepeda 
    pada hari-hari yang cerah, sementara hujan dan cuaca berkabut mengurangi minat untuk menyewa sepeda. 🌧️🚫 
    </div>
    """, unsafe_allow_html=True)

    # Visualisasi 4: Matriks Korelasi
    st.markdown("<h3 style='text-align: center; color: #F39C12;'>🔗 Matriks Korelasi</h3>", unsafe_allow_html=True)
    numeric_columns = day_data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_columns.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'shrink': .8})
    plt.title('Matriks Korelasi', fontsize=16, loc='center')
    st.pyplot(plt)
    st.markdown(""" 
    <div style='text-align: center;'>
    Matriks korelasi menunjukkan hubungan antara variabel numerik. Misalnya, kita dapat melihat bahwa 
    variabel 'temp' memiliki korelasi positif yang kuat dengan 'cnt', menunjukkan bahwa suhu berkontribusi 
    signifikan terhadap jumlah rental. Variabel lain, seperti 'hum' dan 'windspeed', menunjukkan korelasi 
    negatif dengan jumlah rental, yang mengindikasikan bahwa peningkatan kelembapan dan kecepatan angin dapat 
    mengurangi jumlah pengguna sepeda. 📉 
    </div>
    """, unsafe_allow_html=True)

# Kontak
st.markdown("<h2 style='text-align: center; color: #5D6D7E;'>📧 Kontak</h2>", unsafe_allow_html=True)
st.write(""" 
<div style='text-align: center;'>
Untuk informasi lebih lanjut tentang dataset ini, silakan hubungi **Hadi Fanaee-T** (hadi.fanaee@fe.up.pt)
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #5D6D7E;'>✨ Words of Wisdom ✨</h2>", unsafe_allow_html=True)
st.write(""" 
<div style='text-align: center;'>
_"Life is like riding a bicycle. To keep your balance, you must keep moving."_  
– **Albert Einstein**
</div>
""", unsafe_allow_html=True)
