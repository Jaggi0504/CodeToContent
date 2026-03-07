import streamlit as st
import import_ipynb
import tempfile

import main

st.title("README + LinkedIn Generator")

st.write("Upload a Jupyter Notebook to generate a README.md and LinkedIn post.")

uploaded_file = st.file_uploader(
    "Upload your notebook",
    type=["ipynb"]
)

if uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ipynb") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    # Use function from notebook
    notebook_content = main.load_notebook(temp_path)

    with st.spinner("Generating content..."):

        result = main.run_pipeline(notebook_content)

    st.subheader("Generated README")

    st.code(result["readme"], language="markdown")

    st.subheader("LinkedIn Post")

    st.write(result["linkedin_post"])