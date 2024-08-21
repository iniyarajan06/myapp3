import streamlit as st
import google.generativeai as genai


st.title("Welcome to Gemini Chat")


genai.configure(api_key="AIzaSyB3x47UoudsF1fHgEvhQXbGIwu5emyybfs")

text = st.text_input("Enter your question:")


model = genai.GenerativeModel('gemini-pro')


chat = model.start_chat(history=[])

response_text = ""


if st.button("Click me"):
    if text:
        try:
            response = chat.send_message(text)
            response_text = response.text
        except Exception as e:
            response_text = f"An error occurred: {e}"
    else:
        response_text = "Please enter a question."

# Display the response in the Streamlit app
st.write(response_text)
