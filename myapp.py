import streamlit as st
import google.generativeai as genai

# Set your API key
api_key = "AIzaSyB3x47UoudsF1fHgEvhQXbGIwu5emyybfs"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Streamlit UI: Title, Welcome Message, and User Input
st.title("Healthcare Chatbot")
st.header("Welcome to HealBot")  # Ensure this line displays "Welcome to HealBot"
st.write("Ask a healthcare-related question, and I'll try to answer it.")

# User Input
question = st.text_input("Enter your healthcare question:")

# Initialize response variable
response_text = ""

# Create a function to handle the chatbot response
def get_healthcare_response(question):
    try:
        # Create and start the chat
        model = genai.GenerativeModel("gemini-pro")  # Replace with correct model name
        chat = model.start_chat(history=[])

        # Send the user's question to the chat and get a response
        response = chat.send_message(question)
        
        # Extract the response text
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Trigger the chatbot when the button is clicked
if st.button("Ask"):
    if question:
        response_text = get_healthcare_response(question)
    else:
        response_text = "Please enter a question."

# Display the response
st.write("Answer: ", response_text)
