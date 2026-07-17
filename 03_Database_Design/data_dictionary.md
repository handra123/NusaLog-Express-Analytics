# Data Dictionary

Dokumen ini menjelaskan struktur final 5 tabel yang digunakan pada proyek NusaLog Express Analytics. Struktur ini menjadi acuan untuk `database_schema.sql`, proses ETL, dan seluruh tahap analisis berikutnya.

## 1. `customers`

| Kolom | Tipe Data | Key | Nullable | Keterangan |
|---|---|---|---|---|
| customer_id | INT | PK | No | ID unik pelanggan |
| customer_name | VARCHAR(100) | - | No | Nama pelanggan |
| city | VARCHAR(50) | - | No | Kota asal pelanggan |
| customer_type | VARCHAR(20) | - | No | Individual atau Business |

## 2. `warehouses`

| Kolom | Tipe Data | Key | Nullable | Keterangan |
|---|---|---|---|---|
| warehouse_id | INT | PK | No | ID unik gudang/cabang |
| warehouse_name | VARCHAR(100) | - | No | Nama cabang |
| city | VARCHAR(50) | - | No | Kota lokasi cabang |
| region | VARCHAR(50) | - | No | Wilayah (Jawa/Sumatra) |
| daily_shipment_capacity | INT | - | No | Kapasitas gudang memproses pengiriman per hari |

## 3. `couriers`

| Kolom | Tipe Data | Key | Nullable | Keterangan |
|---|---|---|---|---|
| courier_id | INT | PK | No | ID unik kurir |
| courier_name | VARCHAR(100) | - | No | Nama kurir |
| warehouse_id | INT | FK -> warehouses.warehouse_id | No | Cabang penempatan kurir |
| vehicle_type | VARCHAR(20) | - | No | Motor, Mobil Box, atau Truk |
| daily_delivery_capacity | INT | - | No | Kapasitas kurir mengantar paket per hari |

## 4. `routes`

| Kolom | Tipe Data | Key | Nullable | Keterangan |
|---|---|---|---|---|
| route_id | INT | PK | No | ID unik rute |
| origin_warehouse_id | INT | FK -> warehouses.warehouse_id | No | Cabang asal |
| destination_warehouse_id | INT | FK -> warehouses.warehouse_id | No | Cabang tujuan |
| distance_km | DECIMAL(6,2) | - | No | Jarak tempuh dalam kilometer |
| standard_delivery_days | INT | - | No | Estimasi normal waktu tempuh dalam hari |

## 5. `shipments` (fact table)

| Kolom | Tipe Data | Key | Nullable | Keterangan |
|---|---|---|---|---|
| shipment_id | INT | PK | No | ID unik pengiriman |
| customer_id | INT | FK -> customers.customer_id | No | Pelanggan pemesan |
| courier_id | INT | FK -> couriers.courier_id | No | Kurir yang menangani |
| route_id | INT | FK -> routes.route_id | No | Rute yang dilalui |
| shipment_date | DATE | - | No | Tanggal pengiriman dibuat |
| package_weight_kg | DECIMAL(5,2) | - | No | Berat paket |
| shipping_cost | DECIMAL(10,2) | - | No | Biaya pengiriman |
| estimated_delivery_date | DATE | - | No | Estimasi tanggal tiba (ETA) |
| actual_delivery_date | DATE | - | No | Tanggal tiba aktual |
| shipment_status | VARCHAR(20) | - | No | On-Time atau Delayed |

## Relasi Antar Tabel

```
warehouses (1) ---- (N) couriers
warehouses (1) ---- (N) routes (sebagai origin)
warehouses (1) ---- (N) routes (sebagai destination)
customers  (1) ---- (N) shipments
couriers   (1) ---- (N) shipments
routes     (1) ---- (N) shipments
```

Satu `shipment` selalu terhubung ke tepat satu `customer`, satu `courier`, dan satu `route`. Relasi ini menjadi dasar penyusunan ERD dan query join pada tahap SQL.

## Catatan Desain: Normalisasi

Struktur 5 tabel ini dirancang langsung dalam bentuk ternormalisasi (3NF), bukan hasil pemecahan dari satu tabel besar. Beberapa keputusan desain yang mencerminkan hal ini:

- Tidak ada data warehouse (city, region, kapasitas) yang disimpan berulang di tabel `shipments`, `couriers`, atau `routes`. Data tersebut hanya disimpan sekali di `warehouses`, dan diakses lewat `warehouse_id` (FK).
- Tidak ada data customer/courier yang diduplikasi di `shipments`. Setiap shipment cukup menyimpan `customer_id` dan `courier_id`, detail lengkapnya diambil lewat join ke tabel masing-masing.
- Setiap tabel memiliki primary key tunggal dan seluruh kolom non-key bergantung penuh pada key tersebut, sehingga tidak ada ketergantungan transitif (misalnya `city` bergantung pada `warehouse_id`, bukan pada `shipment_id`).

Desain ini menghindari redundansi data dan potensi anomali update, misalnya perubahan kapasitas satu warehouse cukup dilakukan di satu baris, bukan di banyak baris shipment.