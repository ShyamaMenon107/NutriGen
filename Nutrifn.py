#Import required libraries
import google.generativeai as genai

# Function to load Google Gemini model and get response for diet planning
def get_response_diet(prompt, input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  
        response = model.generate_content([prompt, input])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to load Google Gemini model and get response for nutrition analysis
def get_response_nutrition(image, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')  
        response = model.generate_content([image[0], prompt])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Preprocess image data
def prep_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file is uploaded!")