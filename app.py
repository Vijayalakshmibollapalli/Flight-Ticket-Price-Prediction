import streamlit as st
import pandas as pd
import pickle
import base64

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Flight Ticket Price Prediction",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------
def get_base64(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

bg_image = get_base64("Pic.webp")

# ---------------- CSS STYLING ----------------
st.markdown(
    f"""
    <style>

    /* ---------- BACKGROUND IMAGE ---------- */
    .stApp {{
        background:
        linear-gradient(rgba(255,255,255,0.75),
        rgba(255,255,255,0.75)),
        url("data:image/png;base64,{bg_image}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* ---------- TITLE ---------- */
    .title {{
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: black;
        margin-bottom: 30px;
    }}

    /* ---------- SUBHEADINGS ---------- */
    h3 {{
        color: black !important;
        font-size: 24px !important;
        font-weight: bold !important;
    }}

    /* ---------- BUTTON ---------- */
    .stButton {{
        text-align: left;
    }}

    .stButton>button {{
        width: 300px;
        height: 50px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        background-color: #ff4b4b;
        color: white;
    }}

    .stButton>button:hover {{
        background-color: #e63c3c;
        color: white;
    }}

    /* ---------- INPUT BOXES ---------- */
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput input {{
        background-color: #FFFFFF;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
    }}

    /* ---------- LABEL COLOR ---------- */
    .stSelectbox label,
    .stNumberInput label,
    .stSlider label,
    .stMarkdown p {{
        color: #374151 !important;
        font-weight: 600 !important;
    }}

    /* ---------- TEXT INSIDE INPUT BOXES ---------- */
    .stSelectbox div[data-baseweb="select"] span,
    .stNumberInput input {{
        color: #111827 !important;
        font-weight: 500;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown(
    "<div class='title'>✈️ Flight Ticket Price Prediction</div>",
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("Flight Ticket Price Prediction.pkl", "rb"))

# ---------------- LOAD DATA ----------------
df = pd.read_csv("final_flight_dataset.csv")

# ---------------- COLUMNS ----------------
col1, col2, col3 = st.columns(3)

# ---------------- COLUMN 1 ----------------
with col1:
    st.subheader("Flight Details")

    airline = st.selectbox("**Airline**", sorted(df["airline"].unique()))
    source = st.selectbox("**Source**", sorted(df["source"].unique()))
    destination = st.selectbox("**Destination**", sorted(df["destination"].unique()))
    stop = st.selectbox("**Number of Stops**", sorted(df["stop"].unique()))

# ---------------- COLUMN 2 ----------------
with col2:
    st.subheader("Travel Details")

    travel_class = st.selectbox("**Class**", sorted(df["class"].unique()))
    day_type = st.selectbox("**Day Type**", ["weekday", "weekend"])
    month_name = st.selectbox("**Month**", sorted(df["month_name"].unique()))

# ---------------- COLUMN 3 ----------------
with col3:
    st.subheader("Time Details")

    departure_hour = st.slider("**Departure Hour**", 0, 23, 10)
    departure_min = st.slider("**Departure Minute**", 0, 59, 0)
    arrival_hour = st.slider("**Arrival Hour**", 0, 23, 12)
    arrival_min = st.slider("**Arrival Minute**", 0, 59, 0)

    duration_mins = st.number_input(
        "**Duration (minutes)**",
        min_value=30,
        max_value=3000,
        value=120
    )

# ---------------- INPUT DATA ----------------
input_df = pd.DataFrame([[
    airline, source, stop, destination, travel_class,
    day_type, month_name, departure_hour,
    departure_min, duration_mins,
    arrival_hour, arrival_min
]],
columns=[
    "airline", "source", "stop", "destination", "class",
    "day_type", "month_name", "departure_hour", "departure_min",
    "duration_mins", "arrival_hour", "arrival_min"
])

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):

    prediction = model.predict(input_df)

    st.markdown(
        f"""
        <div style="
            text-align:left;
            margin-top:20px;
            color:black;
            font-size:22px;
            font-weight:bold;
        ">
            Estimated Flight Ticket Price: ₹ {int(prediction[0]):,}
        </div>
        """,
        unsafe_allow_html=True
    )