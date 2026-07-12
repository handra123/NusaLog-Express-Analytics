# Business Understanding

## 1. Company Profile

**NusaLog Express** adalah perusahaan ekspedisi domestik fiktif yang melayani pengiriman barang untuk segmen e-commerce, UMKM, dan retail di Indonesia.

**Skala operasional:**

| Aspek | Keterangan |
|---|---|
| Jumlah cabang/gudang | 15 cabang (Jawa dan Sumatra) |
| Jumlah kurir aktif | 300 kurir |
| Volume pengiriman | ± 8.000 paket/bulan |
| Armada | Motor (last-mile), mobil box (antar kota), truk (antar provinsi) |

**Area operasional:** Jawa dan Sumatra, dengan rencana ekspansi ke Kalimantan dan Sulawesi.

**Model bisnis:** B2B2C, kerja sama dengan marketplace dan UMKM, plus layanan reguler untuk individu.

## 2. Business Problem

NusaLog Express menghadapi empat masalah operasional utama:

1. **Keterlambatan pengiriman.** Sebagian paket tiba melewati estimasi waktu (ETA), memicu komplain pelanggan dan penalti dari mitra marketplace.
2. **Biaya operasional tinggi.** Biaya per pengiriman belum terpantau secara rinci per rute atau cabang, sehingga sumber pemborosan sulit diidentifikasi.
3. **Kurangnya visibilitas operasional.** Manajemen tidak memiliki dashboard yang menampilkan performa cabang, kurir, dan rute secara real-time.
4. **Ketidakseimbangan beban gudang dan kurir.** Sebagian cabang/kurir kelebihan beban, sebagian lain kurang termanfaatkan, karena alokasi masih manual.

Proyek ini fokus menyelesaikan masalah pertama (keterlambatan pengiriman), karena dampaknya paling langsung terhadap kepuasan pelanggan dan biaya operasional, sekaligus paling mudah diukur dan dianalisis dengan data.

## 3. Project Objectives

| Objective | Peran |
|---|---|
| Membangun database ekspedisi yang terstruktur | Data Engineering |
| Membangun ETL pipeline (extract, transform, load) | Data Engineering |
| Melakukan analisis SQL untuk KPI operasional | Data Analyst |
| Membangun dashboard Power BI | Data Analyst |
| Membangun model prediksi keterlambatan pengiriman | Data Scientist |
| Menyusun rekomendasi bisnis berbasis hasil analisis | Data Analyst & Data Scientist |

## 4. Business Process

Alur pengiriman NusaLog Express, dari pesanan masuk hingga barang diterima pelanggan:

```
Customer (order dibuat)
        ↓
Pickup (paket diambil dari pengirim)
        ↓
Warehouse (paket masuk ke cabang asal)
        ↓
Sorting (paket disortir berdasarkan tujuan)
        ↓
Transportation (pengiriman antar cabang/kota)
        ↓
Destination Warehouse (paket tiba di cabang tujuan)
        ↓
Last Mile Delivery (kurir mengantar ke alamat pelanggan)
        ↓
Performance Evaluation (On-Time / Delayed)
```

Setiap tahap di atas berpotensi menjadi titik penyebab keterlambatan, dan akan menjadi dasar penentuan fitur pada tahap analisis dan machine learning.

## 5. Project Scope

**Termasuk dalam proyek:**
- Pengiriman domestik (antar kota/provinsi di Jawa dan Sumatra).
- Analisis performa operasional (on-time rate, biaya, beban kurir).
- Prediksi keterlambatan berbasis data historis.
- Dashboard dan rekomendasi bisnis.

**Tidak termasuk dalam proyek:**
- Optimasi rute real-time (vehicle routing problem).
- Tracking GPS real-time.
- Integrasi sistem produksi/API pihak ketiga.
- Pengiriman internasional.

## 6. Success Criteria

Proyek dianggap berhasil jika:

- Database ekspedisi berhasil dibangun dan dapat direproduksi dari script SQL.
- ETL pipeline berjalan dari data mentah hingga masuk ke database.
- Dashboard Power BI menampilkan KPI utama secara jelas dan mudah dibaca.
- Model machine learning memiliki performa yang baik dan dapat dijelaskan (interpretable).
- Rekomendasi bisnis dihasilkan berdasarkan insight data, bukan asumsi.