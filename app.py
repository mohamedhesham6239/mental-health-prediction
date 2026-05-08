import streamlit as st
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("🧠 Mental Health Prediction App")
st.write("Fill the details below:")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])

family_history = st.selectbox(
    "Family History",
    ["Yes", "No"]
)

mood_swings = st.selectbox(
    "Mood Swings",
    ["Low", "Medium", "High"]
)

work_interest = st.selectbox(
    "Work Interest",
    ["Low", "Medium", "High"]
)

stress = st.slider("Stress Level", 0, 10, 5)
days_indoors = st.slider("Days Indoors", 0, 30, 5)

# Create empty dictionary based on training columns
data = dict.fromkeys(columns, 0)

# Map categorical inputs
gender_col = f"Gender_{gender}"
family_col = f"FamilyHistory_{family_history}"
mood_col = f"MoodSwings_{mood_swings}"
work_col = f"WorkInterest_{work_interest}"

if gender_col in data:
    data[gender_col] = 1

if family_col in data:
    data[family_col] = 1

if mood_col in data:
    data[mood_col] = 1

if work_col in data:
    data[work_col] = 1

# Numerical values
if "IncreasingStress" in data:
    data["IncreasingStress"] = stress

if "DaysIndoors" in data:
    data["DaysIndoors"] = days_indoors

# Predict
if st.button("Predict"):

    sample = pd.DataFrame([data])

    # FIX: align features with training
    sample = sample.reindex(columns=columns, fill_value=0)

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("⚠️ Needs Treatment")
    else:
        st.success("✅ No Treatment Needed")
