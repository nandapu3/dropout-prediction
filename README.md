# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi baik dalam mencetak lulusan yang berkualitas. Namun, dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius berupa meningkatnya angka dropout atau siswa yang tidak menyelesaikan pendidikannya. Tingginya tingkat dropout ini menjadi perhatian utama karena tidak hanya berdampak pada citra dan reputasi akademik, tetapi juga memengaruhi akreditasi, kepercayaan publik, serta efisiensi dan keberlanjutan operasional institusi secara keseluruhan.

Untuk menghadapi tantangan tersebut, Jaya Jaya Institut ingin memanfaatkan pendekatan berbasis data guna mengidentifikasi potensi risiko dropout sejak dini. Pihak institusi telah menyediakan dataset performa siswa dan berharap dapat dibangun model prediktif yang mampu mengenali pola-pola yang berkaitan dengan kemungkinan siswa mengalami dropout. Model ini diharapkan dapat digunakan sebagai dasar dalam pemberian intervensi lebih awal kepada siswa yang terindikasi berisiko, seperti pendampingan akademik atau dukungan emosional, sehingga potensi dropout dapat ditekan.

Selain pengembangan model prediktif, institusi juga membutuhkan sarana visualisasi data yang dapat mempermudah proses pemantauan dan pengambilan keputusan. Oleh karena itu, proyek ini juga mencakup pembuatan dashboard bisnis menggunakan Metabase. Dashboard ini dirancang untuk menyajikan informasi performa siswa secara interaktif, membantu pihak manajemen dan akademik dalam memahami tren dan distribusi risiko, serta memantau efektivitas dari kebijakan atau intervensi yang diterapkan.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tantangan serius dalam hal meningkatnya jumlah siswa yang tidak menyelesaikan pendidikannya. Setelah ditelusuri lebih lanjut, terdapat beberapa akar masalah yang perlu segera ditangani, antara lain:
- Belum adanya sistem prediktif yang dapat membantu mengidentifikasi siswa-siswa yang berisiko mengalami *dropout* sejak awal. Akibatnya, intervensi yang seharusnya bisa diberikan lebih cepat justru sering terlambat.
- Kurangnya pemantauan performa siswa secara menyeluruh, sehingga pihak akademik kesulitan dalam memahami kondisi siswa secara real-time dan mengambil keputusan berbasis data yang akurat.
- Belum tersedia dashboard visual interaktif untuk memantau perkembangan siswa secara berkala dan mengevaluasi efektivitas dari intervensi yang telah dijalankan.

### Cakupan Proyek
Proyek ini difokuskan untuk membantu Jaya Jaya Institut dalam menangani permasalahan tingginya angka *dropout* siswa melalui pendekatan berbasis data. Adapun cakupan proyek yang akan dikerjakan meliputi beberapa tahapan utama berikut:

- Melakukan eksplorasi dan pembersihan data (data preprocessing) terhadap dataset performa siswa yang telah disediakan oleh institusi.
- Membangun model prediktif yang dapat mengidentifikasi siswa dengan potensi risiko *dropout* berdasarkan fitur-fitur yang relevan dalam dataset.
- Melakukan evaluasi model untuk memastikan bahwa hasil prediksi memiliki akurasi dan interpretabilitas yang baik bagi pengguna.
- Membangun dashboard menggunakan Metabase yang menyajikan informasi performa siswa dan insight lainnya secara visual dan mudah dipahami.

### Persiapan

Sumber data:  
Dataset Student Performance yang diambil dari
[https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:  
**Clone atau download** folder project ke komputer lokal.
```bash
# 1. masuk kedalam folder project
cd nama_folder_project

# 2. Buat virtual environment
python -m venv venv

# 3. Aktifkan
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 4. Install semua library
pip install -r requirements.txt
```
Cara Menjalankan Dashboard:  
Jalankan perintah berikut menggunakan Docker:

```bash
docker run -d \
  -p 3000:3000 \
  -v $(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db \
  -e "MB_DB_FILE=/metabase.db/metabase.db.mv.db" \
  --name metabase \
  metabase/metabase
```

Setelah perintah berhasil dijalankan, buka browser Anda dan kunjungi:

```
http://localhost:3000
```

## Business Dashboard
Setelah menjalankan Metabase (lihat bagian Setup Environment), login dengan kredensial berikut:

| Email             | Password  |
|-------------------|-----------|
| `root@mail.com`   | `root123` |

### 🎓 Insight Dashboard: Student Performance Jaya Jaya Institut

Dashboard ini memberikan gambaran menyeluruh mengenai performa akademik mahasiswa di Jaya Jaya Institut, dengan fokus pada tingkat kelulusan, dropout, dan faktor-faktor yang memengaruhinya.

### 📊 Ringkasan Utama (KPI)

Dari total 4.424 mahasiswa, tercatat bahwa **32,12% mahasiswa mengalami dropout**, yang berarti sekitar satu dari tiga mahasiswa tidak menyelesaikan studinya. Persentase ini cukup tinggi dan menunjukkan perlunya perhatian khusus dari pihak institusi. Di sisi lain, sekitar **24,84% mahasiswa merupakan penerima beasiswa**, yang menunjukkan adanya upaya mendukung mahasiswa secara finansial. Rata-rata usia mahasiswa dropout adalah **26,07 tahun**, yang menunjukkan bahwa sebagian dari mereka mungkin merupakan mahasiswa non-tradisional, mahasiswa pindahan, atau mereka yang harus membagi waktu dengan pekerjaan atau keluarga.

### 📈 Distribusi Status Mahasiswa

Distribusi status mahasiswa menunjukkan bahwa **49,9% mahasiswa berhasil lulus**, sementara **32,1% dropout**, dan sisanya **17,9% masih aktif terdaftar** (enrolled). Rasio kelulusan yang mendekati 50% dapat dikatakan moderat, namun tingginya tingkat dropout menandakan perlunya strategi retensi yang lebih baik.

### 🕒 Dropout Berdasarkan Tipe Kehadiran

Dalam grafik dropout berdasarkan tipe kehadiran, terlihat bahwa mahasiswa **kelas siang (Daytime)** menyumbang sekitar **1.200 dropout**, sementara mahasiswa **kelas malam (Evening)** hanya sekitar **300 orang**. Ini bisa mengindikasikan bahwa mahasiswa siang lebih rentan terhadap dropout, namun perlu ditinjau apakah hal ini disebabkan oleh distribusi proporsi yang memang lebih banyak di kelas siang, atau ada faktor-faktor internal seperti beban studi atau manajemen waktu yang perlu dievaluasi.

### 🎓 Status Mahasiswa vs Penerima Beasiswa

Analisis hubungan antara status mahasiswa dan beasiswa, jika dibandingkan berdasarkan gender, menunjukkan bahwa **penerima beasiswa dari kedua gender cenderung lebih tinggi tingkat kelulusannya**. Namun, jumlah dropout pada penerima beasiswa juga tetap ada dalam jumlah yang signifikan. Hal ini menunjukkan bahwa **dukungan finansial saja belum cukup**, dan perlu diimbangi dengan dukungan akademik, psikologis, dan mentoring secara menyeluruh.

---

### 📌 Kesimpulan Umum

Secara keseluruhan, dashboard ini mengungkap bahwa **tingkat dropout yang tinggi (32,12%) merupakan tantangan utama** bagi Jaya Jaya Institut. Meskipun beasiswa telah membantu sebagian mahasiswa mencapai kelulusan, perlu ada pendekatan yang lebih holistik terhadap bimbingan akademik dan sosial. Perhatian khusus juga perlu diberikan pada mahasiswa daytime, serta kelompok mahasiswa yang berusia lebih tua dan mungkin memiliki kebutuhan dukungan yang berbeda dari mahasiswa reguler.


## Menjalankan Sistem Machine Learning
Prototype ini merupakan aplikasi prediksi risiko dropout mahasiswa berbasis machine learning, yang dibangun menggunakan model *Logistic Regression*. Aplikasi ini diimplementasikan dalam antarmuka interaktif menggunakan **Streamlit**, sehingga mudah digunakan oleh pengguna non-teknis seperti dosen pembimbing akademik atau pihak pengelola institusi. Setelah environment selesai di-setup dan semua library terinstal, ikuti langkah berikut: 

```
streamlit run app.py
```
Prototype juga dapat diakses melalui link [Aplikasi Streamlit](https://nandapu3-dropout-prediction-app-chpt2f.streamlit.app/)  

### File Penting dalam Prototype

Berikut adalah daftar file utama yang membentuk sistem prediksi risiko dropout mahasiswa:

- **`app.py`**  
  Aplikasi utama berbasis Streamlit yang digunakan untuk menampilkan antarmuka prediksi.

- **`mappings.py`**  
  Berisi dictionary mapping untuk mengubah input kategori menjadi nilai numerik yang sesuai dengan model.

- **`model_logreg.pkl`**  
  File hasil _training_ model machine learning (Logistic Regression) yang disimpan menggunakan `joblib`.

- **`scaler_model.pkl`**  
  File scaler (StandardScaler) yang digunakan untuk menormalisasi fitur numerik sebelum prediksi.

- **`requirements.txt`**  
  Daftar pustaka atau library Python yang diperlukan untuk menjalankan aplikasi, termasuk `streamlit`, `pandas`, `scikit-learn`, dan lainnya.


## Conclusion
Proyek ini berhasil mengembangkan sistem machine learning berbasis aplikasi Streamlit untuk memprediksi risiko dropout mahasiswa di Jaya Jaya Institut. Dengan memanfaatkan data historis mahasiswa yang mencakup informasi akademik, demografis, dan administratif, model logistic regression yang dibangun mampu mengidentifikasi calon mahasiswa yang berpotensi dropout dengan akurasi sebesar 85%. Berdasarkan hasil analisis data, diketahui bahwa risiko dropout sangat dipengaruhi oleh kombinasi faktor akademik, finansial, dan latar belakang pribadi. Mahasiswa dengan tunggakan pembayaran menunjukkan kecenderungan lebih tinggi untuk dropout, sementara performa akademik yang rendah pada semester pertama, seperti sedikitnya mata kuliah yang lulus dan nilai rata-rata yang buruk, menjadi indikator kuat lainnya. Urutan pilihan jurusan saat pendaftaran serta latar belakang pendidikan dan pekerjaan orang tua juga berkontribusi terhadap tingkat risiko tersebut. Aplikasi ini memungkinkan pengguna (misalnya dosen wali atau manajemen akademik) untuk memasukkan data mahasiswa baru secara interaktif dan memperoleh prediksi risiko dropout secara instan. Dengan demikian, institusi dapat melakukan intervensi atau pembinaan lebih awal terhadap mahasiswa berisiko tinggi, sehingga dapat menekan angka dropout dan meningkatkan keberhasilan studi. Secara keseluruhan, sistem ini menunjukkan potensi nyata pemanfaatan machine learning untuk mendukung pengambilan keputusan di bidang pendidikan secara proaktif dan berbasis data.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- **Pemberian Intervensi Dini dan Bimbingan Akademik:** Tawarkan program bimbingan khusus, mentoring, atau pembinaan intensif kepada mahasiswa yang terdeteksi berisiko tinggi, khususnya yang memiliki performa akademik rendah pada semester awal. 
- **Pelatihan Dosen Wali dalam Pemanfaatan Data Prediktif:** Bekali dosen wali dengan pelatihan penggunaan sistem ini agar mereka mampu memahami risiko mahasiswa bimbingannya secara data-driven dan lebih responsif terhadap kebutuhan individu.
- **Peringatan Keuangan Dini dan Dukungan Beasiswa:**  Mahasiswa yang tercatat sebagai *debtor* atau mengalami tunggakan pembayaran perlu diberikan notifikasi lebih awal dan diarahkan ke skema bantuan keuangan atau keringanan pembayaran.
