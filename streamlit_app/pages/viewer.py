import streamlit as st
import pandas as pd

st.set_page_config(page_title="File Viewer", page_icon="📄")

st.title("File Viewer")

if 'uploaded_file' in st.session_state:
    uploaded_file = st.session_state['uploaded_file']
    try:
        if uploaded_file.type == "text/plain":
            st.text(uploaded_file.read().decode("utf-8"))
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
        else:
            st.write(uploaded_file.getvalue())

    except Exception as e:
        st.error(f"Error displaying file: {e}")
else:
    st.info("Please upload a file on the main page.")
