# Final-Kelompok-6

Nama Anggota Kelompok :
                        - Ichwanul Fata (2108107010035)
                        
                        - T. Rifal Aulia (2108107010064)
                        
                        - Ulan Sawalia (2108107010024)
                        
                        - Nabila Aprillia (2108107010025)
                        
                        - Wilda Fahera (2108107010026)

# Judul Projek 
Image Detection

# Klasifikasi Gambar ( Pistachio)

# Deskripsi 
Dataset di ambil dari website kaggle https://www.kaggle.com/datasets/muratkokludataset/pistachio-image-dataset 

Dataset "Pistachio Image Dataset" ini berisi gambar-gambar pistachio yang digunakan untuk tujuan klasifikasi. Dataset ini dapat digunakan untuk pengenalan dan klasifikasi jenis pistachio berdasarkan gambar. Terdapat dua jenis pistachio dalam dataset ini: Kirmizi dan Siirt. Masing-masing gambar dalam dataset ini memiliki label yang menunjukkan jenis pistachio tersebut. Dataset ini memiliki total 2148 gambar, masing-masing varietas memiliki 1074 gambar. Setiap gambar memiliki resolusi 100x100 piksel dalam format RGB. Dataset ini dirancang untuk tugas klasifikasi citra, membantu model dalam membedakan antara kedua varietas pistachio berdasarkan gambar. Dataset ini dapat digunakan dalam berbagai aplikasi computer vision dan machine learning untuk pengenalan objek dan klasifikasi.

- Atribut Dataset
Dataset ini terdiri dari beberapa atribut berikut:

1. Gambar Pistachio:
- Setiap instance dalam dataset ini merupakan gambar dari pistachio.
- Gambar tersebut berformat RGB dengan resolusi yang seragam.
  
2. Label Klasifikasi:
- Kirmizi: Label untuk jenis pistachio Kirmizi.
- Siirt: Label untuk jenis pistachio Siirt.
  
3. Detail Teknis
- Ukuran Dataset: Dataset ini berisi 2148 gambar pistachio.
  
4. Pembagian Kelas:
- Kirmizi: 1122 gambar
- Siirt: 1026 gambar
  



# Instruksi Penerapan   

Instruksi penerapan adalah petunjuk atau panduan yang memberikan detail langkah demi langkah tentang bagaimana suatu tugas, prosedur, atau kegiatan tertentu harus dilakukan.
Adapun instruksi penerapan pada projek ini adalah sebagai berikut:
1. Pengumpulan Data
   
3. Modelling
   
Persiapan Data
- Mount Google Drive
- Tentukan Path Dataset
- Tentukan Label/Kelas
- Membuat ImageDataGenerator untuk proses prepocessing (Augmentasi dan Normalisasi) 
- Memuat Data Pelatihan dan Validasi
Pengembangan dan Kompilasi Model
- Inisialisasi Model ResNet50:
- Kompilasi Model
Pelatihan Model
- Pelatihan Model dengan Callback
Evaluasi dan Visualisasi
- Visualisasi Distribusi Kelas
- Visualisasi Loss dan Akurasi
Penyimpanan Model
- Simpan Model Terlatih
  
3. Pembuatan Web dan Deployment
  
Langkah-langkah pembuatan Web dan Deploy

1. Membuat Virtual Environment
   - Menggunakan perintah python -m venv venv untuk membuat virtual environment.
   - Virtual environment kemudian diaktifkan dengan perintah source venv/bin/activate (untuk sistem operasi berbasis Linux).

2. Instalasi Flask
   - Flask diinstal ke dalam virtual environment menggunakan perintah pip install Flask.

3. Struktur Proyek
   - Membuat sebuah file app.py sebagai file utama aplikasi Flask.
   - Untuk menyimpan file-file HTML yang diperlukan oleh aplikasi, kami membuat folder bernama templates.

4. Menjalankan Aplikasi
   - Aplikasi Flask dijalankan dengan menggunakan perintah flask run.

5. Integrasi dengan HTML
   - File-file HTML yang dibuat ditempatkan dalam folder templates.
   - Aplikasi Flask merender halaman HTML tersebut ke browser menggunakan fungsi render_template.

6. Hasil Deploy
   - Setelah menjalankan flask run, halaman web berhasil ditampilkan di browser, menunjukkan konten dari file HTML yang sudah dibuat.

# Instalasi

1. Clone Repository
   ```bash
   https://github.com/TeukuRifal/Final-Kelompok-6.git
   ```
2. Masuk ke directory Projek
   ```bash
    cd Final-Kelompok-6
   ```
3. Buat dan Aktifkan virtualenv
    ```bash
    virtualenv projek
    projek\Scripts\activate
    ```
4. Download Model [Model Pistachio](https://drive.google.com/file/d/1J8CQChPbdxP7MeFVx5R-osSJwvn6L1rv/view?usp=drive_link)

5. Pindahkan ke dalam folder Final-Kelompok-6
    
7. Install semua dependencies dari requirements.txt
   ```bash
    pip install -r requirements.txt
    ```
5. jalankan kodenya
   ```bash
   python app.py
   ```
