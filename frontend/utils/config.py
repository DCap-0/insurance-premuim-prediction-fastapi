import os
import streamlit as st
from dotenv import load_dotenv
from streamlit.errors import StreamlitSecretNotFoundError

load_dotenv()


def get_api_url() -> str:
    # Try Streamlit secrets (safe)
    try:
        return st.secrets["API_URL"]
    except StreamlitSecretNotFoundError:
        pass
    except KeyError:
        pass

    # Try environment variable (.env or OS)
    api_url = os.getenv("API_URL")
    if api_url:
        return api_url

    # Fail clearly
    st.error("API_URL is not configured. Set it in .env or Streamlit secrets.")
    st.stop()
