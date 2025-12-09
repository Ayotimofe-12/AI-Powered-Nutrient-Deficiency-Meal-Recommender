import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load model and dataset
# ==========================
model = joblib.load("nutrient7_model_compressed.joblib")

foods = pd.read_csv("foods.csv")

# ==========================
# FIX 1: Normalize Column Names
# ==========================
foods.columns = foods.columns.str.strip().str.lower()

# If your CSV uses "region", convert it to "cuisine"
if "region" in foods.columns and "cuisine" not in foods.columns:
    foods.rename(columns={"region": "cuisine"}, inplace=True)

# Ensure string columns behave well
if "cuisine" in foods.columns:
    foods["cuisine"] = foods["cuisine"].astype(str)
else:
    st.error("Your foods.csv file is missing a cuisine/region column")

if "tags" in foods.columns:
    foods["tags"] = foods["tags"].astype(str)
else:
    foods["tags"] = ""    # Safe fallback

# ==========================
# Prediction Function
# ==========================
def predict_deficiency(feature_vector):
    """
    Takes a numeric feature vector of size 14 and predicts nutrient deficiency.
    """
    prediction = model.predict([feature_vector])[0]   # output = array of probs
    nutrient_map = {
        0: "Vitamin C",
        1: "Vitamin B12",
        2: "Selenium",
        3: "Calcium",
        4: "Protein",
        5: "Fibre",
        6: "Total Fat"
    }
    return nutrient_map[prediction.argmax()]

# ==========================
# Meal Recommendation Function
# ==========================
def recommend_food(deficiency, top_n=5, cuisine_filter=None, dietary_filter=None):
    nutrient_column_map = {
        "Vitamin C": "vitamin_c_mg",
        "Vitamin B12": "b12_µg",
        "Selenium": "selenium_µg",
        "Calcium": "calcium_mg",
        "Protein": "protein_g",
        "Fibre": "fibre_g",
        "Total Fat": "total_fat_g"
    }

    col = nutrient_column_map[deficiency]

    df = foods.copy()

    # Cuisine filter
    if cuisine_filter and cuisine_filter != "All":
        df = df[df["cuisine"].str.lower() == cuisine_filter.lower()]

    # Dietary filter (safe string conversion)
    if dietary_filter and dietary_filter != "All":
        df = df[df["tags"].astype(str).str.lower().str.contains(dietary_filter.lower())]

    # Sort foods by nutrient content
    df_sorted = df.sort_values(by=col, ascending=False)

    return df_sorted[["name", "cuisine", "serving_size_g", col, "tags", "ingredients"]].head(top_n)

# ==========================
# User Input Form
# ==========================
def get_user_input():
    st.header("Enter Your Health & Diet Info")

    age = st.number_input("Age", 1, 120, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    BMI = st.number_input("BMI", 10.0, 50.0, 22.0)

    fish_seafood = st.number_input("Fish & seafood intake (per week)", 0, 21, 2)
    meat_poultry = st.number_input("Meat & poultry intake (per week)", 0, 21, 3)
    vegetable_servings = st.number_input("Vegetable servings per week", 0, 50, 14)
    fruit_servings = st.number_input("Fruit servings per week", 0, 50, 14)
    dairy_servings = st.number_input("Dairy servings per week", 0, 50, 7)
    legume_servings = st.number_input("Legume servings per week", 0, 21, 4)
    junk_food = st.number_input("Junk/processed food per week", 0, 21, 3)

    activity_level = st.selectbox("Activity level", ["Low", "Moderate", "High"])
    alcohol_intake = st.selectbox("Alcohol intake", ["None", "Occasional", "Regular"])
    smoking_status = st.selectbox("Smoking status", ["Non-smoker", "Occasional", "Regular"])
    fatigue = st.checkbox("Do you often feel fatigue?")

    # Cuisine & Dietary Filters
    cuisine_filter = st.selectbox(
        "Preferred Cuisine",
        ["All", "Nigerian", "Italian", "American", "Indian", "Asian", "Global"]
    )
    dietary_filter = st.selectbox(
        "Dietary Preference",
        ["All", "vegetarian", "vegan", "high-protein", "low-carb", "low-fat"]
    )

    # Encodings
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    activity_map = {"Low": 0, "Moderate": 1, "High": 2}
    alcohol_map = {"None": 0, "Occasional": 1, "Regular": 2}
    smoking_map = {"Non-smoker": 0, "Occasional": 1, "Regular": 2}

    feature_vector = [
        age,
        gender_map[gender],
        BMI,
        fish_seafood,
        meat_poultry,
        vegetable_servings,
        fruit_servings,
        dairy_servings,
        legume_servings,
        junk_food,
        activity_map[activity_level],
        alcohol_map[alcohol_intake],
        smoking_map[smoking_status],
        int(fatigue)
    ]

    return feature_vector, cuisine_filter, dietary_filter

# ==========================
# Streamlit App Layout
# ==========================
st.title("🍽️ AI-Powered Nutrient Deficiency Meal Recommender")

user_vector, cuisine_filter, dietary_filter = get_user_input()

if st.button("Get Meal Recommendations"):
    deficiency = predict_deficiency(user_vector)
    st.success(f"Predicted nutrient deficiency: **{deficiency}**")

    meals = recommend_food(deficiency, cuisine_filter=cuisine_filter, dietary_filter=dietary_filter)

    st.subheader("Recommended Meals")
    st.table(meals)
