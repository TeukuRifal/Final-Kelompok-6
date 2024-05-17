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
2. Modelling
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
3. Pembuatan Web
4. Deployment

