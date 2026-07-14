# KPI Definition

## 1. Objective

KPI(Key Performance Indicators) digunakan untuk mengukur performa operasional NusaLog Express, mengidentifikasi penyebab keterlambatan, dan mendukung pengambilan keputusan berbasis data. Dua KPI utama, **On-Time Delivery Rate** dan **Delay Rate**, menjadi fokus proyek karena berkaitan langsung dengan masalah bisnis. KPI lain berfungsi sebagai konteks pendukung untuk memperkaya insight dan fitur model prediksi.

## 2. Key Performance Indicators

| KPI | Deskripsi | Tujuan Bisnis |
|---|---|---|
| On-Time Delivery Rate | Persentase pengiriman tepat waktu | Indikator utama kepuasan pelanggan, KPI inti proyek |
| Delay Rate | Persentase pengiriman terlambat | Kebalikan dari On-Time Rate, jadi target variabel model prediksi |
| Average Delivery Time | Rata-rata waktu pengiriman | Menunjukkan efisiensi proses, bukan cuma status tepat/telat |
| Average Shipping Cost | Rata-rata biaya pengiriman | Mengukur efisiensi biaya operasional per pengiriman |
| Shipment Volume | Jumlah pengiriman | Konteks skala operasional (dasar analisis tren dan musiman) |
| Revenue | Total pendapatan pengiriman | Menghubungkan performa operasional dengan dampak finansial |
| Courier Utilization Rate | Beban kerja kurir | Mendeteksi kurir yang overload, salah satu penyebab delay |
| Warehouse Utilization Rate | Beban kerja gudang | Mendeteksi cabang yang overload, salah satu penyebab delay |

## 3. KPI Formula

| KPI | Formula |
|---|---|
| On-Time Delivery Rate | On-Time Shipment / Total Shipment × 100% |
| Delay Rate | Delayed Shipment / Total Shipment × 100% |
| Average Delivery Time | Total Delivery Days / Total Shipment |
| Average Shipping Cost | Total Shipping Cost / Total Shipment |
| Shipment Volume | COUNT(Shipment ID) |
| Revenue | SUM(Shipping Cost) |
| Courier Utilization Rate | Shipment per Courier |
| Warehouse Utilization Rate | Shipment per Warehouse |

## 4. KPI Usage

| KPI | Digunakan di | Peran |
|---|---|---|
| On-Time Delivery Rate | Dashboard, SQL, EDA | Data Analyst |
| Delay Rate | Dashboard, SQL, ML | Data Analyst, Data Scientist |
| Average Delivery Time | Dashboard, SQL | Data Analyst |
| Average Shipping Cost | Dashboard | Data Analyst |
| Shipment Volume | Dashboard | Data Analyst |
| Revenue | Dashboard | Data Analyst |
| Courier Utilization Rate | Dashboard, EDA | Data Analyst |
| Warehouse Utilization Rate | Dashboard, EDA | Data Analyst |

Delay Rate berperan ganda: sebagai KPI di dashboard, sekaligus sebagai target variabel (label) pada model machine learning di tahap `09_Machine_Learning`.