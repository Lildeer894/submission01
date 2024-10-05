#**Bike Sharing Dashboard**

## Deskripsi
Proyek ini adalah dashboard analisis data untuk sistem bike sharing yang menggunakan dataset dari Capital Bikeshare di Washington D.C. Dashboard ini memberikan visualisasi dan analisis mengenai pola penggunaan sepeda berdasarkan faktor lingkungan dan musiman.

## Prerequisites
Sebelum menjalankan dashboard, pastikan Anda memiliki Python 3.1 terinstal di sistem Anda.

## Instalasi
1. Clone repositori ini:
   ```bash
   git clone <URL_REPOSITORI>
   cd <NAMA_FOLDER>
2. Buat virtual environment (opsional, tetapi disarankan):
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
venv\Scripts\activate     # Untuk Windows
3. Install dependencies:
pip install -r requirements.txt

## Mennjalankan Dashboard
Setelah semua dependencies terinstal, Anda bisa menjalankan dashboard dengan perintah berikut:
streamlit run dashboard.py

# Data
Dataset yang digunakan dalam proyek ini adalah:
day.csv: Berisi data penyewaan sepeda berdasarkan hari.
hour.csv: Berisi data penyewaan sepeda berdasarkan jam.

