
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# FILE PATHS
# -----------------------------------
base_path = Path(__file__).parent.parent
model_path = Path(__file__).parent / "car_price_model.pkl"
dataset_path = base_path / "data" / "car data.csv"

# Load model and dataset
model = joblib.load(model_path)
df = pd.read_csv(dataset_path)

car_names = sorted(df["Car_Name"].dropna().unique())

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f1f4ff;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1500px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #061b3d, #102f60);
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Sidebar title */
.sidebar-title {
    text-align: center;
    font-size: 30px !important;
    font-weight: 800 !important;
    padding: 20px 0;
    line-height: 1.5;
}

/* Navigation heading */
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    font-size: 19px !important;
    font-weight: bold !important;
}

/* Home, About and Insights */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size: 18px !important;
    font-weight: 600 !important;
    padding: 8px 0 !important;
}

/* Sidebar paragraph text */
section[data-testid="stSidebar"] p {
    font-size: 17px !important;
    font-weight: 600 !important;
}

/* Sidebar radio buttons */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 12px;
}

/* Header banner */
.hero {
    background: linear-gradient(110deg, #061b45, #0758b5);
    padding: 35px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.12);
}

.hero h1 {
    color: white;
    font-size: 40px;
    margin-bottom: 5px;
}

.hero p {
    color: #dbeafe;
    font-size: 18px;
    margin-bottom: 0;
}

/* Section heading */
.section-heading {
    color: #092b62;
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Form card */
div[data-testid="stForm"] {
    background: white;
    border: 1px solid #d8e3ff;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 4px 15px rgba(20,50,100,0.07);
}

/* Predict button */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #087cff, #0754c7);
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-size: 17px;
    font-weight: bold;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #0647a8;
    color: white;
}

/* Result card */
.result-card {
    background: linear-gradient(110deg, #d9fbe5, #effff3);
    border: 1px solid #9ae6b4;
    border-radius: 16px;
    padding: 25px;
    margin-top: 20px;
    text-align: center;
}

.result-card h2 {
    color: #08752f;
    font-size: 27px;
}

.result-card h1 {
    color: #07832f;
    font-size: 48px;
    margin: 10px;
}

.result-card p {
    color: #075c2a;
    font-size: 17px;
}

/* Technology badges */
.tech-badge {
    display: inline-block;
    background: #e5edff;
    color: #0754bd;
    padding: 9px 15px;
    border-radius: 20px;
    margin: 5px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: #17366b;
    padding: 20px;
    background: #e1eaff;
    border-radius: 12px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.markdown("""
<div class="sidebar-title">
    🚘<br>
    Car Price Predictor
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["🏠 Home", "ℹ️ About", "📊 Insights"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="
    text-align:center;
    font-size:20px;
    font-weight:bold;
    line-height:1.6;
    padding:15px 5px;
">
    Drive Smart...<br>
    Sell Better! 🚗
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# HOME PAGE
# -----------------------------------
if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🚗 Used Car Price Prediction</h1>
        <p>Machine Learning Based Car Price Estimator</p>
        <p>🚘 Find the estimated value of your used car easily</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">🚘 Enter Car Details</div>',
        unsafe_allow_html=True
    )

    with st.form("car_prediction_form"):

        col1, col2 = st.columns(2)

        with col1:

            car_name = st.selectbox(
                "🚘 Car Name",
                car_names
            )

            year = st.number_input(
                "📅 Manufacturing Year",
                min_value=2003,
                max_value=2018,
                value=2015
            )

            present_price = st.number_input(
                "💰 Present Price (Lakhs)",
                min_value=0.1,
                value=5.0,
                step=0.1
            )

            kms_driven = st.number_input(
                "🛣️ Kilometres Driven",
                min_value=0,
                value=30000,
                step=1000
            )

        with col2:

            fuel_type = st.selectbox(
                "⛽ Fuel Type",
                ["Petrol", "Diesel", "CNG"]
            )

            seller_type = st.selectbox(
                "👤 Seller Type",
                ["Dealer", "Individual"]
            )

            transmission = st.selectbox(
                "⚙️ Transmission",
                ["Manual", "Automatic"]
            )

            owner = st.selectbox(
                "👥 Previous Owners",
                [0, 1, 3]
            )

        submitted = st.form_submit_button(
            "🔍 Predict Car Price",
            use_container_width=True
        )

    # Prediction
    if submitted:

        input_data = pd.DataFrame([{
            "Year": year,
            "Present_Price": present_price,
            "Kms_Driven": kms_driven,
            "Fuel_Type": fuel_type,
            "Seller_Type": seller_type,
            "Transmission": transmission,
            "Owner": owner
        }])

        prediction = model.predict(input_data)[0]

        st.markdown(f"""
        <div class="result-card">
            <h2>✅ Prediction Result</h2>
            <p>Estimated Selling Price</p>
            <h1>₹ {prediction:.2f} Lakhs</h1>
            <p>🚘 Selected Car: {car_name}</p>
        </div>
        """, unsafe_allow_html=True)

        st.info(
            "Note: This is an estimated price generated by a "
            "machine learning model. Actual selling prices may vary."
        )

    # About project section
    st.markdown("---")

    st.markdown("### ℹ️ About This Project")

    st.write(
        "Used Car Price Prediction System uses Machine Learning "
        "to estimate the selling price of a used car."
    )

    st.markdown("**Technologies Used:**")

    st.markdown("""
    <span class="tech-badge">🐍 Python</span>
    <span class="tech-badge">🐼 Pandas</span>
    <span class="tech-badge">📊 Scikit-learn</span>
    <span class="tech-badge">🎈 Streamlit</span>
    <span class="tech-badge">🌳 Random Forest</span>
    """, unsafe_allow_html=True)

# -----------------------------------
# ABOUT PAGE
# -----------------------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.write("""
    ### Used Car Price Prediction System

    This project predicts the estimated selling price of a used car
    using a Machine Learning model.

    **Project Workflow:**

    1. Data Collection
    2. Data Cleaning and Preprocessing
    3. Exploratory Data Analysis
    4. Model Training
    5. Price Prediction Using Streamlit
    """)

    st.subheader("Technologies Used")

    st.write(
        "Python, Pandas, NumPy, Matplotlib, Seaborn, "
        "Scikit-learn, Random Forest and Streamlit."
    )

# -----------------------------------
# INSIGHTS PAGE
# -----------------------------------
elif page == "📊 Insights":

    st.title("📊 Dataset Insights")

    st.write("Explore the used car dataset.")

    st.metric("Total Cars", len(df))

    st.metric(
        "Average Selling Price",
        f"₹ {df['Selling_Price'].mean():.2f} Lakhs"
    )

    st.metric(
        "Average Present Price",
        f"₹ {df['Present_Price'].mean():.2f} Lakhs"
    )

    st.subheader("Selling Price Distribution")

    st.bar_chart(df["Selling_Price"].value_counts().sort_index())

    st.subheader("Fuel Type Distribution")

    st.bar_chart(df["Fuel_Type"].value_counts())

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("""
<div class="footer">
    🚗 Developed as a Data Science Machine Learning Project 🚗
    <br>
    Used Car Price Prediction System
</div>
""", unsafe_allow_html=True)
