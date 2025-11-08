import streamlit as st

st.set_page_config(page_title="File Uploader", page_icon="📄")

st.title("Upload your sceintific data file!")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.session_state['uploaded_file'] = uploaded_file
    st.success("File uploaded successfully!")
    st.switch_page("pages/viewer.py")
