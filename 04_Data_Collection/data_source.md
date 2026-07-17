# Data Source

## 1. Sifat Data

Seluruh data pada proyek ini bersifat **sintetis** (dibuat secara terprogram), bukan data operasional perusahaan asli. Ini karena data internal perusahaan ekspedisi bersifat rahasia dan tidak dipublikasikan. Data sintetis dibuat dengan pendekatan Faker (untuk nama, kota) dikombinasikan aturan bisnis logis, agar pola yang terbentuk tetap realistis dan bisa dianalisis secara bermakna.

## 2. Volume dan Cakupan

| Tabel | Estimasi Jumlah Baris | Catatan |
|---|---|---|
| warehouses | 15 | Tersebar di Jawa dan Sumatra |
| couriers | 300 | Terasosiasi ke salah satu warehouse |
| routes | ~100 | Kombinasi antar warehouse |
| customers | 3.000 | Individual dan Business |
| shipments | 8.000-10.000 | Periode beberapa bulan ke belakang |

## 3. Aturan Bisnis di Balik Data

Data `shipments` tidak dibuat acak murni. Pola keterlambatan (`shipment_status`) dipengaruhi beberapa faktor, agar hubungan sebab-akibat dapat ditemukan di tahap EDA dan dipelajari oleh model machine learning:

- **Jarak (distance_km)**: semakin jauh rute, semakin tinggi probabilitas delay.
- **Beban kurir**: kurir yang menangani banyak shipment pada hari yang sama memiliki probabilitas delay lebih tinggi.
- **Musim (high season)**: periode tertentu (11.11, 12.12, menjelang Lebaran) memiliki volume shipment lebih tinggi sekaligus probabilitas delay yang lebih tinggi.
- **Berat paket**: paket dengan berat lebih besar sedikit menaikkan probabilitas delay.

`shipping_cost` dihitung dari kombinasi jarak dan berat paket, ditambah variasi kecil agar tidak terkesan rumus kaku.

## 4. Masalah Kualitas Data yang Disisipkan

Agar tahap ETL (`04_Data_Collection`) dan Data Cleaning (`06_Data_Cleaning`) memiliki materi nyata untuk dikerjakan, beberapa masalah kualitas data disisipkan secara terkontrol pada data `raw/`:

| Masalah | Proporsi | Contoh |
|---|---|---|
| Missing value | ~1-2% | `package_weight_kg` atau `actual_delivery_date` kosong |
| Inkonsistensi format kota | Sebagian kecil baris | "Jakarta", "JKT", "jakarta" untuk kota yang sama |
| Inkonsistensi format tanggal | Sebagian kecil baris | "01/07/2026", "2026-07-01", "1 Jul 2026" |
| Duplicate | ~0.5% | Baris shipment yang tercatat dua kali |
| Outlier | Sebagian kecil baris | `shipping_cost` atau `package_weight_kg` dengan nilai tidak wajar |

Masalah ini didokumentasikan di sini agar transparan, dan proporsinya sengaja dijaga kecil supaya isu utama proyek (analisis keterlambatan pengiriman) tetap menjadi fokus, bukan soal data kotor.

## 5. Pembagian Tanggung Jawab: ETL vs Data Cleaning

| | ETL (`04_Data_Collection`) | Data Cleaning (`06_Data_Cleaning`) |
|---|---|---|
| Sifat perbaikan | Struktural, rule-based, otomatis | Butuh analisis dan pertimbangan |
| Contoh | Standardisasi format tanggal, samakan penulisan kota, konversi tipe data | Keputusan cara menangani missing value, deteksi dan penanganan outlier |
| Bentuk | Script Python (`transform.py`) | Notebook analisis dengan justifikasi |
| Output | `processed/` | Dokumentasi insight dan ringkasan cleaning |

## 6. Alur Data

```
generate_data.py
       ↓
raw/ (5 file CSV, mengandung masalah kualitas data di atas)
       ↓
extract.py (membaca raw/)
       ↓
transform.py (perbaikan struktural)
       ↓
load.py (menyimpan hasil)
       ↓
processed/ (5 file CSV, siap dianalisis lebih lanjut di 06_Data_Cleaning)
```