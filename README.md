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
```bash
# 1. Buat folder proyek dan masuk ke dalamnya
mkdir Submission_Proyek Data Science
cd Submission_Proyek Data Science

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

### Insight Dashboard

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
