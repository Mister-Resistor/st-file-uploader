import base64
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


uploaded_files = st.file_uploader(
    "Choose a PDF file",
    accept_multiple_files=True,
    type=['pdf']
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()

    st.write("filename:", uploaded_file.name)
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
    
    pdf_viewer(input=uploaded_file)

    
    # pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    # st.markdown(pdf_display, unsafe_allow_html=True)
