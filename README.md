# K2-Hackaton-v1

## About

This project is a Streamlit application designed to assist users in analyzing research papers. It uses the K2 Think API to summarize papers, extract key information, and answer questions about the content.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/K2-Hackaton-v1.git
   cd K2-Hackaton-v1
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

To use this application, you need to configure your K2 Think API credentials in a `.env` file.

1. **Create a `.env` file in the `streamlit_app` directory:**
   ```bash
   cp streamlit_app/.env.example streamlit_app/.env
   ```

2. **Edit the `.env` file and add your API key:**
   ```
   OPENAI_API_KEY="Your K2 API"
   OPENAI_API_BASE="https://llm-api.k2think.ai/v1/"
   OPENAI_MODEL="MBZUAI-IFM/K2-Think"
   ```

## Usage

To run the Streamlit application, use the following command:

```bash
streamlit run streamlit_app/app.py
```
