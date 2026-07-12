# Industry Research

## 1. Industry Overview

Industri logistik/ekspedisi memegang peran penting dalam distribusi barang pada perekonomian modern. Logistik bukan sekadar "antar barang". Akan tetapi, menentukan kepuasan pelanggan akhir, biaya operasional bisnis, dan reputasi merek yang menitipkan pengirimannya.

Karakteristik umum industri ini secara global maupun lokal:
- **Volume tinggi, margin tipis**: perusahaan ekspedisi bersaing di harga, sehingga efisiensi operasional menjadi kunci profitabilitas.
- **Last-mile delivery** adalah titik paling mahal dan paling rawan masalah dalam rantai pengiriman (macet kota, alamat tidak jelas, keterbatasan kurir).
- **Ketepatan waktu (on-time delivery)** menjadi diferensiator kompetitif utama, karena pelanggan modern, khususnya di e-commerce, sangat sensitif terhadap kecepatan pengiriman.
- **Musiman (seasonality)**: permintaan melonjak pada periode tertentu (promo belanja, hari raya, akhir tahun), yang menuntut fleksibilitas kapasitas operasional.

## 2. Logistics Industry in Indonesia

Di Indonesia, pertumbuhan e-commerce (Shopee, Tokopedia, TikTok Shop, dll.) secara langsung meningkatkan kompleksitas supply chain: volume pengiriman meningkat tajam, cakupan wilayah operasional meluas hingga ke luar kota/pulau, dan ekspektasi pelanggan terhadap kecepatan pengiriman terus naik.

Beberapa pemain utama dan positioning mereka:

| Perusahaan | Karakteristik Umum |
|---|---|
| JNE | Jaringan cabang terluas, kuat di layanan reguler & YES (kilat) |
| J&T Express | Fokus otomasi sortir, kuat di segmen e-commerce |
| SiCepat | Agresif di harga & promo, kuat di last-mile perkotaan |
| Anteraja, Ninja Xpress, dll | Pemain menengah, sering menjadi partner marketplace |

Dalam konteks ini, **NusaLog Express** (perusahaan fiktif pada proyek ini) diposisikan sebagai pemain menengah yang ingin bersaing bukan lewat perang harga, melainkan lewat **keunggulan operasional berbasis data**, sebuah strategi yang semakin relevan di pasar logistik Indonesia yang padat pemain namun tipis diferensiasi layanan.

## 3. Current Challenges

Berdasarkan riset terhadap pola umum industri ekspedisi, terdapat empat tantangan utama yang paling relevan dengan studi kasus:

1. **Keterlambatan pengiriman (delivery delay)**: banyak perusahaan masih bersifat reaktif, baru menyadari keterlambatan setelah komplain pelanggan masuk, bukan mendeteksinya secara proaktif.
2. **Tingginya biaya operasional**: biaya per pengiriman sulit dipantau secara granular per rute atau cabang, sehingga inefisiensi sulit diidentifikasi.
3. **Kurangnya visibilitas pengiriman**: manajemen umumnya tidak memiliki dashboard real-time untuk memantau performa cabang, kurir, maupun rute secara menyeluruh.
4. **Ketidakseimbangan kapasitas gudang & kurir**: sebagian kurir/cabang mengalami overload sementara yang lain kurang termanfaatkan, karena alokasi masih dilakukan manual tanpa mempertimbangkan pola historis.

## 4. Technology Trends

Beberapa tren teknologi yang relevan dan mulai banyak diadopsi di industri logistik:

- **Machine learning untuk delay prediction**: memprediksi risiko keterlambatan sebelum pengiriman terjadi, memungkinkan tindakan mitigasi proaktif.
- **Dashboard operasional real-time** (Power BI/Tableau) untuk pemantauan KPI cabang dan pengambilan keputusan yang lebih cepat.
- **Data pipeline terstruktur (ETL)**: memastikan data operasional mengalir secara konsisten dan andal dari sumber mentah ke sistem analitik.
- **Route optimization** berbasis data historis, meskipun ini umumnya menjadi fase lanjutan yang lebih kompleks di luar MVP awal.

## 5. Project Focus

Dari empat tantangan yang teridentifikasi, proyek **NusaLog Express Analytics** memilih fokus pada **keterlambatan pengiriman**, dengan alasan:

- Berdampak **paling langsung** terhadap kepuasan pelanggan, ini adalah hal pertama yang dirasakan end-customer.
- Berdampak **paling langsung** terhadap biaya operasional, melalui penalti SLA, komplain, dan biaya re-delivery.
- Dapat diminimalkan melalui pendekatan data end-to-end yang natural, melibatkan tiga peran sekaligus:
  - **Data Engineering**: menyusun database dan data pipeline yang rapi dan dapat diandalkan.
  - **Data Analyst**: membangun dashboard untuk memantau performa pengiriman secara berkelanjutan.
  - **Data Scientist**: membangun model prediktif untuk mendeteksi risiko keterlambatan sebelum terjadi.

Fokus ini menjadi dasar penyusunan business case, KPI, dan requirement proyek pada dokumen-dokumen selanjutnya.

## 6. Conclusion

Pertumbuhan e-commerce di Indonesia mendorong industri logistik untuk terus meningkatkan efisiensi dan keandalan layanan. Di antara berbagai tantangan yang ada, keterlambatan pengiriman berdiri sebagai masalah dengan dampak bisnis paling signifikan dan paling dapat diukur menggunakan data. Proyek ini dirancang untuk mendemonstrasikan bagaimana pendekatan data end-to-end, mulai dari perancangan data hingga prediksi berbasis machine learning, dapat membantu perusahaan logistik seperti NusaLog Express mengubah pendekatan operasionalnya dari reaktif menjadi proaktif.