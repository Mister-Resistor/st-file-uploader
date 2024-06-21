import streamlit as st
import os
import base64
from pathlib import Path

# Directory to save uploaded files
UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(exist_ok=True)

st.title("PDF Upload and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved at {file_path}")

    # Display file
    st.write("File Preview:")
    st.download_button(
        label="Download PDF",
        data=open(file_path, "rb"),
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
    st.write(file_path)
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)