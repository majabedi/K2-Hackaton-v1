import streamlit as st
from dotenv import load_dotenv
import os
import sys
import pandas as pd

# Add the parent directory to the Python path to find openai_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from openai_utils import get_openai_response

# Load environment variables from .env file in the parent directory
load_dotenv()

st.set_page_config(page_title="File Viewer", page_icon="📄")

st.title("File Viewer")

# Check for environment variables
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")
model = os.getenv("OPENAI_MODEL")
env_vars_are_set = all([api_key, base_url, model])

if 'uploaded_file' in st.session_state:
    uploaded_file = st.session_state['uploaded_file']

    # Initialize session state for OpenAI response
    if 'openai_response' not in st.session_state:
        st.session_state['openai_response'] = None

    try:
        if st.session_state['openai_response']:
            st.markdown(st.session_state['openai_response'])
        else:
            if uploaded_file.type == "text/plain":
                string_data = uploaded_file.read().decode("utf-8")
                st.text(string_data)
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)
            else:
                st.write(uploaded_file.getvalue())

            if env_vars_are_set:
                if st.button("Get OpenAI Response"):
                    with st.spinner("Waiting for response..."):
                        if uploaded_file.type == "text/plain":
                            response = get_openai_response(string_data)
                        elif uploaded_file.type == "text/csv":
                            response = get_openai_response(df.to_string())
                        else:
                            response = "File type not supported for OpenAI analysis."

                        st.session_state['openai_response'] = response
                        st.rerun()
            else:
                st.warning("Please configure your OpenAI credentials in a `.env` file to use the OpenAI functionality.")


    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a file on the main page.")
