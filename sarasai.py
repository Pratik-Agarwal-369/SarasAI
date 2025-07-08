import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_key"])

st.set_page_config(page_title="SarasAI", layout="centered", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: white;'>🌸 SarasAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Wisdom of the Divine. Powered by AI.</p>", unsafe_allow_html=True)

user_input = st.text_input("Ask SarasAI anything...")

if user_input:
    with st.spinner("Thinking like Saraswati..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.success("SarasAI says:")
        st.write(response.choices[0].message.content)

st.markdown("<footer style='text-align: center; color: gray; font-size: 12px;'>Made with 🕊️ by Pratik</footer>", unsafe_allow_html=True)
