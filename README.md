# K2-Hackaton-v1: A Streamlit Application for Research Paper Analysis

This project is a Streamlit application designed to assist users in analyzing research papers. It leverages OpenAI-compatible APIs to provide functionalities such as summarizing papers, extracting key information, and answering questions about the content.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the `streamlit_app` directory by copying the `.env.example` file:

```bash
cp streamlit_app/.env.example streamlit_app/.env
```

Then, edit the `streamlit_app/.env` file to include your specific credentials:

- `OPENAI_API_KEY`: Your API key for the OpenAI-compatible service.
- `OPENAI_API_BASE`: The base URL of the API.
- `OPENAI_MODEL`: The model you wish to use (e.g., `gpt-3.5-turbo`).

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run streamlit_app/app.py
```

## Project Structure

- `streamlit_app/`: Contains the main Streamlit application.
- `streamlit_app/app.py`: The entry point of the application.
- `streamlit_app/pages/`: Holds the different pages of the multi-page app.
- `streamlit_app/openai_utils.py`: A module for handling communication with the OpenAI-compatible API.
- `streamlit_app/.env.example`: An example file for configuring environment variables.
- `requirements.txt`: Lists the required Python packages for the project.
- `README.md`: Provides documentation for the project.
