🥗✨ AI Nutrition Deficiency Predictor + Intelligent Food Recommendation System

A Data Science + Machine Learning + Streamlit Project

🌟 Project Summary

This project continues my earlier AI-Based Nutrient Deficiency Predictor, expanding it into a complete Nutritional Intelligence System.

Phase 1 analyzed user food intake patterns and predicted likely nutrient gaps.
Phase 2 (this repo) now introduces an AI-powered food recommendation engine that suggests foods rich in the nutrients the user is missing — customized by region, cuisine, and dietary preferences.

Together, they form an end-to-end health-focused ML system that connects prediction → recommendation → action.

🧠 Core Features
🔍 1. Nutrient Deficiency Prediction

* ML model identifies potential deficiencies based on food intake

* Uses engineered nutrient features

* Helps users understand their dietary gaps

🍽️ 2. Intelligent Food Recommendations

Recommends foods rich in the nutrients the user lacks

Filters include:
- Cuisine

- Dietary preference (e.g., vegan, low-fat, etc.)

Uses cosine similarity + nutrient vector matching

🌐 3. Interactive Streamlit Application

* Clean UI for predictions & recommendations

* Fast and lightweight

* Easy to deploy and share


🔧 Tech Stack
Data Science & Machine Learning

* Python

* Pandas

* NumPy

* Scikit-learn

* Feature scaling & vectorization

Application Development

* Streamlit

* Joblib (model persistence)

Deployment

* GitHub

* Streamlit Cloud

 🗂️ Project Structure
├── app.py                   
├── nutrient7_model_compressed.joblib                
├── foods.csv            
├── requirements.txt         
└── README.md                


📊 How It Works
1️⃣ User provides intake / deficiency inputs
2️⃣ ML model predicts likely nutrient gaps
3️⃣ System matches user deficits with foods rich in missing nutrients
4️⃣ Recommendations are refined using selected filters
5️⃣ Final suggestions displayed with nutrient highlights

🚀 Live Demo
I will update this section with the live link.


📚 Use Cases

* Personal health and wellness tracking

* Diet planning

* Campus/academic machine learning showcase

* Recommendation system portfolio project

* Nutrition tech prototype

  🎯 Why This Project Matters

Nutrition is deeply personal and often confusing.
By combining data science, ML, and real-world nutrition knowledge, this system helps users move from:
“What am I lacking?” → “What should I eat next?”

It demonstrates:
* End-to-end ML product development

* Clean UI implementation

* Practical recommendation systems

* Data engineering + feature design

* Deployment experience

🧩 Future Improvements

* Add user profiles & history tracking

* Add calorie-based recommendations

* Expand the dataset with more foods

* Use collaborative filtering for personalized suggestions

* Integrate with a mobile UI

💬 Feedback & Contributions

Feel free to open issues or contribute!
I’m actively improving this project.
