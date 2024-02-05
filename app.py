from dotenv import load_dotenv
load_dotenv() ## Load all the environment variables from .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro vision
model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Question Paper Solver")

st.title("Gemi✍️ A Question Paper Solver📝")
st.write("Welcome to Gemi✍️! Provide question/Paper and get answers📝.")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose an image of the Question Paper...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)

submit=st.button("Submit")

input_prompt="""
Act as a expert in understanding images of question paper . we will uploaded a images of question paper
and you will have to answer any question in details based on the uploaded question paper image  """

## If submit button  is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000000; /* Black background color */
    color: #ffffff; /* White text color */
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="footer">Unlock the power of Question Paper Solver📝 with Gemi✍️, your trusted question-paper solver📝 fueled by Gemini.</p>', unsafe_allow_html=True)