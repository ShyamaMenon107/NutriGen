#Import required libraries
import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
import google.generativeai as genai
from Nutrifn import prep_image, get_response_nutrition, get_response_diet

# Set page configuration
st.set_page_config(page_title="NutriGen - Nutrition Calculator & Diet Planner", page_icon="🥗", layout="wide")

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Main UI
st.title("NutriGen - Your Personalized Nutrition and Diet Planner")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Nutrition Calculator", "Diet Planner", "Meal Plan", "About", "Contact Us"])

if page == "Home":
    st.header("Welcome to NutriGen!")
    st.write("NutriGen helps you calculate nutrition from an image, plan your diet based on calorie input, and generate meal plans using selected ingredients.")
    st.image("homepage_logo.png", use_column_width=True)
    st.write("Get started by navigating to one of the sections from the sidebar.")

elif page == "Nutrition Calculator":
    st.header("Nutrition Calculator")
    uploaded_file = st.file_uploader("Upload an image of your food to analyse its nutritional value", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Analyse Image 🔍"):
            image_data = prep_image(uploaded_file)
            prompt = """You are an expert nutritionist. As a skilled nutririonist, you are required to analyze the food items in the image and determine the total nutritional value, also provide the details of every food items with calories intake in below format. You may also give just an estimate of its nutritional content if you are not able to guess it correctly, but make sure that the response that you give sounds professional.
            1. Item 1 - number of calories
            2. Item 2 - number of calories
            ......
            ......
            Finally you can also mention whether the food is healthy or not and also mention the percentage split of the ratio of carbohydrates, fats, fibres, sugar and other important nutrients required in our diet"""
            result = get_response_nutrition(image_data, prompt)
            st.write("**Nutritional Information:**")
            st.write(result)

elif page == "Diet Planner":
    st.header("Diet Planner")
    calorie_input = st.number_input("Enter Your Daily Calorie Goal", min_value=1000, max_value=5000, step=100)
    gender = st.selectbox("Select your gender:", ["Male","Female"])
    age_category = st.selectbox("Select your age group:", ["Child", "Teenager", "Adult", "Senior"])
    diseases = st.multiselect("Do you have any of the following diseases? (Select all that apply):",
                                  ["Diabetes", "Hypertension", "Heart Disease", "Asthma", "High Cholesterol", "None"])
    diet_type = st.selectbox("Select Your Diet Type", ["Balanced", "Keto", "Vegan", "Low Carb", "High Protein"])
    if st.button("Generate Diet Plan 📋"):
        prompt = f"Create a {diet_type} diet plan for a daily intake of {calorie_input} calories considering factors such as gender {gender}, age group {age_category} and the following diseases: {', '.join(diseases)}"
        result = get_response_diet(prompt, "")
        st.write("**Diet Plan:**")
        st.write(result)

elif page == "Meal Plan":
    st.header("Meal Plan")
    ingredients = st.text_area("Enter Ingredients (comma-separated)", "")
    if st.button("Generate Meal Plan 🍴"):
        prompt = f"Generate a meal plan using the following ingredients: {ingredients}."
        result = get_response_diet(prompt, "")
        st.write("**Meal Plan:**")
        st.write(result)

elif page == "About":
    st.header("About NutriGen")
    st.write("""Maintaining a healthy lifestyle and proper nutrition is important than ever in today's fast-paced world. However, personalised dietary advice is often expensive and inaccessible to many. The NutriGen bridges this gap by harnessing the power of generative AI to provide tailored nutrition guidance, meal planning, and insights. It is a web application that helps you analyze nutrition, plan diets, and create meal plans with ease. The primary purpose of this app is to assist users in achieving and maintaining healthy eating habits with minimal effort. With the help of Google Gemini models, the app will analyze food images uploaded by users, identify the food items, and calculate their nutritional values and calorie content. The app also offers customised meal plans tailored to individual dietary needs and preferences, ensuring that users receive balanced and nutritious recommendations.""")

elif page == "Contact Us":
    st.header("Contact Us")
    st.write("For any enquiries, please reach out to any:")
    st.write("awantigiradkar1621@gmail.com")
    st.write("dhanashree.s.kengale@gmail.com")
    st.write("kavya061427@gmail.com")
    st.write("mmpeddawad08@gmail.com")
    st.write("menonshyama96@gmail.com")
