import streamlit as st
import json
from services.requestUtils import getGeneratedImage

st.title('FastAPI ML Model Serving App')
with st.form(key='my_form'):
    textPrompt:str =st.text_area('Enter the Your Image generating Text')
    print(textPrompt)
    response = getGeneratedImage(textPrompt)
    print(response)
    st.form_submit_button('Generate')

st.header('Image Result from Model')    

st.write(response['Hello'])

#st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")