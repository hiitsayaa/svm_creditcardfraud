# Implementasi Algoritma Support Vector Machine (SVM) untuk Deteksi Transaksi Fraud pada Kartu Kredit

Proyek ini adalah implementasi *Machine Learning* untuk membangun sistem pendukung keputusan (SPK) deteksi transaksi *fraud* pada kartu kredit. Fokus utama adalah menguji efektivitas algoritma **Support Vector Machine (SVM)** dalam mengatasi masalah *class imbalance* yang ekstrem pada data transaksi.

**Kelas:** Sistem Pendukung Keputusan - C
**Institusi:** Program Studi Sistem Informasi, Fakultas Ilmu Komputer, Universitas Brawijaya (2026)

---

## 💻 Fitur Utama Proyek

1.  **Deteksi *Fraud* dengan SVM:** Implementasi algoritma SVM dengan kernel RBF untuk klasifikasi biner transaksi sah (*non-fraud*) dan penipuan (*fraud*).
2.  **Penanganan *Imbalance Data*:** Penerapan metode *Oversampling* **SMOTE** (*Synthetic Minority Oversampling Technique*) untuk menyeimbangkan kelas minoritas, menghasilkan performa *recall* yang optimal.
3.  ***Hyperparameter Tuning***: Optimasi parameter C dan gamma menggunakan *GridSearchCV* untuk meningkatkan F1-score dan mengurangi jumlah *false negative*.
4.  **Aplikasi Web Interaktif:** *Deployment* model terbaik menggunakan **Streamlit** untuk prediksi *real-time* dan kategorisasi risiko (Low, Medium, High Risk Fraud).

## 📊 Dataset

*   **Nama Dataset:** Credit Card Fraud Detection
*   **Sumber:** Machine Learning Group – ULB (Kaggle)
*   **Jumlah Data:** 284.807 transaksi
*   **Karakteristik:**
    *   Sangat *imbalanced*: Transaksi *fraud* hanya sekitar 0,17% dari total data.
    *   Fitur anonim (V1–V28) hasil transformasi PCA, ditambah fitur `Amount` dan `Time`.

## 🚀 Metodologi dan Algoritma

Proyek ini mengikuti alur kerja (pipeline) yang sistematis:

1.  ***Exploratory Data Analysis* (EDA):** Analisis statistik deskriptif, pengecekan *missing value* (ditemukan 0), dan identifikasi *extreme outlier*.
2.  ***Preprocessing***: Penskalaan fitur `Amount` menggunakan **RobustScaler** untuk mengurangi pengaruh *outlier*.
3.  **Pembagian Data:** Data dibagi 70% untuk *training* dan 30% untuk *testing* secara *stratified*.
4.  ***Imbalance Handling***: Model dilatih dan dievaluasi menggunakan 4 skenario data: *Imbalanced* (Baseline), SMOTE, ADASYN, dan *Random Under-Sampling*.
5.  **Pemodelan & Optimasi:** Model SVM RBF Kernel di-*tuning* menggunakan *GridSearch* pada data hasil SMOTE. Parameter terbaik yang diperoleh adalah **C=10** dan **gamma='scale'**.

### Lingkungan Pengembangan

| Komponen | Detail |
| :--- | :--- |
| **Bahasa Pemrograman** | Python |
| **Library Utama** | scikit-learn, imbalanced-learn, pandas, numpy, matplotlib, seaborn |
| **Platform** | Google Colab (Eksperimen), VS Code (Deployment) |
| **Aplikasi Web** | Streamlit |

## ✅ Hasil dan Evaluasi Model Terbaik

Model akhir yang terpilih adalah kombinasi **SVM + SMOTE + Tuning** karena memberikan keseimbangan terbaik antara *precision* dan *recall*.

| Metrik Evaluasi | Nilai (Data Testing) | Catatan |
| :--- | :--- | :--- |
| **Accuracy** | 99.80% | Akurasi tinggi tidak relevan karena *imbalance*. |
| **Recall** (Key Metric) | **72.97%** | Peningkatan signifikan dalam mendeteksi *fraud*. |
| **Precision** | 45.19% | Menunjukkan 45% transaksi yang diprediksi *fraud* adalah benar-benar *fraud*. |
| **F1-score** | **55.81%** | Meningkat 58% dibandingkan model SMOTE sebelum *tuning*. |
| **AUC** | 92.61% | Kemampuan diskriminasi kelas yang sangat baik. |

### Temuan Operasional

*   Jumlah **False Negative (Fraud yang Lolos)** berhasil ditekan menjadi hanya **40 transaksi**.
*   Rekomendasi diterapkan berdasarkan kategori risiko:
    *   **Low Risk (<30% Probabilitas Fraud):** Auto Approve.
    *   **Medium Risk (30%–70% Probabilitas Fraud):** Verifikasi Tambahan (OTP/Scan Wajah).
    *   **High Risk Fraud (>70% Probabilitas Fraud):** Auto Block/Investigasi Manual.

## 👨‍💻 Kontributor

Proyek ini disusun oleh Kelompok 6:

*   Aqila Noraihana (235150401111057)
*   Fathyya Nahda (235150401111065)
*   Zahrah Athifah Septiani (235150407111068)

**Dosen Pengampu:** Yuita Arum Sari, S.Kom., M.Kom., Ph.D.
