import streamlit as st
import pandas as pd
import joblib

# Load model SVM hasil training
model = joblib.load("svm_model.pkl")

st.title("Fraud Detection dengan SVM")

# 1. Upload file Excel
uploaded_file = st.file_uploader("Upload file Excel dengan kolom V1-V28 dan Amount", type=["xlsx", "xls"])

if uploaded_file is not None:
    # 2. Baca Excel
    df = pd.read_excel(uploaded_file)

    # 3. Preview data
    st.write("Preview data (5 baris pertama):")
    st.dataframe(df.head())

    # 4. Tombol prediksi
    if st.button("Prediksi"):
        # Ambil fitur sesuai model
        fitur = [f"V{i}" for i in range(1, 29)] + ["Amount"]
        X = df[fitur]

        # Prediksi label
        y_pred = model.predict(X)

        # Prediksi probabilitas (kolom 1 = fraud)
        y_prob = model.predict_proba(X)[:, 1]

        # Kategori probabilitas
        def kategori_prob(p):
            if p < 0.3: return "Low"
            elif p <= 0.7: return "Medium"
            else: return "High"

        # Kategori amount
        def kategori_amount(a):
            if a < 20: return "Low"
            elif a <= 500: return "Medium"
            else: return "High"

        # Risk matrix logic
        def kategori_risk(p, a):
            if p > 0.95:
                return "High Risk"
            elif p > 0.7 and a > 500:
                return "High Risk Fraud"
            elif p >= 0.3:
                return "Medium Risk"
            else:
                return "Low Risk"

        hasil_df = pd.DataFrame({
            "Hasil": ["Fraud" if val==1 else "Normal" for val in y_pred],
            "Probabilitas Fraud": y_prob,
            "Kategori Probabilitas": [kategori_prob(p) for p in y_prob],
            "Amount": df["Amount"],
            "Kategori Risk": [kategori_risk(p,a) for p,a in zip(y_prob, df["Amount"])]
        })

        st.write("Hasil Prediksi:")
        st.dataframe(hasil_df)

        # Rekomendasi operasional
        st.subheader("Rekomendasi Keputusan")
        st.markdown("""
        - **High Risk Fraud** → Blokir otomatis (probabilitas tinggi + nominal besar).  
        - **Medium Risk Fraud** → Tantangan ekstra / verifikasi (misalnya OTP atau scan wajah).  
        - **Low Risk** → Lolos otomatis, transaksi diproses instan.  
        """)
