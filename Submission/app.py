import streamlit as st
import pandas as pd
import joblib
from mapping import *  

# Load model, scaler, dan urutan fitur
model = joblib.load("model_logreg.pkl")
scaler = joblib.load("scaler_model.pkl")
feature_names = joblib.load("feature_names.pkl")  # list fitur asli

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")
st.markdown("""
Aplikasi ini digunakan untuk memprediksi kemungkinan dropout berdasarkan data akademik dan sosiodemografi mahasiswa.
Silakan lengkapi data berikut ini:
""")

# Form input user
with st.form("dropout_form"):
    marital_status = st.selectbox("Status Pernikahan", list(marital_status_map.keys()))
    gender = st.radio("Gender", list(gender_map.keys()))
    age = st.number_input("Usia Saat Mendaftar", min_value=15, max_value=100, step=1)
    application_order = st.slider("Urutan Pilihan Masuk", 0, 9, 1)
    daytime = st.radio("Attendance", list(daytime_map.keys()))
    prev_qual = st.selectbox("Kualifikasi Sebelumnya", list(mother_qual_map.keys()))
    prev_qual_grade = st.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, step=0.5)
    admission_grade = st.slider("Nilai Masuk", 0.0, 200.0, step=0.5)
    m_qual = st.selectbox("Kualifikasi Ibu", list(mother_qual_map.keys()))
    f_qual = st.selectbox("Kualifikasi Ayah", list(father_qual_map.keys()))
    m_occ = st.selectbox("Pekerjaan Ibu", list(mother_occ_map.keys()))
    f_occ = st.selectbox("Pekerjaan Ayah", list(father_occ_map.keys()))
    debtor = st.selectbox("Menunggak Biaya?", list(yes_no_map.keys()))
    tuition_paid = st.selectbox("Biaya Terbayar?", list(yes_no_map.keys()))
    scholarship = st.selectbox("Penerima Beasiswa?", list(yes_no_map.keys()))

    # Fitur semester 1 yang relevan
    cu_enrolled = st.slider("Jumlah Mata Kuliah Diambil (1st Sem)", 0, 20, step=1)
    cu_eval = st.slider("Jumlah Dievaluasi (1st Sem)", 0, 20, step=1)
    cu_approved = st.slider("Jumlah Lulus (1st Sem)", 0, 20, step=1)
    cu_grade = st.slider("Nilai Rata-rata (1st Sem)", 0.0, 20.0, step=0.1)

    submitted = st.form_submit_button("Prediksi")

if submitted:
    # Ubah input menjadi format numerik
    data = {
        'Marital_status': marital_status_map[marital_status],
        'Application_order': application_order,
        'Daytime_evening_attendance': daytime_map[daytime],
        'Previous_qualification': mother_qual_map[prev_qual],
        'Previous_qualification_grade': prev_qual_grade,
        'Mothers_qualification': mother_qual_map[m_qual],
        'Fathers_qualification': father_qual_map[f_qual],
        'Mothers_occupation': mother_occ_map[m_occ],
        'Fathers_occupation': father_occ_map[f_occ],
        'Admission_grade': admission_grade,
        'Debtor': yes_no_map[debtor],
        'Tuition_fees_up_to_date': yes_no_map[tuition_paid],
        'Gender': gender_map[gender],
        'Scholarship_holder': yes_no_map[scholarship],
        'Age_at_enrollment': age,
        'Curricular_units_1st_sem_enrolled': cu_enrolled,
        'Curricular_units_1st_sem_evaluations': cu_eval,
        'Curricular_units_1st_sem_approved': cu_approved,
        'Curricular_units_1st_sem_grade': cu_grade,
    }

    input_df = pd.DataFrame([data])

    # Susun dan scaling sesuai fitur pelatihan
    input_ordered = input_df[feature_names]
    input_scaled = scaler.transform(input_ordered)


    # Prediksi dan tampilkan hasil
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Hasil Prediksi:")
    st.markdown("---")
    if prediction == 1:
        st.error(f"⚠️ Mahasiswa berisiko dropout. Probabilitas: {probability:.2f}")
    else:
        st.success(f"✅ Mahasiswa diprediksi akan bertahan. Probabilitas dropout: {probability:.2f}")

st.markdown("""
---
**© 2025 Jaya Jaya Institut AI Lab**  
""")
