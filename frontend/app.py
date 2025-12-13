import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
test_url = "http://127.0.0.1:7071/rag/query"
url = f"https://zamzam-function-app.azurewebsites.net/rag/query?code={os.getenv('FUNCTION_APP_API')}"

def layout():

    st.markdown("# Kokchun´s youtube videos")
    st.markdown("Ask a question about Kokchun Giang's youtube videos")

    text_input = st.text_input(label="Ask a questions")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(url, json={"prompt": text_input}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data.get("answer", "No answer returned"))

if __name__ == "__main__":
    layout()