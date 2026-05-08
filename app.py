import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("🧠 Mental Health Prediction App")

st.write("Fill the details below:")


gender = st.selectbox("Gender", ["Male", "Female"])
family_history = st.selectbox("Family History", ["Yes", "No"])
mood_swings = st.selectbox("Mood Swings", ["Low", "Medium", "High"])
work_interest = st.selectbox("Work Interest", ["Low", "Medium", "High"])
stress = st.slider("Stress Level", 0, 10, 5)
days_indoors = st.slider("Days Indoors", 0, 30, 5)


data = dict.fromkeys(columns, 0)

if "Gender_Male" in data and gender == "Male":
    data["Gender_Male"] = 1

if "FamilyHistory_Yes" in data and family_history == "Yes":
    data["FamilyHistory_Yes"] = 1

if "MoodSwings_High" in data and mood_swings == "High":
    data["MoodSwings_High"] = 1

if "WorkInterest_Low" in data and work_interest == "Low":
    data["WorkInterest_Low"] = 1

if "IncreasingStress" in data:
    data["IncreasingStress"] = stress

if "DaysIndoors" in data:
    data["DaysIndoors"] = days_indoors


if st.button("Predict"):
    sample = pd.DataFrame([data])
    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("⚠️ Needs Treatment")
    else:
        st.success("✅ No Treatment Needed")