# Requirement Specification

## 1. Project Scope

**In Scope**
- Analisis pengiriman domestik.
- ETL pipeline.
- SQL analysis.
- Dashboard Power BI.
- Machine learning (prediksi keterlambatan).
- Business recommendation.

**Out of Scope**
- Tracking GPS real-time.
- Optimasi rute real-time.
- Integrasi API pihak ketiga.
- Pengiriman internasional.

## 2. Business Questions

Pertanyaan berikut akan dijawab melalui SQL, EDA, dashboard, dan machine learning:

1. Berapa persentase keterlambatan pengiriman?
2. Cabang mana yang memiliki Delay Rate tertinggi?
3. Kurir mana yang paling sering terlambat?
4. Apakah berat paket memengaruhi keterlambatan?
5. Apakah jarak pengiriman memengaruhi keterlambatan?
6. Bagaimana tren pengiriman setiap bulan?
7. Berapa rata-rata waktu pengiriman?
8. Faktor apa yang paling berpengaruh terhadap keterlambatan?
9. Gudang mana yang memiliki beban pengiriman tertinggi?
10. Apakah biaya pengiriman berkorelasi dengan keterlambatan?

## 3. Functional Requirements

| Modul | Requirement |
|---|---|
| Database | Menyimpan data operasional pengiriman |
| ETL | Membersihkan dan memuat data |
| SQL | Menjawab pertanyaan bisnis |
| Dashboard | Menampilkan KPI utama |
| Machine Learning | Memprediksi keterlambatan |
| Documentation | Menjelaskan seluruh proses proyek |

## 4. Data Requirements

Dataset minimal harus memiliki:

| Data | Contoh Kolom |
|---|---|
| Customer | customer_id, city |
| Shipment | shipment_id, shipping_date |
| Courier | courier_id, vehicle |
| Warehouse | warehouse_id, capacity |
| Delivery | delivery_date, status |
| Cost | shipping_cost |

## 5. Expected Deliverables

- Database MySQL.
- ERD.
- ETL pipeline.
- SQL script.
- Notebook Python.
- Dashboard Power BI.
- Model machine learning.
- Business recommendation.